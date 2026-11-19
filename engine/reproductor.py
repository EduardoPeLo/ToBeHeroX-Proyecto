"""Ajustes del jugador, soundtrack y videos (archivo local o YouTube oficial)."""
from __future__ import annotations

import json
import os
import subprocess
import sys

import pygame

from engine import assets as A
from engine.game import ROOT, SAVE_DIR
from story import medios

AJUSTES_FILE = os.path.join(SAVE_DIR, "ajustes.json")
DEFAULTS = {"musica": True, "videos": True, "opening": True, "volumen": 60, "pistas": True}


def load_settings() -> dict:
    d = dict(DEFAULTS)
    try:
        with open(AJUSTES_FILE, encoding="utf-8") as f:
            d.update(json.load(f))
    except (OSError, ValueError):
        pass
    return d


def save_settings(d: dict):
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(AJUSTES_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=1)


def webview_ok() -> bool:
    try:
        import webview  # noqa: F401
        return True
    except ImportError:
        return False


def _spawn(vid: str, mode: str, title: str, vol: int, capture=False, extra=()) -> subprocess.Popen | None:
    if not webview_ok():
        return None
    flags = 0
    if sys.platform == "win32":
        flags = 0x08000000  # CREATE_NO_WINDOW: sin consola extra
    try:
        return subprocess.Popen([sys.executable, "-m", "engine.visor_web", vid, mode, title, str(vol),
                                 *[str(e) for e in extra]],
                                cwd=ROOT, creationflags=flags,
                                stdout=subprocess.PIPE if capture else subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
    except OSError:
        return None


class Soundtrack:
    """Música por capítulo: archivo en assets/musica o tema oficial de YouTube."""

    def __init__(self, settings: dict):
        self.settings = settings
        self.key = None
        self.proc: subprocess.Popen | None = None
        self.title = ""
        self.paused_key = None

    @property
    def enabled(self):
        return self.settings.get("musica", True)

    def _stop_proc(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=3)
            except subprocess.TimeoutExpired:
                self.proc.kill()
        self.proc = None

    def stop(self):
        self._stop_proc()
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()

    def play(self, key: str, force=False):
        if key == self.key and not force and (self.proc is None or self.proc.poll() is None):
            return
        self.key = key
        self.stop()
        if not self.enabled or not key:
            return
        path = A.music_path(key)
        info = medios.MUSICA.get(key)
        self.title = info[1] if info else key
        if path and pygame.mixer.get_init():
            try:
                pygame.mixer.music.load(path)
                pygame.mixer.music.set_volume(self.settings.get("volumen", 60) / 100)
                pygame.mixer.music.play(-1, fade_ms=800)
                return
            except pygame.error:
                pass
        if info:
            self.proc = _spawn(info[0], "audio", "To Be Hero X · Soundtrack", self.settings.get("volumen", 60))

    def toggle(self) -> bool:
        self.settings["musica"] = not self.enabled
        save_settings(self.settings)
        if self.enabled:
            self.play(self.key, force=True)
        else:
            self.stop()
        return self.enabled

    def pause_for_video(self):
        self.paused_key = self.key
        self.stop()

    def resume(self):
        if self.paused_key:
            self.play(self.paused_key, force=True)
        self.paused_key = None

    def shutdown(self):
        self.stop()


# Área (en coordenadas lógicas 1280x720) donde se incrusta el video dentro del juego.
VIDEO_RECT = pygame.Rect(176, 104, 928, 522)


def play_youtube_blocking(app, vid: str, title: str) -> bool:
    """Reproduce un video de YouTube incrustado en un recuadro dentro de la ventana del juego."""
    import math
    import time
    extra = ()
    mode = "video"
    try:
        hwnd = pygame.display.get_wm_info().get("window")
    except pygame.error:
        hwnd = None
    if hwnd and sys.platform == "win32":
        r = VIDEO_RECT
        mode = "widget"
        extra = (hwnd, r.x / app.W, r.y / app.H, r.w / app.W, r.h / app.H)
    proc = _spawn(vid, mode, title, 100, capture=True, extra=extra)
    if proc is None:
        return False
    t0 = time.time()
    snap = app.screen.copy()
    r = VIDEO_RECT
    skip = pygame.Rect(r.right - 250, r.bottom + 18, 250, 46)
    accent, ink = (255, 204, 0), (8, 8, 14)
    while app.running and proc.poll() is None:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                app.running = False
            elif ev.type == pygame.KEYDOWN and ev.key in (pygame.K_ESCAPE, pygame.K_SPACE, pygame.K_RETURN):
                proc.terminate()
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and skip.collidepoint(ev.pos):
                proc.terminate()
        t = time.time() - t0
        app.screen.blit(snap, (0, 0))
        app.dark(200)
        # marco del widget: solo el recuadro amarillo
        pygame.draw.rect(app.screen, (0, 0, 0), r)
        pygame.draw.rect(app.screen, accent, r.inflate(8, 8), 4)
        # (el video aparece encima de este recuadro; mientras carga se ve este aviso)
        dots = "." * (1 + int(t * 2) % 3)
        app.text("Cargando video" + dots, app.f, (200, 200, 215), r.center, center=True)
        hover = skip.collidepoint(pygame.mouse.get_pos())
        pygame.draw.polygon(app.screen, (60, 66, 104) if hover else (24, 27, 44),
                            [(skip.x + 14, skip.y), (skip.right, skip.y), (skip.right - 14, skip.bottom), (skip.x, skip.bottom)])
        pygame.draw.polygon(app.screen, accent,
                            [(skip.x + 14, skip.y), (skip.right, skip.y), (skip.right - 14, skip.bottom), (skip.x, skip.bottom)], 3)
        app.text("SALTAR (ESC)", app.f_name, (240, 240, 246), skip.center, center=True)
        pygame.display.flip()
        app.clock.tick(30)
    if proc.poll() is None:
        proc.terminate()
    try:
        out = proc.communicate(timeout=3)[0] or b""
    except (subprocess.TimeoutExpired, ValueError):
        out = b""
    if b"ERROR_YOUTUBE" in out:
        # el video no permite reproducirse incrustado: se abre en el navegador
        import webbrowser
        webbrowser.open(f"https://www.youtube.com/watch?v={vid}")
    return True
