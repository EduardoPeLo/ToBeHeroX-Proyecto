"""Interfaz gráfica (pygame) de la novela visual, con estilo 'hero shooter' (Marvel Rivals × To Be Hero X)."""
from __future__ import annotations

import math
import os
import random
import time

import pygame

from engine import arte
from engine import assets as A
from engine.game import (Game, State, X_CHAPTER, load_game, load_gallery, save_game,
                         save_path, unlock_ending)
from engine.reproductor import (Soundtrack, load_settings, play_youtube_blocking,
                                save_settings, webview_ok)
from story import load_story, medios

W, H = 1280, 720
FPS = 60
SLOTS = 3
SKEW = 18

COL = {
    "bg": (10, 11, 20), "panel": (12, 14, 26, 230), "text": (240, 240, 246),
    "dim": (150, 155, 175), "accent": (255, 204, 0), "red": (235, 64, 74),
    "blue": (90, 170, 255), "green": (80, 214, 120), "yellow": (255, 204, 0),
    "btn": (24, 27, 44), "btn_h": (44, 48, 78), "ink": (8, 8, 14),
}
TAGS = {
    "canon": ("CANON", COL["green"]),
    "minor": ("NO AFECTA DEL TODO AL CANON", COL["yellow"]),
    "major": ("MODIFICA EL CANON", COL["red"]),
}


def wrap(text: str, font: pygame.font.Font, width: int) -> list[str]:
    out = []
    for para in text.split("\n"):
        cur = ""
        for w in para.split(" "):
            test = (cur + " " + w).strip()
            if font.size(test)[0] <= width:
                cur = test
            else:
                if cur:
                    out.append(cur)
                cur = w
        out.append(cur)
    return out


def slant(rect, skew=SKEW):
    r = pygame.Rect(rect)
    return [(r.x + skew, r.y), (r.right, r.y), (r.right - skew, r.bottom), (r.x, r.bottom)]


def clip_slant(surf: pygame.Surface, skew: int) -> pygame.Surface:
    """Recorta una superficie con forma de paralelogramo."""
    w, h = surf.get_size()
    out = pygame.Surface((w, h), pygame.SRCALPHA)
    out.blit(surf, (0, 0))
    mask = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.polygon(mask, (255, 255, 255, 255), [(skew, 0), (w, 0), (w - skew, h), (0, h)])
    out.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return out


class Button:
    def __init__(self, rect, text, action, enabled=True, sub=None, sub_col=None, color=None, small=False):
        self.rect = pygame.Rect(rect)
        self.text, self.action, self.enabled = text, action, enabled
        self.sub, self.sub_col, self.color, self.small = sub, sub_col, color, small


