"""Carga de imágenes, música y videos desde la carpeta assets/ (con respaldo generado)."""
from __future__ import annotations

import json
import os
import re
import unicodedata

import pygame

from engine import arte
from engine.game import ROOT

ASSETS = os.path.join(ROOT, "assets")
IMG_EXT = (".png", ".jpg", ".jpeg", ".webp", ".bmp")
AUDIO_EXT = (".ogg", ".mp3", ".wav")
VIDEO_EXT = (".mp4", ".webm", ".mkv", ".avi", ".mov")


def slug(name: str) -> str:
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def find(folder: str, key: str, exts) -> str | None:
    if not key:
        return None
    base = os.path.join(ASSETS, folder, key)
    for e in exts:
        if os.path.isfile(base + e):
            return base + e
    return None


def _anime_map() -> dict:
    try:
        with open(os.path.join(ASSETS, "anime", "mapa_fondos.json"), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


class Assets:
    def __init__(self, size):
        self.size = size
        self._bg = {}
        self._portrait = {}
        self.anime = _anime_map()

    # ---------- fondos ----------
    def background(self, key: str | None, color=(40, 40, 60)) -> pygame.Surface:
        ck = (key, color)
        if ck in self._bg:
            return self._bg[ck]
        path = find("fondos", key, IMG_EXT)
        anime = self.anime.get(key or "")
        if not path and anime and os.path.isfile(os.path.join(ASSETS, "anime", anime)):
            try:
                surf = self._cover(pygame.image.load(os.path.join(ASSETS, "anime", anime)).convert(), self.size)
                # suavizado y oscurecido para que se lean el texto y el retrato encima
                surf = pygame.transform.gaussian_blur(surf, 7)
                shade = pygame.Surface(self.size, pygame.SRCALPHA)
                shade.fill((0, 0, 0, 105))
                surf.blit(shade, (0, 0))
                self._bg[ck] = surf
                return surf
            except (pygame.error, ValueError):
                pass
        if path:
            try:
                surf = self._cover(pygame.image.load(path).convert(), self.size)
            except pygame.error:
                surf = arte.background(key, self.size, color)
        else:
            surf = arte.background(key, self.size, color)
        self._bg[ck] = surf
        return surf

    @staticmethod
    def _cover(img: pygame.Surface, size) -> pygame.Surface:
        w, h = size
        iw, ih = img.get_size()
        sc = max(w / iw, h / ih)
        img = pygame.transform.smoothscale(img, (int(iw * sc) + 1, int(ih * sc) + 1))
        out = pygame.Surface(size)
        out.blit(img, ((w - img.get_width()) // 2, (h - img.get_height()) // 2))
        return out

    def _generated(self, key, color) -> pygame.Surface:
        w, h = self.size
        surf = pygame.Surface(self.size)
        r, g, b = color
        for y in range(h):
            t = y / h
            surf.fill((int(r * (1 - t) * 0.9 + 8), int(g * (1 - t) * 0.9 + 8), int(b * (1 - t) * 0.9 + 14)),
                      (0, y, w, 1))
        lines = pygame.Surface(self.size, pygame.SRCALPHA)
        for x in range(-h, w, 46):
            pygame.draw.line(lines, (255, 255, 255, 12), (x, h), (x + h, 0), 2)
        surf.blit(lines, (0, 0))
        if key:
            font = pygame.font.SysFont("consolas,couriernew", 14)
            label = font.render(f"assets/fondos/{key}.png", True, (255, 255, 255))
            label.set_alpha(90)
            surf.blit(label, ((w - label.get_width()) // 2, 8))
        return surf

    # ---------- retratos ----------
    def card(self, num: int, name: str, size, color) -> pygame.Surface:
        """Arte de la carta de capítulo: assets/cartas/capXX.png o retrato del representante."""
        ck = ("card", num, size)
        if ck in self._bg:
            return self._bg[ck]
        surf = None
        card = find("cartas", f"cap{num:02d}", IMG_EXT)
        pers = find("personajes", slug(name), IMG_EXT)
        try:
            if card:
                raw = pygame.image.load(card)
                if raw.get_flags() & pygame.SRCALPHA:
                    img = raw.convert_alpha()
                    surf = arte.chapter_card(name, size, color, None, art=img)
                else:
                    surf = self._cover(raw.convert(), size)
            elif pers:
                surf = arte.chapter_card(name, size, color, pygame.image.load(pers).convert_alpha())
        except pygame.error:
            surf = None
        if surf is None:
            surf = arte.chapter_card(name, size, color)
        self._bg[ck] = surf
        return surf

    @staticmethod
    def _framed(img: pygame.Surface, h: int) -> pygame.Surface:
        """Captura sin transparencia: se muestra como carta inclinada con borde."""
        sc = h / img.get_height()
        img = pygame.transform.smoothscale(img, (int(img.get_width() * sc), h))
        w, sk = img.get_width(), int(h * .1)
        out = pygame.Surface((w, h), pygame.SRCALPHA)
        out.blit(img, (0, 0))
        mask = pygame.Surface((w, h), pygame.SRCALPHA)
        poly = [(sk, 0), (w, 0), (w - sk, h), (0, h)]
        pygame.draw.polygon(mask, (255, 255, 255, 255), poly)
        out.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
        pygame.draw.polygon(out, (255, 204, 0), poly, 6)
        return out

    def portrait(self, speaker: str | None, max_h: int) -> pygame.Surface | None:
        if not speaker:
            return None
        ck = (speaker, max_h)
        if ck in self._portrait:
            return self._portrait[ck]
        path = find("personajes", slug(speaker), IMG_EXT)
        surf = None
        if path:
            try:
                raw = pygame.image.load(path)
                if raw.get_flags() & pygame.SRCALPHA:
                    img = raw.convert_alpha()
                    sc = max_h / img.get_height()
                    surf = pygame.transform.smoothscale(img, (int(img.get_width() * sc), max_h))
                else:
                    surf = self._framed(raw.convert(), int(max_h * .86))
            except pygame.error:
                surf = None
        if surf is None:
            surf = arte.silhouette(speaker, max_h)
        self._portrait[ck] = surf
        return surf


def music_path(key: str) -> str | None:
    return find("musica", key, AUDIO_EXT)


def video_path(key: str) -> str | None:
    return find("videos", key, VIDEO_EXT)


def video_audio_path(key: str) -> str | None:
    return find("videos", key, AUDIO_EXT)