class App:
    W, H = W, H

    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init()
        except pygame.error:
            pass
        pygame.display.set_caption("To Be Hero X — Hilos del Destino")
        self.screen = pygame.display.set_mode((W, H), pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        disp = "bahnschrift,impact,arialblack"
        self.f_logo = pygame.font.SysFont(disp, 150, bold=True)
        self.f_title = pygame.font.SysFont(disp, 64, bold=True)
        self.f_big = pygame.font.SysFont(disp, 40, bold=True)
        self.f_btn = pygame.font.SysFont(disp, 28, bold=True)
        self.f_h = pygame.font.SysFont(disp, 30, bold=True)
        self.f = pygame.font.SysFont("segoeui,arial", 24)
        self.f_s = pygame.font.SysFont("segoeui,arial", 18)
        self.f_xs = pygame.font.SysFont("bahnschrift,segoeui,arial", 15, bold=True)
        self.f_name = pygame.font.SysFont(disp, 26, bold=True)
        self.story = load_story()
        self.assets = A.Assets((W, H))
        self.settings = load_settings()
        self.music = Soundtrack(self.settings)
        self.game: Game | None = None
        self.slot = 1
        self.running = True
        self.toast = ("", 0.0)

    # ======================= utilidades de dibujo =======================
    @property
    def hints(self):
        return self.settings.get("pistas", True)

    def text(self, s, font, color, pos, center=False, alpha=255, right=False):
        surf = font.render(s, True, color)
        if alpha < 255:
            surf.set_alpha(max(0, alpha))
        r = surf.get_rect()
        if center:
            r.center = pos
        elif right:
            r.topright = pos
        else:
            r.topleft = pos
        self.screen.blit(surf, r)
        return r

    def italic_text(self, s, font, color, pos, angle=6, center=True, outline=None):
        surf = font.render(s, True, color)
        if outline:
            base = pygame.Surface((surf.get_width() + 8, surf.get_height() + 8), pygame.SRCALPHA)
            o = font.render(s, True, outline)
            for dx, dy in ((-3, 0), (3, 0), (0, -3), (0, 3), (4, 4)):
                base.blit(o, (4 + dx, 4 + dy))
            base.blit(surf, (4, 4))
            surf = base
        surf = pygame.transform.rotozoom(surf, 0, 1)
        # cizalla simulada: rotar ligeramente da el aire 'dinámico'
        surf = pygame.transform.rotate(surf, angle)
        r = surf.get_rect(center=pos) if center else surf.get_rect(topleft=pos)
        self.screen.blit(surf, r)
        return r

    def panel(self, rect, color=None, radius=12):
        r = pygame.Rect(rect)
        s = pygame.Surface(r.size, pygame.SRCALPHA)
        pygame.draw.rect(s, color or COL["panel"], s.get_rect(), border_radius=radius)
        self.screen.blit(s, r.topleft)

    def slant_panel(self, rect, color, skew=SKEW, border=None):
        r = pygame.Rect(rect)
        s = pygame.Surface(r.size, pygame.SRCALPHA)
        pygame.draw.polygon(s, color, slant((0, 0, r.w, r.h), skew))
        self.screen.blit(s, r.topleft)
        if border:
            pygame.draw.polygon(self.screen, border, slant(r, skew), 3)

    def dark(self, alpha=140):
        s = pygame.Surface((W, H), pygame.SRCALPHA)
        s.fill((0, 0, 0, alpha))
        self.screen.blit(s, (0, 0))

    def stripes(self, t, color=(255, 204, 0), alpha=30, count=6, offset=0):
        s = pygame.Surface((W, H), pygame.SRCALPHA)
        for i in range(count):
            x = (i * 260 + int(t * 40) + offset) % (W + 600) - 300
            pygame.draw.polygon(s, (*color, alpha), [(x, 0), (x + 60, 0), (x - 240, H), (x - 300, H)])
        self.screen.blit(s, (0, 0))

    def draw_buttons(self, buttons, mouse):
        for b in buttons:
            hover = b.enabled and b.rect.collidepoint(mouse)
            r = b.rect.move(10 if hover else 0, 0)
            base = b.color or COL["accent"]
            fill = COL["btn_h"] if hover else COL["btn"]
            if not b.enabled:
                fill = (20, 20, 30)
            pygame.draw.polygon(self.screen, fill, slant(r))
            if b.enabled:
                pygame.draw.polygon(self.screen, base, slant((r.x, r.y, 26, r.h), 10 if r.h < 60 else SKEW))
            if b.color and b.enabled:
                tint = pygame.Surface(r.size, pygame.SRCALPHA)
                pygame.draw.polygon(tint, (*base, 70 if hover else 34), slant((0, 0, r.w, r.h)))
                self.screen.blit(tint, r.topleft)
            pygame.draw.polygon(self.screen, base if (hover or b.color) else (70, 76, 110), slant(r), 4 if hover else 3)
            font = self.f_s if b.small else (self.f_btn if not b.sub and len(b.text) < 28 else self.f)
            lines = wrap(b.text, font, r.w - 70)
            lh = font.get_linesize()
            total = len(lines) * lh + (20 if b.sub else 0)
            y = r.centery - total // 2
            for ln in lines:
                self.text(ln, font, COL["text"] if b.enabled else COL["dim"], (r.x + 44, y))
                y += lh
            if b.sub:
                self.text(b.sub, self.f_xs, b.sub_col or COL["dim"], (r.x + 44, y + 1))

    def show_toast(self, msg):
        self.toast = (msg, time.time())

    def draw_toast(self):
        msg, t = self.toast
        if msg and time.time() - t < 2.5:
            a = 255 if time.time() - t < 2 else int(255 * (2.5 - (time.time() - t)) / .5)
            w = self.f_s.size(msg)[0] + 60
            self.slant_panel((W // 2 - w // 2, 64, w, 36), (0, 0, 0, 200), 12, COL["accent"])
            self.text(msg, self.f_s, COL["accent"], (W // 2, 82), center=True, alpha=a)

    def handle_global_key(self, ev) -> bool:
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
                return True
            if ev.key == pygame.K_m:
                on = self.music.toggle()
                self.show_toast(("Soundtrack activado: " + self.music.title) if on else "Soundtrack desactivado")
                return True
        return False

    def menu_loop(self, draw_fn, buttons, keymap=None):
        while self.running:
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    return None
                if self.handle_global_key(ev):
                    continue
                if ev.type == pygame.KEYDOWN and keymap and ev.key in keymap:
                    return keymap[ev.key]
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    for b in buttons:
                        if b.enabled and b.rect.collidepoint(ev.pos):
                            return b.action
            draw_fn()
            self.draw_buttons(buttons, mouse)
            self.draw_toast()
            pygame.display.flip()
            self.clock.tick(FPS)
        return None

    def wait_click(self, draw_fn):
        while self.running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    return
                if self.handle_global_key(ev):
                    continue
                if ev.type == pygame.KEYDOWN and ev.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                    return
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    return
            draw_fn()
            self.draw_toast()
            pygame.display.flip()
            self.clock.tick(FPS)

    def confirm(self, question) -> bool:
        snap = self.screen.copy()
        buttons = [Button((W // 2 - 260, 380, 240, 56), "SÍ", True, color=COL["green"]),
                   Button((W // 2 + 20, 380, 240, 56), "NO", False, color=COL["red"])]

        def draw():
            self.screen.blit(snap, (0, 0))
            self.dark(190)
            for i, ln in enumerate(wrap(question, self.f, 760)):
                self.text(ln, self.f, COL["text"], (W // 2, 290 + i * 32), center=True)
        return bool(self.menu_loop(draw, buttons, {pygame.K_ESCAPE: False, pygame.K_RETURN: True}))

    # ======================= videos =======================
    def play_local_video(self, key) -> bool:
        path = A.video_path(key)
        if not path:
            return False
        try:
            import cv2
        except ImportError:
            return False
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            return False
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        audio = A.video_audio_path(key)
        if audio and pygame.mixer.get_init():
            try:
                pygame.mixer.music.load(audio)
                pygame.mixer.music.play()
            except pygame.error:
                pass
        start, frame_i = time.time(), 0
        while self.running:
            stop = False
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    stop = True
                elif ev.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    stop = True
            if stop:
                break
            target = int((time.time() - start) * fps)
            ok, frame = True, None
            while frame_i <= target and ok:
                ok, frame = cap.read()
                frame_i += 1
            if not ok or frame is None:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w = frame.shape[:2]
            surf = pygame.image.frombuffer(frame.tobytes(), (w, h), "RGB")
            sc = min(W / w, H / h)
            surf = pygame.transform.smoothscale(surf, (int(w * sc), int(h * sc)))
            self.screen.fill((0, 0, 0))
            self.screen.blit(surf, ((W - surf.get_width()) // 2, (H - surf.get_height()) // 2))
            self.text("Pulsa cualquier tecla para saltar", self.f_s, COL["dim"], (W - 300, H - 30), alpha=140)
            pygame.display.flip()
            self.clock.tick(fps)
        cap.release()
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
        return True

    def play_media(self, local_key, yt_id=None, title="") -> bool:
        """Reproduce un video: primero archivo local; si no, el video oficial de YouTube."""
        if not self.settings.get("videos", True):
            return False
        self.music.pause_for_video()
        shown = self.play_local_video(local_key)
        if not shown and yt_id:
            shown = play_youtube_blocking(self, yt_id, title)
        self.music.resume()
        return shown

    # ======================= flujo principal =======================
    def run(self):
        if self.settings.get("opening", True):
            self.screen.blit(self.assets.background("titulo", (30, 30, 90)), (0, 0))
            self.play_media("opening", medios.OPENING, "Opening · INERTIA — SawanoHiroyuki[nZk]:Rei")
        while self.running:
            action = self.title_screen()
            if action == "new":
                slot = self.slot_screen("NUEVA PARTIDA")
                if slot:
                    self.slot = slot
                    self.game = Game(self.story, State())
                    save_game(self.game.state, slot)
                    self.chapter_select(unlock=1)
            elif action == "load":
                slot = self.slot_screen("CONTINUAR", load=True)
                if slot and load_game(slot):
                    self.slot = slot
                    self.game = Game(self.story, load_game(slot))
                    self.chapter_select()
            elif action == "gallery":
                self.gallery_screen()
            elif action == "settings":
                self.settings_screen()
            elif action == "help":
                self.help_screen()
            elif action in ("quit", None):
                self.running = False
        self.music.shutdown()
        pygame.quit()

    # ---------- título ----------
    def title_screen(self):
        self.music.play("titulo")
        bg = self.assets.background("titulo", (30, 30, 90))
        heroes = ["Lin Ling", "E-Soul", "Cyan", "Queen", "Loli", "Ghostblade", "Little Johnny", "Dragon Boy", "Ahu"]
        cards = [self.assets.card(i + 1, n, (120, 300), self.story.chapters[i + 1].color) for i, n in enumerate(heroes)]
        x_card = self.assets.card(11, "X", (200, 470), (40, 40, 60))
        has_save = any(os.path.isfile(save_path(i)) for i in range(1, SLOTS + 1))
        labels = [("CONTINUAR", "load", has_save), ("NUEVA PARTIDA", "new", True), ("FINALES", "gallery", True),
                  ("AJUSTES", "settings", True), ("CRÉDITOS", "help", True), ("SALIR", "quit", True)]
        buttons = [Button((60, 330 + i * 58, 330, 48), t, a, e) for i, (t, a, e) in enumerate(labels)]
        t0 = time.time()
        trust0 = random.randint(9_000_000, 12_000_000)

        def draw():
            t = time.time() - t0
            self.screen.blit(bg, (0, 0))
            self.dark(120)
            self.stripes(t, alpha=26)
            # gran X de fondo
            big = self.f_logo.render("X", True, COL["accent"])
            big = pygame.transform.rotozoom(big, -8, 4.2)
            big.set_alpha(28)
            self.screen.blit(big, big.get_rect(center=(int(W * .72), int(H * .45))))
            # alineación de héroes (cartas inclinadas)
            for i, c in enumerate(cards):
                x = 470 + i * 84
                y = 250 + (i % 2) * 40 + int(6 * math.sin(t * 1.4 + i))
                cs = clip_slant(c, 26)
                self.screen.blit(cs, (x, y))
                pygame.draw.polygon(self.screen, COL["ink"], slant((x, y, 120, 300), 26), 4)
            xs = clip_slant(x_card, 40)
            self.screen.blit(xs, (W - 300, 190 + int(4 * math.sin(t * 2))))
            pygame.draw.polygon(self.screen, COL["accent"], slant((W - 300, 190 + int(4 * math.sin(t * 2)), 200, 470), 40), 5)
            # logo
            self.slant_panel((40, 50, 560, 200), (0, 0, 0, 150), 30)
            self.italic_text("TO BE HERO", self.f_title, COL["text"], (240, 104), 4, outline=COL["ink"])
            self.italic_text("X", self.f_logo, COL["accent"], (510, 130), 4, outline=COL["ink"])
            self.slant_panel((56, 192, 380, 42), COL["accent"], 14)
            self.text("HILOS DEL DESTINO", self.f_h, COL["ink"], (246, 213), center=True)
            self.text("En este mundo, la confianza de la gente se convierte en poder.", self.f_s, COL["text"], (64, 262))
            self.text("El héroe con más confianza recibe un nombre: X.", self.f_s, COL["accent"], (64, 286))
            # contador de confianza
            val = trust0 + int(t * 1371)
            self.slant_panel((W - 430, 24, 400, 46), (0, 0, 0, 170), 16, COL["blue"])
            self.text(f"CONFIANZA GLOBAL  +{val:,}", self.f_name, COL["blue"], (W - 230, 47), center=True)
            # pie
            mus = ("Sonando: " + self.music.title) if self.music.enabled else "Soundtrack apagado"
            self.text(f"{mus}   ·   [M] música   ·   [F11] pantalla completa", self.f_xs, COL["dim"], (60, H - 34))
            self.text("Creado por Eduardo Pedroza López y Rogelio Uriel Gutierrez Jimenez", self.f_xs, COL["dim"],
                      (W - 30, H - 34), right=True)
        return self.menu_loop(draw, buttons, {pygame.K_ESCAPE: "quit"})

    def slot_screen(self, title, load=False):
        buttons = []
        for i in range(1, SLOTS + 1):
            st = load_game(i)
            if st:
                ch = self.story.chapters[st.chapter]
                desc = f"Cap. {st.chapter}: {ch.title} · {st.decisions} decisiones · " + \
                       ("hilo intacto" if st.thread_intact else "hilo alterado")
                if st.ending:
                    desc = f"Final obtenido: {self.story.endings[st.ending].title}"
            else:
                desc = "Vacío"
            buttons.append(Button((W // 2 - 340, 200 + (i - 1) * 110, 680, 90), f"ESPACIO {i}", i,
                                  enabled=(st is not None) or not load, sub=desc))
        buttons.append(Button((W // 2 - 130, 560, 260, 50), "VOLVER", None))
        bg = self.assets.background("titulo", (30, 30, 90))
        t0 = time.time()

        def draw():
            self.screen.blit(bg, (0, 0))
            self.dark(180)
            self.stripes(time.time() - t0, alpha=18)
            self.italic_text(title, self.f_title, COL["accent"], (W // 2, 110), 3, outline=COL["ink"])
            if not load:
                self.text("Si eliges un espacio ocupado, se sobrescribirá.", self.f_s, COL["dim"], (W // 2, 165), center=True)
        return self.menu_loop(draw, buttons, {pygame.K_ESCAPE: None})

    # ---------- selección de capítulo ----------
    def chapter_status(self, num):
        st = self.game.state
        if num in st.done:
            return "done"
        if num == X_CHAPTER and (not st.thread_intact):
            return "sealed"
        if num == st.chapter and not st.ending:
            return "current"
        return "locked"

    def chapter_select(self, unlock=None, sealed_anim=False):
        while self.running and self.game:
            action = self._chapter_select_screen(unlock, sealed_anim)
            unlock, sealed_anim = None, False
            if action is None or action == "back":
                return
            kind, num = action
            if kind == "trailer":
                self.play_media(f"trailer_cap{num:02d}", medios.TRAILERS.get(num),
                                f"Tráiler oficial · {self.story.chapters[num].title}")
                continue
            if kind == "replay":
                if not self.confirm(f"¿Repetir el capítulo {num} desde el principio? Se perderá el progreso de "
                                    "los capítulos posteriores en este espacio de guardado."):
                    continue
                self.game.replay(num)
                save_game(self.game.state, self.slot)
            res = self.play_chapter_loop()
            if res is None:
                return
            if res[0] == "unlock":
                unlock = res[1]
            elif res[0] == "ending":
                sealed_anim = not self.game.state.thread_intact and X_CHAPTER not in self.game.state.done

    def _chapter_select_screen(self, unlock, sealed_anim):
        self.music.play("titulo")
        st = self.game.state
        nums = sorted(self.story.chapters)
        cw, chh, gap = 104, 360, 8
        x0 = (W - (len(nums) * (cw + gap) - gap + 30)) // 2
        y0 = 120
        arts = {n: self.assets.card(n, medios.REPRESENTANTE[n], (cw + 30, chh), self.story.chapters[n].color) for n in nums}
        grays = {n: pygame.transform.grayscale(a) for n, a in arts.items()}
        sel = st.chapter if not st.ending else max(st.done or [1])
        if unlock:
            sel = unlock
        t0 = time.time()
        anim_t = 1.6 if (unlock or sealed_anim) else 0
        bg = self.assets.background("fuera_del_tiempo", (30, 20, 60))
        rng = random.Random(3)
        shards = []

        def card_rect(n):
            i = nums.index(n)
            return pygame.Rect(x0 + i * (cw + gap), y0, cw + 30, chh)

        def detail_buttons():
            stt = self.chapter_status(sel)
            out = []
            if stt == "current":
                label = "CONTINUAR" if self.game.node.id != self.story.chapters[sel].start else "JUGAR"
                out.append(Button((60, 600, 260, 56), label, ("play", sel), color=COL["green"]))
            elif stt == "done" and self.game.can_replay(sel):
                out.append(Button((60, 600, 260, 56), "REPETIR", ("replay", sel), color=COL["yellow"]))
            if medios.TRAILERS.get(sel) and webview_ok():
                out.append(Button((340, 600, 300, 56), "VER TRÁILER", ("trailer", sel), color=COL["blue"]))
            out.append(Button((W - 260, 600, 200, 56), "MENÚ", "back", color=COL["red"]))
            return out

        while self.running:
            t = time.time() - t0
            mouse = pygame.mouse.get_pos()
            buttons = detail_buttons()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    return None
                if self.handle_global_key(ev):
                    continue
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        return "back"
                    if ev.key == pygame.K_LEFT:
                        sel = nums[max(0, nums.index(sel) - 1)]
                    if ev.key == pygame.K_RIGHT:
                        sel = nums[min(len(nums) - 1, nums.index(sel) + 1)]
                    if ev.key == pygame.K_RETURN and self.chapter_status(sel) == "current" and t > anim_t:
                        return ("play", sel)
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and t > anim_t:
                    for b in buttons:
                        if b.rect.collidepoint(ev.pos):
                            return b.action
                    for n in nums:
                        if card_rect(n).collidepoint(ev.pos):
                            if n == sel and self.chapter_status(n) == "current":
                                return ("play", n)
                            sel = n
            # ---- dibujo ----
            self.screen.blit(bg, (0, 0))
            self.dark(150)
            self.stripes(t, alpha=20)
            self.slant_panel((40, 26, 560, 64), COL["accent"], 26)
            self.text("SELECCIONA CAPÍTULO", self.f_big, COL["ink"], (320, 58), center=True)
            intact = st.thread_intact
            self.slant_panel((W - 470, 34, 430, 48), (0, 0, 0, 180), 16, COL["green"] if intact else COL["red"])
            self.text("HILO DEL DESTINO: " + ("INTACTO" if intact else "ALTERADO"), self.f_name,
                      COL["green"] if intact else COL["red"], (W - 255, 58), center=True)
            for n in nums:
                r = card_rect(n)
                stt = self.chapter_status(n)
                animating = unlock == n and t < anim_t
                if animating:
                    stt_draw = "locked"
                else:
                    stt_draw = stt
                hover = r.collidepoint(mouse)
                lift = -14 if n == sel else (-6 if hover else 0)
                rr = r.move(0, lift)
                art = arts[n] if stt_draw in ("done", "current") else grays[n]
                surf = clip_slant(art, 30)
                if stt_draw in ("locked", "sealed"):
                    dk = pygame.Surface(surf.get_size(), pygame.SRCALPHA)
                    dk.fill((0, 0, 0, 150))
                    surf.blit(dk, (0, 0), special_flags=0)
                    surf = clip_slant(surf, 30)
                self.screen.blit(surf, rr.topleft)
                border = {"done": COL["green"], "current": COL["accent"], "locked": (70, 70, 90),
                          "sealed": COL["red"]}[stt_draw]
                if n == sel:
                    pulse = int(3 + 2 * math.sin(t * 6))
                    pygame.draw.polygon(self.screen, COL["accent"], slant(rr.inflate(8, 8), 32), 3 + pulse)
                pygame.draw.polygon(self.screen, border, slant(rr, 30), 4)
                # número
                self.slant_panel((rr.x + 6, rr.bottom - 54, 78, 40), (0, 0, 0, 200), 10)
                self.text(f"{n:02d}", self.f_h, COL["text"], (rr.x + 44, rr.bottom - 34), center=True)
                if stt_draw == "locked":
                    self._lock_icon(rr.centerx + 8, rr.y + 150, shake=(animating and t > anim_t - .8) * 6 * math.sin(t * 60))
                elif stt_draw == "sealed":
                    self._seal_icon(rr, t)
                elif stt_draw == "done":
                    pygame.draw.circle(self.screen, COL["green"], (rr.right - 30, rr.y + 26), 16)
                    pygame.draw.lines(self.screen, COL["ink"], False,
                                      [(rr.right - 38, rr.y + 26), (rr.right - 31, rr.y + 33), (rr.right - 20, rr.y + 19)], 4)
            # animación de desbloqueo
            if unlock and anim_t - .05 < t < anim_t + .25 and not shards:
                r = card_rect(unlock)
                for _ in range(40):
                    shards.append([r.centerx, r.y + 150, rng.uniform(-12, 12), rng.uniform(-14, 4), 1.0])
            if shards:
                for s in shards:
                    s[0] += s[2]; s[1] += s[3]; s[3] += .5; s[4] -= .02
                    if s[4] > 0:
                        pygame.draw.rect(self.screen, COL["accent"], (s[0], s[1], 6, 6))
                shards[:] = [s for s in shards if s[4] > 0]
            if unlock and anim_t <= t < anim_t + .2:
                fl = pygame.Surface((W, H), pygame.SRCALPHA)
                fl.fill((255, 255, 255, int(200 * (1 - (t - anim_t) / .2))))
                self.screen.blit(fl, (0, 0))
            if unlock and anim_t <= t < anim_t + 2.4:
                label = "¡CAPÍTULO FINAL DESBLOQUEADO!" if unlock == X_CHAPTER else f"¡CAPÍTULO {unlock} DESBLOQUEADO!"
                self.slant_panel((W // 2 - 330, 270, 660, 70), (*COL["accent"], 235), 30)
                self.text(label, self.f_big, COL["ink"], (W // 2, 305), center=True)
            if sealed_anim and t < 3.0:
                self.slant_panel((W // 2 - 380, 270, 760, 70), (*COL["red"], 235), 30)
                self.text("EL CAPÍTULO DE X PERMANECE SELLADO", self.f_big, COL["ink"], (W // 2, 305), center=True)
            # panel de detalle
            ch = self.story.chapters[sel]
            stt = self.chapter_status(sel)
            self.slant_panel((40, 500, W - 80, 90), (0, 0, 0, 190), 24)
            self.text(f"CAPÍTULO {sel}" if sel != X_CHAPTER else "CAPÍTULO FINAL", self.f_xs, COL["accent"], (80, 510))
            self.text(ch.title.upper(), self.f_big, COL["text"], (80, 528))
            self.text(ch.eps + " del anime", self.f_s, COL["dim"], (80 + self.f_big.size(ch.title.upper())[0] + 20, 545))
            status_txt = {"done": ("COMPLETADO", COL["green"]), "current": ("DISPONIBLE", COL["accent"]),
                          "locked": ("BLOQUEADO: completa el capítulo anterior", COL["dim"]),
                          "sealed": ("SELLADO: el hilo del destino fue alterado", COL["red"])}[stt]
            self.text(status_txt[0], self.f_name, status_txt[1], (W - 80, 512), right=True)
            if stt in ("done", "current"):
                intro = wrap(ch.intro, self.f_s, 700)[0]
                self.text(intro, self.f_s, COL["text"], (W - 80, 552), right=True)
            self.draw_buttons(buttons, mouse)
            self.text("FLECHAS elegir · ENTER jugar · M música · ESC menú", self.f_xs, COL["dim"], (W // 2, H - 22), center=True)
            self.draw_toast()
            pygame.display.flip()
            self.clock.tick(FPS)
        return None

    def _lock_icon(self, cx, cy, shake=0):
        cx += shake
        pygame.draw.arc(self.screen, (200, 200, 210), (cx - 18, cy - 34, 36, 40), 0, math.pi, 6)
        pygame.draw.rect(self.screen, (200, 200, 210), (cx - 24, cy - 14, 48, 38), border_radius=6)
        pygame.draw.rect(self.screen, COL["ink"], (cx - 24, cy - 14, 48, 38), 3, border_radius=6)
        pygame.draw.circle(self.screen, COL["ink"], (int(cx), cy + 2), 5)

    def _seal_icon(self, r, t):
        for i in range(2):
            y = r.y + 110 + i * 120
            pygame.draw.line(self.screen, COL["red"], (r.x, y), (r.right, y + 60), 6)
            pygame.draw.line(self.screen, COL["red"], (r.right, y), (r.x, y + 60), 6)
        self.text("SELLADO", self.f_xs, COL["red"], (r.centerx + 6, r.y + 300), center=True)

    # ---------- juego ----------
    def autosave(self):
        if self.game:
            save_game(self.game.state, self.slot)

    def chapter_intro(self):
        ch = self.game.chapter
        self.music.play(f"cap{ch.num:02d}")
        self.play_local_video(f"cap{ch.num:02d}_intro")
        bg = self.assets.background(f"cap{ch.num:02d}_titulo", ch.color)
        art = self.assets.card(ch.num, medios.REPRESENTANTE[ch.num], (300, 560), ch.color)
        t0 = time.time()

        def draw():
            t = time.time() - t0
            self.screen.blit(bg, (0, 0))
            self.dark(150)
            self.stripes(t, color=ch.color, alpha=60)
            slide = max(0, 1 - t * 2.5)
            self.screen.blit(clip_slant(art, 60), (W - 420 + int(400 * slide), 90))
            a = min(255, int(t * 300))
            label = "CAPÍTULO FINAL" if ch.num == X_CHAPTER else f"CAPÍTULO {ch.num}"
            self.slant_panel((80 - int(500 * slide), 170, 300, 48), COL["accent"], 18)
            self.text(label, self.f_h, COL["ink"], (230 - int(500 * slide), 194), center=True)
            self.italic_text(ch.title.upper(), self.f_title, COL["text"], (90, 230), 3, center=False, outline=COL["ink"])
            self.text(ch.eps + " del anime", self.f_s, COL["dim"], (96, 320), alpha=a)
            y = 370
            for ln in wrap(ch.intro, self.f, 700):
                self.text(ln, self.f, COL["text"], (96, y), alpha=a)
                y += 32
            if self.music.enabled:
                self.text("SONANDO: " + self.music.title.upper(), self.f_xs, COL["accent"], (96, H - 80), alpha=a)
            self.text("Haz clic para comenzar", self.f_s, COL["dim"], (96, H - 50),
                      alpha=int(128 + 127 * math.sin(time.time() * 3)))
        self.wait_click(draw)

    def play_chapter_loop(self):
        """Juega el capítulo actual. Devuelve ('unlock', n), ('ending', key) o None (salió al menú)."""
        self.chapter_intro()
        while self.running and self.game:
            node = self.game.node
            if node.kind == "end":
                result = self.chapter_end_screen()
                if result is None:
                    return None
                self.autosave()
                if result == "ending":
                    self.ending_screen(self.game.state.ending)
                    return ("ending", self.game.state.ending)
                return ("unlock", self.game.state.chapter)
            if node.kind == "fight":
                if not self.fight_screen(node):
                    return None
                self.game.advance()
                self.autosave()
                continue
            if self.scene_screen(node) == "quit":
                self.autosave()
                return None
        return None

    def hud(self):
        st = self.game.state
        ch = self.game.chapter
        self.slant_panel((16, 14, 430, 40), (0, 0, 0, 170), 14)
        self.text(f"CAP. {ch.num} · {ch.title.upper()}", self.f_name, COL["text"], (44, 20))
        intact = st.thread_intact
        col = COL["green"] if intact else COL["red"]
        self.slant_panel((W - 400, 14, 384, 40), (0, 0, 0, 170), 14)
        x0, y0 = W - 380, 34
        for i in range(10):
            xx = x0 + i * 12
            if intact or i % 3:
                pygame.draw.line(self.screen, col, (xx, y0 + int(4 * math.sin(i + time.time() * 2))),
                                 (xx + 12, y0 + int(4 * math.sin(i + 1 + time.time() * 2))), 3)
        self.text("HILO DEL DESTINO: " + ("INTACTO" if intact else "ALTERADO"), self.f_xs, col, (W - 250, 25))
        self.text(("MÚSICA ON (M)" if self.music.enabled else "MÚSICA OFF (M)"), self.f_xs, COL["dim"], (W - 30, 60), right=True)

    def draw_scene_base(self, node, speaker, t_speaker):
        ch = self.game.chapter
        self.screen.blit(self.assets.background(node.bg, ch.color), (0, 0))
        port = self.assets.portrait(speaker, 480) if speaker else None
        if port:
            slide = max(0.0, 1 - (time.time() - t_speaker) * 5)
            x = 50 - int(120 * slide)
            glow = pygame.Surface((port.get_width() + 60, 80), pygame.SRCALPHA)
            pygame.draw.ellipse(glow, (0, 0, 0, 120), glow.get_rect())
            self.screen.blit(glow, (x - 30, H - 240))
            port = port.copy()
            port.set_alpha(int(255 * (1 - slide)))
            self.screen.blit(port, (x, H - 200 - port.get_height() + 40))
        self.hud()

    def scene_screen(self, node):
        clip = medios.ESCENAS.get(node.id)
        if clip and self.settings.get("videos", True):
            self.play_media(f"escena_{node.id}", clip[0], clip[1])
            if not self.running:
                return "quit"
        lines = self.game.visible_lines(node)
        opts = self.game.options(node)
        if not lines and not opts:
            self.game.advance()
            return "ok"
        idx, t_line = 0, time.time()
        last_speaker, t_speaker = None, time.time()
        choosing = not lines and bool(opts)
        while self.running:
            ln = lines[idx] if lines and idx < len(lines) else None
            speaker = ln.speaker if ln else None
            if speaker != last_speaker:
                last_speaker, t_speaker = speaker, time.time()
            full = ln.text if ln else ""
            shown = min(len(full), (time.time() - t_line) * 55)
            done_typing = shown >= len(full)
            buttons = self.choice_buttons(node, opts) if choosing else []
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    return "quit"
                if self.handle_global_key(ev):
                    continue
                adv = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        if self.pause_menu() == "quit":
                            return "quit"
                    elif ev.key == pygame.K_p:
                        self.settings["pistas"] = not self.hints
                        save_settings(self.settings)
                    elif ev.key == pygame.K_h:
                        self.history_screen()
                    elif ev.key in (pygame.K_SPACE, pygame.K_RETURN) and not choosing:
                        adv = True
                    elif choosing and pygame.K_1 <= ev.key <= pygame.K_9:
                        i = ev.key - pygame.K_1
                        if i < len(opts):
                            self.game.choose(opts[i])
                            self.autosave()
                            return "ok"
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    if choosing:
                        for b in buttons:
                            if b.rect.collidepoint(ev.pos):
                                self.game.choose(b.action)
                                self.autosave()
                                return "ok"
                    else:
                        adv = True
                if adv:
                    if not done_typing:
                        t_line = 0
                    else:
                        idx += 1
                        t_line = time.time()
                        if idx >= len(lines):
                            if opts:
                                choosing = True
                                idx = len(lines) - 1
                            else:
                                self.game.advance()
                                self.autosave()
                                return "ok"
            self.draw_scene_base(node, None if choosing else speaker, t_speaker)
            if choosing:
                self.dark(120)
                if node.ask:
                    self.slant_panel((W // 2 - 500, 84, 1000, 60), (0, 0, 0, 210), 22, COL["accent"])
                    self.text(node.ask, self.f_name, COL["accent"], (W // 2, 114), center=True)
                self.draw_buttons(buttons, mouse)
                if self.hints:
                    self._legend()
            elif ln:
                self.draw_textbox(speaker, full[:int(shown)], done_typing)
            self.draw_toast()
            pygame.display.flip()
            self.clock.tick(FPS)
        return "quit"

    def _legend(self):
        x = 60
        for tag in ("canon", "minor", "major"):
            label, col = TAGS[tag]
            pygame.draw.polygon(self.screen, col, slant((x, H - 44, 22, 18), 6))
            self.text(label, self.f_xs, col, (x + 30, H - 44))
            x += 46 + self.f_xs.size(label)[0]
        self.text("P: ocultar colores", self.f_xs, COL["dim"], (W - 40, H - 44), right=True)

    def choice_buttons(self, node, opts):
        n = len(opts)
        bh = 76
        top = max(170, H // 2 - (n * (bh + 14)) // 2 + 20)
        out = []
        for i, o in enumerate(opts):
            label, col = TAGS[o.tag]
            if not self.hints:
                label, col = None, (150, 150, 170)
            out.append(Button((W // 2 - 460, top + i * (bh + 14), 920, bh), f"{i + 1}. {o.text}", o,
                              sub=label, sub_col=col, color=col))
        return out

    def draw_textbox(self, speaker, text, done):
        box = pygame.Rect(40, H - 210, W - 80, 180)
        self.panel(box, (10, 12, 24, 235), 6)
        pygame.draw.line(self.screen, COL["accent"], (box.x, box.y), (box.right, box.y), 4)
        if speaker:
            name = speaker if speaker != "Voz" else "???"
            tw = self.f_name.size(name.upper())[0] + 60
            self.slant_panel((box.x + 20, box.y - 26, tw, 42), COL["accent"], 16)
            self.text(name.upper(), self.f_name, COL["ink"], (box.x + 50, box.y - 20))
        color = COL["text"] if speaker else (205, 212, 235)
        font = self.f if speaker else pygame.font.SysFont("segoeui,arial", 24, italic=True)
        y = box.y + 34
        for ln in wrap(text, font, box.w - 60):
            self.text(ln, font, color, (box.x + 30, y))
            y += 32
        if done:
            self.text("▼", self.f_s, COL["accent"], (box.right - 36, box.bottom - 34 + int(3 * math.sin(time.time() * 6))))

    # ---------- peleas ----------
    def fight_screen(self, node) -> bool:
        f = node.fight
        ch = self.game.chapter
        info = medios.PELEAS.get(node.id)
        if self.settings.get("videos", True):
            self.play_media(node.id, info[0] if info else None,
                            f"{f.title} · {info[1]}" if info else f.title)
        if not self.running:
            return False
        bg = self.assets.background(node.bg, ch.color)
        hp = {"a": 1.0, "b": 1.0}
        n = max(1, len(f.beats))
        beat_i, t_beat = 0, time.time()
        pa = self.assets.portrait(f.a, 380)
        pb = self.assets.portrait(f.b, 380)
        if pb:
            pb = pygame.transform.flip(pb, True, False)
        rng = random.Random(node.id)
        sparks = []

        def hit(i):
            if f.winner == "a":
                hp["b"] = max(0.0, 1 - (i + 1) / n)
                hp["a"] = max(0.25, hp["a"] - 0.12 * rng.random())
            elif f.winner == "b":
                hp["a"] = max(0.0, 1 - (i + 1) / n)
                hp["b"] = max(0.25, hp["b"] - 0.12 * rng.random())
            else:
                hp["a"] = hp["b"] = max(0.3, 1 - (i + 1) / n * 0.7)
            for _ in range(28):
                sparks.append([W / 2, H / 2 - 40, rng.uniform(-9, 9), rng.uniform(-9, 9), 1.0])

        hit(0)
        while self.running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.running = False
                    return False
                if self.handle_global_key(ev):
                    continue
                if (ev.type == pygame.KEYDOWN and ev.key in (pygame.K_SPACE, pygame.K_RETURN)) or \
                        (ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1):
                    beat_i += 1
                    if beat_i >= n:
                        return True
                    t_beat = time.time()
                    hit(beat_i)
                elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                    return True
            dt = time.time() - t_beat
            shake = max(0, 0.35 - dt) * 40
            ox, oy = rng.uniform(-shake, shake), rng.uniform(-shake, shake)
            self.screen.fill((0, 0, 0))
            self.screen.blit(bg, (ox, oy))
            self.dark(120)
            self.stripes(time.time() * 4, color=(255, 255, 255), alpha=14, count=8)
            if pa:
                self.screen.blit(pa, (40 + ox, H - 160 - pa.get_height() + oy))
            if pb:
                self.screen.blit(pb, (W - 40 - pb.get_width() + ox, H - 160 - pb.get_height() + oy))
            if dt < 0.12:
                fl = pygame.Surface((W, H), pygame.SRCALPHA)
                fl.fill((255, 255, 255, int(180 * (1 - dt / 0.12))))
                self.screen.blit(fl, (0, 0))
            for s in sparks:
                s[0] += s[2]; s[1] += s[3]; s[4] -= 0.025
                if s[4] > 0:
                    pygame.draw.circle(self.screen, (255, int(160 + 90 * s[4]), 60), (int(s[0]), int(s[1])), int(5 * s[4]) + 1)
            sparks[:] = [s for s in sparks if s[4] > 0]
            self.italic_text("¡PELEA!", self.f_title, COL["red"], (W // 2, 70), 4, outline=COL["ink"])
            self.text(f.title.upper(), self.f_name, COL["text"], (W // 2, 130), center=True)
            for side, name in (("a", f.a), ("b", f.b)):
                x = 60 if side == "a" else W - 60 - 420
                pygame.draw.polygon(self.screen, (40, 40, 50), slant((x, 170, 420, 26), 10))
                wv = int(416 * hp[side])
                colr = COL["blue"] if side == "a" else COL["red"]
                if wv > 12:
                    pygame.draw.polygon(self.screen, colr, slant((x + 2 if side == "a" else x + 418 - wv, 172, wv, 22), 9))
                self.text(name.upper(), self.f_name, COL["text"], (x if side == "a" else x + 420 - self.f_name.size(name.upper())[0], 200))
            self.panel((W // 2 - 470, H - 190, 940, 140), (10, 12, 24, 230), 6)
            yy = H - 165
            for ln in wrap(f.beats[beat_i], self.f, 880):
                self.text(ln, self.f, COL["text"], (W // 2, yy + 14), center=True)
                yy += 32
            self.text(f"{beat_i + 1}/{n} · clic para continuar", self.f_s, COL["dim"], (W // 2, H - 66), center=True)
            self.draw_toast()
            pygame.display.flip()
            self.clock.tick(FPS)
        return False

    # ---------- fin de capítulo / finales ----------
    def chapter_end_screen(self):
        node = self.game.node
        lines = self.game.visible_lines(node)
        st = self.game.state
        ch = self.game.chapter
        bg = self.assets.background(node.bg, ch.color)
        t0 = time.time()

        def draw():
            self.screen.blit(bg, (0, 0))
            self.dark(170)
            self.stripes(time.time() - t0, alpha=16)
            self.slant_panel((W // 2 - 340, 60, 680, 60), COL["red"] if node.alt_end else COL["accent"], 24)
            self.text((node.end_title or "Fin del capítulo").upper(), self.f_h, COL["ink"], (W // 2, 90), center=True)
            y = 160
            for ln in lines:
                txt = (("" if ln.speaker in (None, "Voz") else ln.speaker + ": ") + ln.text)
                for sub in wrap(txt, self.f, 980):
                    self.text(sub, self.f, COL["text"] if ln.speaker != "Voz" else COL["accent"], (150, y))
                    y += 32
                y += 8
            y = max(y + 20, 470)
            self.slant_panel((150, y, 980, 110), (10, 12, 26, 230), 20)
            self.text(f"Decisiones: {st.decisions}   ·   Canon: {st.canon_taken}   ·   "
                      f"Menores: {st.minors}   ·   Mayores: {len(st.majors)}", self.f_s, COL["text"], (185, y + 18))
            msg = ("El hilo del destino sigue intacto." if st.thread_intact else
                   "El hilo del destino está alterado: el capítulo de X permanecerá sellado.")
            self.text(msg, self.f_s, COL["green"] if st.thread_intact else COL["red"], (185, y + 52))
            self.text("Haz clic para volver a la selección de capítulos", self.f_s, COL["dim"], (W // 2, H - 30), center=True)
        self.wait_click(draw)
        if not self.running:
            return None
        return self.game.finish_chapter()

    def ending_screen(self, key):
        e = self.story.endings[key]
        unlock_ending(key)
        if e.canon:
            self.play_media("fin_E01", medios.OPENING_X, "Opening ver.X · INERTIA")
        self.music.play("fin_x" if e.canon else "fin")
        bg = self.assets.background(e.bg, (30, 30, 50))
        lines = [ln for ln in e.text.strip().splitlines() if ln.strip()]
        t0 = time.time()
        got = len(load_gallery())

        def draw():
            self.screen.blit(bg, (0, 0))
            self.dark(160)
            a = min(255, int((time.time() - t0) * 200))
            col = COL["accent"] if e.canon else COL["red"]
            self.slant_panel((W // 2 - 220, 40, 440, 40), col, 16)
            self.text("FINAL CANÓNICO" if e.canon else f"FINAL ALTERNATIVO · {key}", self.f_name, COL["ink"],
                      (W // 2, 60), center=True)
            self.italic_text(e.title.upper(), self.f_title, COL["text"], (W // 2, 130), 2, outline=COL["ink"])
            y = 200
            for ln in lines:
                for sub in wrap(ln, self.f, 980):
                    self.text(sub, self.f, COL["text"], (150, y), alpha=a)
                    y += 31
                y += 10
            self.text(f"Finales descubiertos: {got}/{len(self.story.endings)}  ·  Haz clic para continuar",
                      self.f_s, COL["dim"], (W // 2, H - 30), center=True)
        self.wait_click(draw)

    def gallery_screen(self):
        got = load_gallery()
        bg = self.assets.background("titulo", (30, 30, 90))
        keys = sorted(self.story.endings)
        t0 = time.time()

        def draw():
            self.screen.blit(bg, (0, 0))
            self.dark(185)
            self.stripes(time.time() - t0, alpha=16)
            self.slant_panel((40, 26, 520, 64), COL["accent"], 26)
            self.text(f"FINALES · {len(got)}/{len(keys)}", self.f_big, COL["ink"], (300, 58), center=True)
            for i, k in enumerate(keys):
                e = self.story.endings[k]
                col_x = 120 if i < 7 else 660
                y = 120 + (i % 7) * 72
                ok = k in got
                self.slant_panel((col_x, y, 500, 60), (20, 22, 40, 230), 18,
                                 (COL["accent"] if e.canon else COL["green"]) if ok else (60, 60, 80))
                self.text(f"{k} · {e.title.upper() if ok else '???'}", self.f_name,
                          (COL["accent"] if e.canon else COL["text"]) if ok else COL["dim"], (col_x + 34, y + 15))
            self.text("Haz clic para volver", self.f_s, COL["dim"], (W // 2, H - 30), center=True)
        self.wait_click(draw)

    def settings_screen(self):
        bg = self.assets.background("titulo", (30, 30, 90))
        while self.running:
            s = self.settings
            onoff = lambda v: "SÍ" if v else "NO"  # noqa: E731
            buttons = [
                Button((W // 2 - 320, 150, 640, 56), f"SOUNDTRACK DEL ANIME: {onoff(s['musica'])}", "musica",
                       color=COL["green"] if s["musica"] else COL["red"]),
                Button((W // 2 - 320, 220, 640, 56), f"VIDEOS DE PELEAS (YouTube oficial): {onoff(s['videos'])}", "videos",
                       color=COL["green"] if s["videos"] else COL["red"]),
                Button((W // 2 - 320, 290, 640, 56), f"OPENING AL INICIAR: {onoff(s['opening'])}", "opening",
                       color=COL["green"] if s["opening"] else COL["red"]),
                Button((W // 2 - 320, 360, 640, 56), f"COLORES DE CANON EN OPCIONES: {onoff(s['pistas'])}", "pistas",
                       color=COL["green"] if s["pistas"] else COL["red"]),
                Button((W // 2 - 320, 430, 300, 56), "VOLUMEN –", "vol-"),
                Button((W // 2 + 20, 430, 300, 56), "VOLUMEN +", "vol+"),
                Button((W // 2 - 130, 560, 260, 52), "VOLVER", "back", color=COL["red"]),
            ]

            def draw():
                self.screen.blit(bg, (0, 0))
                self.dark(185)
                self.italic_text("AJUSTES", self.f_title, COL["accent"], (W // 2, 80), 3, outline=COL["ink"])
                self.text(f"Volumen del soundtrack: {s['volumen']}%", self.f_s, COL["text"], (W // 2, 505), center=True)
                if not webview_ok():
                    self.text("Para los videos y la música de YouTube instala:  python -m pip install pywebview",
                              self.f_s, COL["red"], (W // 2, 530), center=True)
            a = self.menu_loop(draw, buttons, {pygame.K_ESCAPE: "back"})
            if a in (None, "back"):
                return
            if a == "musica":
                self.music.toggle()
                continue
            if a in ("videos", "opening", "pistas"):
                s[a] = not s[a]
            elif a == "vol-":
                s["volumen"] = max(0, s["volumen"] - 10)
            elif a == "vol+":
                s["volumen"] = min(100, s["volumen"] + 10)
            save_settings(s)
            if a in ("vol-", "vol+") and s["musica"]:
                self.music.play(self.music.key, force=True)

    def help_screen(self):
        bg = self.assets.background("titulo", (30, 30, 90))
        lines = [
            "CLIC / ESPACIO / ENTER: avanzar el texto      1-4: elegir una opción",
            "ESC: pausa      M: activar/desactivar el soundtrack      P: colores de canon      H: historial      F11: pantalla completa",
            "",
            "Colores de las respuestas: VERDE = canon · AMARILLO = no afecta del todo al canon · ROJO = modifica el canon.",
            "Mientras no elijas ninguna roja, el hilo del destino sigue intacto y al final se desbloquea el capítulo de X.",
            "",
            "Videos y música: tráileres, 'HERO's Highlight', opening, ending y temas de personajes del canal oficial",
            "de To Be Hero X (tbhx.net). Si pones archivos propios en assets/, el juego los usa primero.",
            "",
            "Basado en el anime To Be Hero X (Li Haoling / bilibili / Aniplex / Fuji TV).",
            "Todos los derechos de la obra original pertenecen a sus autores.",
        ]

        def draw():
            self.screen.blit(bg, (0, 0))
            self.dark(190)
            self.italic_text("CRÉDITOS Y CONTROLES", self.f_title, COL["accent"], (W // 2, 70), 3, outline=COL["ink"])
            self.slant_panel((W // 2 - 400, 118, 800, 92), (0, 0, 0, 190), 22, COL["accent"])
            self.text("CREADO POR", self.f_xs, COL["accent"], (W // 2, 134), center=True)
            self.text("Eduardo Pedroza López", self.f_name, COL["text"], (W // 2, 160), center=True)
            self.text("Rogelio Uriel Gutierrez Jimenez", self.f_name, COL["text"], (W // 2, 190), center=True)
            y = 240
            for ln in lines:
                for sub in wrap(ln, self.f_s, 1080):
                    self.text(sub, self.f_s, COL["text"], (100, y))
                    y += 28
        self.wait_click(draw)

    # ---------- menús ----------
    def pause_menu(self):
        snapshot = self.screen.copy()
        while True:
            buttons = [Button((W // 2 - 190, 190, 380, 52), "CONTINUAR", "resume", color=COL["green"]),
                       Button((W // 2 - 190, 254, 380, 52), "GUARDAR", "save"),
                       Button((W // 2 - 190, 318, 380, 52), "HISTORIAL", "hist"),
                       Button((W // 2 - 190, 382, 380, 52), f"SOUNDTRACK: {'SÍ' if self.music.enabled else 'NO'}", "music"),
                       Button((W // 2 - 190, 446, 380, 52), f"COLORES DE CANON: {'SÍ' if self.hints else 'NO'}", "hints"),
                       Button((W // 2 - 190, 510, 380, 52), "GUARDAR Y SALIR", "quit", color=COL["red"])]

            def draw():
                self.screen.blit(snapshot, (0, 0))
                self.dark(170)
                self.italic_text("PAUSA", self.f_title, COL["accent"], (W // 2, 120), 3, outline=COL["ink"])
            a = self.menu_loop(draw, buttons, {pygame.K_ESCAPE: "resume"})
            if a == "save":
                self.autosave()
                self.show_toast("Partida guardada")
            elif a == "hist":
                self.history_screen()
            elif a == "music":
                self.music.toggle()
            elif a == "hints":
                self.settings["pistas"] = not self.hints
                save_settings(self.settings)
            elif a == "quit" or a is None:
                self.autosave()
                return "quit"
            else:
                return "resume"

    def history_screen(self):
        log = self.game.state.log[-16:]

        def draw():
            self.screen.fill(COL["bg"])
            self.italic_text("ÚLTIMAS DECISIONES", self.f_big, COL["accent"], (W // 2, 50), 2)
            y = 100
            for cap, ask, txt, tag in log:
                label, col = TAGS[tag]
                self.text(f"Cap. {cap} · {ask[:60]}", self.f_s, COL["dim"], (80, y))
                self.text(f"→ {txt[:80]}", self.f_s, COL["text"], (100, y + 18))
                self.text(label, self.f_xs, col, (W - 80, y + 8), right=True)
                y += 38
            if not log:
                self.text("Todavía no has tomado decisiones.", self.f, COL["dim"], (W // 2, 300), center=True)
            self.text("Haz clic para volver", self.f_s, COL["dim"], (W // 2, H - 30), center=True)
        self.wait_click(draw)


def main():
    app = App()
    try:
        app.run()
    finally:
        app.music.shutdown()
