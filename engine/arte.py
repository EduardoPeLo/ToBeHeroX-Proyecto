"""Arte generado por código: retratos estilizados y fondos alegóricos.

Se usa siempre que no exista una imagen real en assets/. Así cada personaje que habla
tiene una imagen y cada escena un fondo acorde al lugar.
"""
from __future__ import annotations

import math
import random
import zlib

import pygame

INK = (12, 10, 18)
SKIN = (238, 204, 176)

# ------------------------------------------------------------------ retratos
# main: color del traje · hair: color de pelo · hs: peinado · em: emblema · extra: detalles
STYLE = {
    "Lin Ling": dict(main=(46, 92, 196), hair=(34, 28, 28), hs="messy", em="mask", extra=["tie"]),
    "Nice": dict(main=(236, 238, 248), hair=(244, 206, 92), hs="neat", em="star", extra=["cape"]),
    "Miss J": dict(main=(170, 28, 60), hair=(20, 20, 24), hs="bob", em="diamond", extra=["glasses"]),
    "Shand": dict(main=(64, 66, 78), hair=(40, 40, 44), hs="slick", em="tree", extra=["tie"]),
    "Moon": dict(main=(54, 54, 132), hair=(18, 18, 30), hs="long", em="moon"),
    "E-Soul": dict(main=(26, 130, 255), hair=(20, 40, 90), hs="spiky", em="bolt", extra=["glow"]),
    "Yang Cheng": dict(main=(26, 130, 255), hair=(30, 30, 40), hs="spiky", em="bolt"),
    "Xia Qing": dict(main=(236, 150, 172), hair=(90, 50, 34), hs="long", em="heart"),
    "Pomelo": dict(main=(250, 190, 60), hair=(60, 40, 30), hs="kid", em="star", kid=True),
    "Shang Chao": dict(main=(120, 90, 60), hair=(150, 150, 150), hs="neat", em="scale", extra=["tie"]),
    "Rock": dict(main=(90, 62, 40), hair=(60, 50, 40), hs="bald", em="zero", extra=["beard"]),
    "Cyan": dict(main=(34, 196, 186), hair=(40, 210, 200), hs="bob", em="note", extra=["phones"]),
    "Luo": dict(main=(84, 76, 108), hair=(30, 26, 40), hs="messy", em="crack"),
    "Liu Zhen": dict(main=(96, 98, 90), hair=(120, 120, 120), hs="neat", em="eye", extra=["glasses"]),
    "Director": dict(main=(108, 58, 90), hair=(70, 60, 60), hs="bald", em="eye"),
    "Mickey": dict(main=(220, 176, 40), hair=(30, 30, 30), hs="slick", em="diamond", extra=["tie"]),
    "Queen": dict(main=(176, 20, 58), hair=(70, 10, 24), hs="long", em="crown", extra=["crown"]),
    "Liu Yuwei": dict(main=(176, 20, 58), hair=(70, 10, 24), hs="long", em="crown"),
    "Bowa": dict(main=(232, 120, 30), hair=(120, 40, 20), hs="spiky", em="fist"),
    "Loli": dict(main=(240, 110, 170), hair=(250, 170, 210), hs="pigtails", em="gear", extra=["mech"]),
    "Luo Li": dict(main=(240, 110, 170), hair=(250, 170, 210), hs="pigtails", em="gear"),
    "Nuonuo": dict(main=(250, 200, 90), hair=(60, 40, 30), hs="bun", em="wrench"),
    "Padre de Loli": dict(main=(120, 140, 160), hair=(90, 90, 90), hs="neat", em="atom", extra=["glasses"]),
    "DJ Shindig": dict(main=(160, 40, 200), hair=(250, 60, 160), hs="mohawk", em="note", extra=["phones"]),
    "Ghostblade": dict(main=(46, 46, 58), hair=(20, 20, 26), hs="hood", em="blade", extra=["maskface"]),
    "Wang Yi": dict(main=(46, 46, 58), hair=(20, 20, 26), hs="messy", em="blade"),
    "Zhang Lan": dict(main=(200, 160, 140), hair=(50, 30, 30), hs="long", em="heart"),
    "Little Johnny": dict(main=(232, 140, 40), hair=(90, 50, 20), hs="spiky", em="paw", kid=True),
    "Big Johnny": dict(kind="monster", main=(112, 80, 170)),
    "Ah Sheng": dict(main=(180, 60, 40), hair=(40, 30, 30), hs="neat", em="flame", extra=["cape"]),
    "Vortex": dict(main=(60, 180, 200), hair=(220, 230, 240), hs="spiky", em="swirl", extra=["cape"]),
    "Zac": dict(main=(60, 200, 120), hair=(30, 30, 30), hs="slick", em="diamond", extra=["tie"]),
    "Dragon Boy": dict(main=(200, 40, 30), hair=(160, 20, 20), hs="spiky", em="dragon", extra=["scales"]),
    "Smile": dict(main=(250, 200, 60), hair=(170, 170, 170), hs="neat", em="smile", extra=["grin", "cape"]),
    "Ahu": dict(kind="dog", main=(212, 152, 92)),
    "Xin Ya": dict(main=(250, 130, 110), hair=(50, 30, 24), hs="ponytail", em="heart"),
    "X": dict(main=(26, 26, 34), hair=(16, 16, 20), hs="short", em="x", extra=["tie", "glasses"]),
    "Voz": dict(kind="shadow", main=(30, 30, 50)),
    "Wreck": dict(main=(120, 30, 30), hair=(30, 30, 30), hs="mohawk", em="fist"),
    "Wolf Girl": dict(main=(120, 110, 140), hair=(200, 200, 210), hs="long", em="paw"),
    "Firm-Man": dict(main=(150, 150, 160), hair=(60, 60, 60), hs="neat", em="shield", extra=["cape"]),
    "God Eye": dict(main=(40, 30, 60), hair=(20, 20, 20), hs="hood", em="eye", extra=["maskface"]),
    "Enlighter": dict(main=(90, 110, 130), hair=(40, 40, 40), hs="neat", em="eye", extra=["glasses"]),
    "Blankster": dict(main=(200, 200, 210), hair=(240, 240, 240), hs="slick", em="circle"),
    "Ex-jefe": dict(main=(70, 70, 80), hair=(40, 40, 40), hs="bald", em="crack", extra=["tie"]),
    "Madre de Dragon Boy": dict(main=(110, 60, 60), hair=(40, 20, 20), hs="bun", em="crack"),
    "Clon": dict(main=(20, 20, 24), hair=(10, 10, 10), hs="hood", em="crack", extra=["maskface"]),
    "Clones": dict(main=(20, 20, 24), hair=(10, 10, 10), hs="hood", em="crack", extra=["maskface"]),
    "Comisión": dict(main=(30, 40, 70), hair=(20, 20, 20), hs="slick", em="scale", extra=["tie", "glasses"]),
    "Comisionado": dict(main=(30, 40, 70), hair=(90, 90, 90), hs="slick", em="scale", extra=["tie"]),
    "Agente": dict(main=(30, 40, 70), hair=(20, 20, 20), hs="short", em="scale", extra=["glasses"]),
}


def _seed(s: str) -> int:
    return zlib.crc32(s.encode("utf-8"))


def style_for(name: str) -> dict:
    if name in STYLE:
        return STYLE[name]
    rng = random.Random(_seed(name))
    main = tuple(rng.randint(60, 220) for _ in range(3))
    return dict(main=main, hair=tuple(rng.randint(10, 90) for _ in range(3)),
                hs=rng.choice(["spiky", "messy", "long", "bob", "ponytail", "short"]),
                em=rng.choice(["circle", "star", "diamond"]))


def _lighter(c, k=0.35):
    return tuple(min(255, int(v + (255 - v) * k)) for v in c)


def _darker(c, k=0.35):
    return tuple(int(v * (1 - k)) for v in c)


def _poly(s, col, pts, w=4):
    pygame.draw.polygon(s, col, pts)
    pygame.draw.polygon(s, INK, pts, w)


def _ell(s, col, rect, w=4):
    pygame.draw.ellipse(s, col, rect)
    pygame.draw.ellipse(s, INK, rect, w)


def emblem(s, kind, cx, cy, r, col):
    pts_star = [(cx + r * math.cos(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else 0.45),
                 cy + r * math.sin(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else 0.45)) for i in range(10)]
    if kind == "bolt":
        _poly(s, col, [(cx + r * .2, cy - r), (cx - r * .6, cy + r * .1), (cx - r * .05, cy + r * .1),
                       (cx - r * .3, cy + r), (cx + r * .6, cy - r * .2), (cx + r * .05, cy - r * .2)], 3)
    elif kind == "crown":
        _poly(s, col, [(cx - r, cy + r * .6), (cx - r, cy - r * .5), (cx - r * .5, cy), (cx, cy - r),
                       (cx + r * .5, cy), (cx + r, cy - r * .5), (cx + r, cy + r * .6)], 3)
    elif kind == "moon":
        pygame.draw.circle(s, col, (cx, cy), r)
        pygame.draw.circle(s, INK, (cx, cy), r, 3)
        pygame.draw.circle(s, _darker(col, .6), (int(cx + r * .45), int(cy - r * .2)), int(r * .8))
    elif kind == "x":
        w = max(4, int(r * .45))
        pygame.draw.line(s, col, (cx - r, cy - r), (cx + r, cy + r), w)
        pygame.draw.line(s, col, (cx + r, cy - r), (cx - r, cy + r), w)
    elif kind == "heart":
        pygame.draw.circle(s, col, (int(cx - r * .45), int(cy - r * .2)), int(r * .55))
        pygame.draw.circle(s, col, (int(cx + r * .45), int(cy - r * .2)), int(r * .55))
        pygame.draw.polygon(s, col, [(cx - r, cy - r * .05), (cx + r, cy - r * .05), (cx, cy + r)])
    elif kind == "note":
        pygame.draw.circle(s, col, (int(cx - r * .3), int(cy + r * .5)), int(r * .35))
        pygame.draw.line(s, col, (cx + r * .02, cy + r * .5), (cx + r * .02, cy - r), max(3, int(r * .2)))
        pygame.draw.line(s, col, (cx + r * .02, cy - r), (cx + r * .6, cy - r * .5), max(3, int(r * .2)))
    elif kind == "gear":
        for i in range(8):
            a = math.radians(i * 45)
            pygame.draw.circle(s, col, (int(cx + r * .85 * math.cos(a)), int(cy + r * .85 * math.sin(a))), int(r * .25))
        pygame.draw.circle(s, col, (cx, cy), int(r * .75))
        pygame.draw.circle(s, INK, (cx, cy), int(r * .3))
    elif kind == "blade":
        _poly(s, col, [(cx - r * .9, cy + r * .9), (cx + r * .8, cy - r), (cx + r, cy - r * .8), (cx - r * .7, cy + r)], 3)
    elif kind == "paw":
        pygame.draw.circle(s, col, (cx, int(cy + r * .3)), int(r * .5))
        for dx, dy in ((-.6, -.3), (-.2, -.7), (.2, -.7), (.6, -.3)):
            pygame.draw.circle(s, col, (int(cx + r * dx), int(cy + r * dy)), int(r * .22))
    elif kind == "dragon":
        for i in range(3):
            pygame.draw.arc(s, col, (cx - r + i * 6, cy - r + i * 6, 2 * r - i * 12, 2 * r - i * 12), 0.3, 4.5, 4)
        pygame.draw.circle(s, col, (int(cx + r * .4), int(cy - r * .6)), int(r * .25))
    elif kind == "smile":
        pygame.draw.circle(s, col, (cx, cy), r)
        pygame.draw.circle(s, INK, (int(cx - r * .35), int(cy - r * .25)), int(r * .12))
        pygame.draw.circle(s, INK, (int(cx + r * .35), int(cy - r * .25)), int(r * .12))
        pygame.draw.arc(s, INK, (cx - r * .6, cy - r * .5, r * 1.2, r * 1.1), 3.5, 5.9, 4)
    elif kind == "eye":
        pygame.draw.ellipse(s, col, (cx - r, cy - r * .5, 2 * r, r))
        pygame.draw.circle(s, INK, (cx, cy), int(r * .35))
    elif kind == "zero":
        pygame.draw.ellipse(s, col, (cx - r * .7, cy - r, r * 1.4, 2 * r), max(4, int(r * .3)))
    elif kind == "flame":
        _poly(s, col, [(cx, cy - r), (cx + r * .7, cy + r * .2), (cx + r * .3, cy + r), (cx - r * .3, cy + r),
                       (cx - r * .7, cy + r * .2), (cx - r * .1, cy - r * .2)], 3)
    elif kind == "swirl":
        for i in range(3):
            pygame.draw.arc(s, col, (cx - r + i * 7, cy - r + i * 7, 2 * r - i * 14, 2 * r - i * 14), i, i + 4, 4)
    elif kind == "tree":
        pygame.draw.circle(s, col, (cx, int(cy - r * .3)), int(r * .7))
        pygame.draw.rect(s, col, (cx - r * .15, cy, r * .3, r))
    elif kind == "mask":
        pygame.draw.ellipse(s, col, (cx - r, cy - r * .45, 2 * r, r * .9))
        pygame.draw.ellipse(s, INK, (cx - r * .7, cy - r * .2, r * .5, r * .3))
        pygame.draw.ellipse(s, INK, (cx + r * .2, cy - r * .2, r * .5, r * .3))
    elif kind == "scale":
        pygame.draw.line(s, col, (cx, cy - r), (cx, cy + r), 4)
        pygame.draw.line(s, col, (cx - r, cy - r * .5), (cx + r, cy - r * .5), 4)
        pygame.draw.arc(s, col, (cx - r * 1.1, cy - r * .5, r * .9, r * .8), 3.14, 6.28, 4)
        pygame.draw.arc(s, col, (cx + r * .2, cy - r * .5, r * .9, r * .8), 3.14, 6.28, 4)
    elif kind == "crack":
        pygame.draw.lines(s, col, False, [(cx - r, cy - r), (cx - r * .2, cy - r * .1), (cx - r * .5, cy + r * .2),
                                          (cx + r * .4, cy + r), (cx + r * .1, cy + r * .1), (cx + r, cy - r * .3)], 4)
    elif kind == "fist":
        pygame.draw.rect(s, col, (cx - r * .8, cy - r * .6, r * 1.6, r * 1.3), border_radius=int(r * .3))
        for i in range(3):
            pygame.draw.line(s, INK, (cx - r * .8 + (i + 1) * r * .4, cy - r * .6), (cx - r * .8 + (i + 1) * r * .4, cy), 3)
    elif kind == "shield":
        _poly(s, col, [(cx - r, cy - r), (cx + r, cy - r), (cx + r * .8, cy + r * .3), (cx, cy + r), (cx - r * .8, cy + r * .3)], 3)
    elif kind == "wrench":
        pygame.draw.line(s, col, (cx - r * .7, cy + r * .7), (cx + r * .4, cy - r * .4), max(4, int(r * .3)))
        pygame.draw.circle(s, col, (int(cx + r * .5), int(cy - r * .5)), int(r * .4), max(3, int(r * .2)))
    elif kind == "atom":
        for a in (0, 60, 120):
            sub = pygame.Surface((2 * r + 4, 2 * r + 4), pygame.SRCALPHA)
            pygame.draw.ellipse(sub, col, (2, r * .65, 2 * r, r * .7), 3)
            sub = pygame.transform.rotate(sub, a)
            s.blit(sub, sub.get_rect(center=(cx, cy)))
        pygame.draw.circle(s, col, (cx, cy), int(r * .2))
    elif kind == "diamond":
        _poly(s, col, [(cx, cy - r), (cx + r * .7, cy), (cx, cy + r), (cx - r * .7, cy)], 3)
    elif kind == "star":
        _poly(s, col, pts_star, 3)
    else:
        pygame.draw.circle(s, col, (cx, cy), r)
        pygame.draw.circle(s, INK, (cx, cy), r, 3)


def _hair_back(s, st, hx, hy, rx, ry):
    hs, hair = st.get("hs", "short"), st.get("hair", (30, 30, 30))
    if hs in ("long", "ponytail"):
        _poly(s, hair, [(hx - rx * 1.15, hy - ry * .2), (hx + rx * 1.15, hy - ry * .2),
                        (hx + rx * 1.3, hy + ry * 2.1), (hx - rx * 1.3, hy + ry * 2.1)])
    if hs == "pigtails":
        _ell(s, hair, (hx - rx * 1.9, hy - ry * .1, rx * .9, ry * 1.6))
        _ell(s, hair, (hx + rx * 1.0, hy - ry * .1, rx * .9, ry * 1.6))
    if hs == "bun":
        _ell(s, hair, (hx - rx * .45, hy - ry * 1.55, rx * .9, ry * .8))
    if hs == "hood":
        _poly(s, st["main"], [(hx - rx * 1.45, hy + ry * 1.4), (hx - rx * 1.3, hy - ry * .7), (hx, hy - ry * 1.5),
                              (hx + rx * 1.3, hy - ry * .7), (hx + rx * 1.45, hy + ry * 1.4)])


def _hair_front(s, st, hx, hy, rx, ry, rng):
    hs, hair = st.get("hs", "short"), st.get("hair", (30, 30, 30))
    top = hy - ry
    if hs in ("bald", "hood"):
        return
    if hs == "spiky":
        pts = [(hx - rx * 1.05, hy - ry * .1)]
        for i in range(7):
            x = hx - rx + i * rx * 2 / 6
            pts.append((x + rx * .1, top - ry * (.45 + rng.random() * .4)))
            pts.append((x + rx * .25, top + ry * .25))
        pts.append((hx + rx * 1.05, hy - ry * .1))
        _poly(s, hair, pts)
    elif hs == "mohawk":
        _poly(s, hair, [(hx - rx * .25, top + ry * .2), (hx - rx * .1, top - ry * .9), (hx + rx * .15, top - ry * .9),
                        (hx + rx * .25, top + ry * .2)])
    elif hs == "messy":
        pts = [(hx - rx * 1.08, hy)]
        for i in range(9):
            a = math.pi + i * math.pi / 8
            rr = 1.12 + rng.random() * .22
            pts.append((hx + rx * rr * math.cos(a), hy - ry * .1 + ry * rr * math.sin(a)))
        pts.append((hx + rx * 1.08, hy))
        pts.append((hx + rx * .2, hy - ry * .45))
        pts.append((hx - rx * .4, hy - ry * .3))
        _poly(s, hair, pts)
    elif hs == "bob":
        _poly(s, hair, [(hx - rx * 1.15, hy + ry * .7), (hx - rx * 1.15, hy - ry * .5), (hx - rx * .6, top - ry * .2),
                        (hx + rx * .6, top - ry * .2), (hx + rx * 1.15, hy - ry * .5), (hx + rx * 1.15, hy + ry * .7),
                        (hx + rx * .85, hy + ry * .7), (hx + rx * .8, hy - ry * .35), (hx - rx * .8, hy - ry * .35),
                        (hx - rx * .85, hy + ry * .7)])
    elif hs == "slick":
        _poly(s, hair, [(hx - rx * 1.05, hy - ry * .1), (hx - rx * .9, top - ry * .1), (hx + rx * .3, top - ry * .25),
                        (hx + rx * 1.05, top + ry * .2), (hx + rx * 1.05, hy - ry * .3), (hx - rx * .5, hy - ry * .5)])
    elif hs == "neat":
        _poly(s, hair, [(hx - rx * 1.06, hy - ry * .05), (hx - rx * .95, top - ry * .1), (hx + rx * .95, top - ry * .1),
                        (hx + rx * 1.06, hy - ry * .05), (hx + rx * .9, hy - ry * .4), (hx - rx * .2, hy - ry * .55),
                        (hx - rx * .9, hy - ry * .4)])
    else:  # short, long, ponytail, pigtails, bun, kid
        _poly(s, hair, [(hx - rx * 1.08, hy + ry * .1), (hx - rx * .9, top - ry * .15), (hx + rx * .9, top - ry * .15),
                        (hx + rx * 1.08, hy + ry * .1), (hx + rx * .85, hy - ry * .45), (hx + rx * .2, hy - ry * .35),
                        (hx - rx * .3, hy - ry * .55), (hx - rx * .85, hy - ry * .4)])


ANIME_HAIR = ["shonen", "flequillo", "largo", "coleta", "corto", "rebelde"]
SIL_STYLE = {
    "Voz": "flequillo", "Niño": "rebelde", "Huérfano": "corto", "Fan": "coleta", "Zac": "corto",
    "Madre de Dragon Boy": "largo", "Clon": "capucha", "Clones": "capucha", "Agente": "corto",
    "Comisionado": "corto", "Comisión": "corto", "Periodista": "flequillo", "Ah Sheng": "shonen",
    "Secuestrador": "rebelde", "Secuestradores": "rebelde", "Cirquero": "rebelde", "Científico": "flequillo",
}


def _anime_shape(name: str, w: int, h: int) -> pygame.Surface:
    """Dibuja (en blanco) la forma de un personaje anime: cabeza con barbilla en punta y pelo con mechones."""
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    rng = random.Random(_seed(name + "anime"))
    st = SIL_STYLE.get(name) or rng.choice(ANIME_HAIR)
    if style_for(name).get("kind") == "dog":
        return portrait(name, h, aura=False)
    C = (255, 255, 255, 255)
    cx, rx = w * .5, w * .17
    top, chin = h * .25, h * .53
    poly = lambda pts: pygame.draw.polygon(s, C, [(int(x), int(y)) for x, y in pts])  # noqa: E731
    # pelo largo por detrás
    if st in ("largo",):
        pts = [(cx - rx * 1.25, h * .32)]
        for i in range(9):
            x = cx - rx * 1.35 + i * rx * 2.7 / 8
            pts.append((x + rng.uniform(-6, 6), h * (.74 + rng.uniform(-.04, .05))))
        pts.append((cx + rx * 1.25, h * .32))
        poly(pts)
    if st == "coleta":
        poly([(cx + rx * .6, h * .27), (cx + rx * 2.1, h * .33), (cx + rx * 2.5, h * .55),
              (cx + rx * 1.7, h * .5), (cx + rx * .9, h * .38)])
    # hombros y cuello
    poly([(w * .02, h), (w * .1, h * .74), (w * .26, h * .655), (cx - w * .06, h * .64), (cx, h * .68),
          (cx + w * .06, h * .64), (w * .74, h * .655), (w * .9, h * .74), (w * .98, h)])
    pygame.draw.rect(s, C, (cx - w * .055, h * .48, w * .11, h * .18))
    # cara: barbilla en punta
    pygame.draw.ellipse(s, C, (cx - rx, top, rx * 2, (chin - top) * 1.15))
    poly([(cx - rx, h * .37), (cx - rx * .8, h * .47), (cx, chin), (cx + rx * .8, h * .47), (cx + rx, h * .37)])
    if st == "capucha":
        poly([(cx - rx * 1.5, h * .66), (cx - rx * 1.45, h * .3), (cx - rx * .6, h * .17), (cx + rx * .6, h * .17),
              (cx + rx * 1.45, h * .3), (cx + rx * 1.5, h * .66)])
        return s
    # casquete de pelo
    pygame.draw.ellipse(s, C, (cx - rx * 1.18, top - h * .045, rx * 2.36, h * .2))
    # flequillo: mechones en punta sobre la frente
    n = rng.randint(5, 7)
    for i in range(n):
        x0 = cx - rx * 1.1 + i * rx * 2.2 / n
        x1 = x0 + rx * 2.2 / n
        tip = (x0 + x1) / 2 + rng.uniform(-8, 8)
        long_ = h * (.36 + rng.uniform(0, .06)) if st != "corto" else h * (.31 + rng.uniform(0, .03))
        poly([(x0 - 3, h * .27), (x1 + 3, h * .27), (tip, long_)])
    # mechones laterales
    for side in (-1, 1):
        x = cx + side * rx * 1.05
        poly([(x - 9, h * .3), (x + 9, h * .3), (x + side * rng.uniform(2, 10), h * (.46 + rng.uniform(0, .06)))])
    if st in ("shonen", "rebelde"):
        k = 7 if st == "shonen" else 5
        for i in range(k):
            a = math.radians(200 + i * (140 / (k - 1)) + rng.uniform(-6, 6))
            L = rx * (1.25 + rng.uniform(.2, .7))
            bx, by = cx + math.cos(a) * rx * .8, top + h * .06 + math.sin(a) * rx * .5
            poly([(bx + math.cos(a + 1.4) * 16, by + math.sin(a + 1.4) * 16),
                  (bx + math.cos(a) * L, by + math.sin(a) * L),
                  (bx + math.cos(a - 1.4) * 16, by + math.sin(a - 1.4) * 16)])
    # 'ahoge': el mechón rebelde típico del anime
    if st != "corto":
        pts = [(cx + rx * .1, top), (cx + rx * .35, top - h * .07), (cx + rx * .7, top - h * .08),
               (cx + rx * .4, top - h * .055), (cx + rx * .25, top + 2)]
        poly(pts)
    return s


def silhouette(name: str, h: int) -> pygame.Surface:
    """Personaje 'por desbloquear': silueta negra estilo anime con brillo de contorno."""
    w = int(h * .72)
    shape = _anime_shape(name, w, h)
    m = pygame.mask.from_surface(shape, 20)
    accent = _lighter(style_for(name)["main"], .35)
    out = pygame.Surface((w, h), pygame.SRCALPHA)
    rim = m.to_surface(setcolor=(*accent, 255), unsetcolor=(0, 0, 0, 0))
    glow = pygame.transform.gaussian_blur(rim, 8)
    out.blit(glow, (0, 0))
    out.blit(glow, (0, 0))
    sil = m.to_surface(setcolor=(14, 14, 22, 255), unsetcolor=(0, 0, 0, 0))
    grad = pygame.Surface((w, h), pygame.SRCALPHA)
    for y in range(h):
        c = int(46 - 34 * y / h)
        grad.fill((c, c, c + 10, 255), (0, y, w, 1))
    grad.blit(sil, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    out.blit(grad, (0, 0))
    pts = m.outline(2)
    if len(pts) > 2:
        pygame.draw.lines(out, (*accent, 255), True, pts, 2)
    if name == "Voz":
        f = pygame.font.SysFont("bahnschrift,arialblack", int(h * .16), bold=True)
        q = f.render("?", True, accent)
        out.blit(q, q.get_rect(center=(w // 2, int(h * .8))))
    return out


def portrait(name: str, h: int, aura: bool = True) -> pygame.Surface:
    st = style_for(name)
    w = int(h * .72)
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    rng = random.Random(_seed(name))
    main = st["main"]
    accent = _lighter(main, .45)
    # aura con líneas de velocidad (estilo cómic)
    glow = pygame.Surface((w, h), pygame.SRCALPHA)
    for i in range(18):
        a = rng.random() * math.tau
        pygame.draw.line(glow, (*accent, 40), (w / 2, h * .45),
                         (w / 2 + math.cos(a) * w, h * .45 + math.sin(a) * h), rng.randint(2, 9))
    pygame.draw.circle(glow, (*accent, 55), (w // 2, int(h * .45)), int(w * .46))
    if aura:
        s.blit(glow, (0, 0))
    kind = st.get("kind")
    if kind == "dog":
        _dog(s, w, h, main)
        return s
    if kind == "monster":
        _monster(s, w, h, main, rng)
        return s
    kid = st.get("kid", False)
    sc = .86 if kid else 1.0
    hx, hy = w / 2, h * (.40 if not kid else .47)
    rx, ry = w * .2 * sc, h * .155 * sc
    extra = st.get("extra", [])
    shadow = kind == "shadow"
    if shadow:
        main = (20, 20, 34)
    _hair_back(s, st, hx, hy, rx, ry)
    if "cape" in extra:
        _poly(s, _darker(main, .45), [(w * .02, h), (w * .12, h * .66), (w * .88, h * .66), (w * .98, h)])
    # hombros / torso
    sy = h * (.70 if not kid else .76)
    body = [(w * .04, h + 4), (w * .12, sy + h * .05), (w * .3, sy - h * .02), (w * .7, sy - h * .02),
            (w * .88, sy + h * .05), (w * .96, h + 4)]
    if "mech" in extra:
        _poly(s, (200, 205, 220), body)
        _ell(s, main, (w * .06, sy - h * .02, w * .26, h * .14))
        _ell(s, main, (w * .68, sy - h * .02, w * .26, h * .14))
    else:
        _poly(s, main, body)
    if "scales" in extra:
        for i in range(14):
            x, y = rng.uniform(w * .15, w * .85), rng.uniform(sy + 10, h - 10)
            pygame.draw.arc(s, _darker(main, .5), (x, y, 26, 18), 3.3, 6.1, 3)
    skin = (50, 46, 70) if shadow else SKIN
    pygame.draw.rect(s, skin, (hx - rx * .38, hy + ry * .7, rx * .76, ry * .9))
    pygame.draw.rect(s, INK, (hx - rx * .38, hy + ry * .7, rx * .76, ry * .9), 3)
    if "tie" in extra and not shadow:
        _poly(s, (245, 245, 250), [(hx - rx * .7, sy - h * .02), (hx + rx * .7, sy - h * .02), (hx, sy + h * .12)], 3)
        _poly(s, (160, 20, 30) if name != "X" else (40, 40, 60),
              [(hx - rx * .14, sy), (hx + rx * .14, sy), (hx + rx * .22, sy + h * .16), (hx, sy + h * .21),
               (hx - rx * .22, sy + h * .16)], 3)
    # cabeza
    _ell(s, skin, (hx - rx, hy - ry, rx * 2, ry * 2))
    _hair_front(s, st, hx, hy, rx, ry, rng)
    if "crown" in extra:
        _poly(s, (250, 200, 60), [(hx - rx * .7, hy - ry * .85), (hx - rx * .75, hy - ry * 1.55), (hx - rx * .35, hy - ry * 1.15),
                                  (hx, hy - ry * 1.7), (hx + rx * .35, hy - ry * 1.15), (hx + rx * .75, hy - ry * 1.55),
                                  (hx + rx * .7, hy - ry * .85)], 3)
    if "phones" in extra:
        pygame.draw.arc(s, INK, (hx - rx * 1.2, hy - ry * 1.25, rx * 2.4, ry * 2.2), 0.2, 2.94, 7)
        _ell(s, accent, (hx - rx * 1.3, hy - ry * .3, rx * .5, ry * .75))
        _ell(s, accent, (hx + rx * .8, hy - ry * .3, rx * .5, ry * .75))
    # cara
    ey = hy + ry * .05
    if shadow:
        pygame.draw.circle(s, (255, 200, 80), (int(hx - rx * .38), int(ey)), int(rx * .12))
        pygame.draw.circle(s, (255, 200, 80), (int(hx + rx * .38), int(ey)), int(rx * .12))
        f = pygame.font.SysFont("bahnschrift,arialblack", int(ry * 1.4), bold=True)
        q = f.render("?", True, (255, 200, 80))
        s.blit(q, q.get_rect(center=(hx, sy + h * .12)))
        return s
    eye_col = accent if "glow" in extra else INK
    for dx in (-.38, .38):
        pygame.draw.ellipse(s, eye_col, (hx + rx * dx - rx * .13, ey - ry * .12, rx * .26, ry * .26))
        pygame.draw.line(s, INK, (hx + rx * dx - rx * .2, ey - ry * .28), (hx + rx * dx + rx * .2, ey - ry * .3), 4)
    if "glasses" in extra:
        for dx in (-.38, .38):
            pygame.draw.circle(s, INK, (int(hx + rx * dx), int(ey)), int(rx * .27), 3)
        pygame.draw.line(s, INK, (hx - rx * .12, ey), (hx + rx * .12, ey), 3)
    if "maskface" in extra:
        _poly(s, _darker(main, .2), [(hx - rx * 1.0, hy + ry * .2), (hx + rx * 1.0, hy + ry * .2),
                                     (hx + rx * .8, hy + ry * .9), (hx, hy + ry * 1.05), (hx - rx * .8, hy + ry * .9)], 3)
    elif "grin" in extra:
        pygame.draw.arc(s, INK, (hx - rx * .55, hy + ry * .05, rx * 1.1, ry * .8), 3.4, 6.0, 5)
    else:
        pygame.draw.line(s, INK, (hx - rx * .22, hy + ry * .55), (hx + rx * .22, hy + ry * .52), 4)
    if "beard" in extra:
        _poly(s, st["hair"], [(hx - rx * .9, hy + ry * .3), (hx + rx * .9, hy + ry * .3), (hx + rx * .5, hy + ry * 1.1),
                              (hx - rx * .5, hy + ry * 1.1)], 3)
    emblem(s, st.get("em", "circle"), int(w / 2), int(sy + (h - sy) * .5), int(w * .085), accent)
    return s


def _dog(s, w, h, main):
    hx, hy = w / 2, h * .46
    light = _lighter(main, .3)
    _poly(s, main, [(w * .06, h + 4), (w * .2, h * .74), (w * .8, h * .74), (w * .94, h + 4)])
    for i in range(4):
        pygame.draw.arc(s, _darker(main, .35), (w * .2, h * .76 + i * 22, w * .6, 40), 3.4, 6.0, 4)
    _ell(s, main, (hx - w * .3, hy - h * .2, w * .6, h * .4))
    _ell(s, _darker(main, .25), (hx - w * .38, hy - h * .2, w * .18, h * .24))
    _ell(s, _darker(main, .25), (hx + w * .2, hy - h * .2, w * .18, h * .24))
    for i in range(3):
        pygame.draw.arc(s, _darker(main, .4), (hx - w * .18, hy - h * .17 + i * 14, w * .36, 30), .3, 2.8, 3)
    _ell(s, light, (hx - w * .17, hy + h * .02, w * .34, h * .15))
    pygame.draw.ellipse(s, INK, (hx - w * .06, hy + h * .03, w * .12, h * .05))
    pygame.draw.ellipse(s, INK, (hx - w * .14, hy - h * .05, w * .05, h * .035))
    pygame.draw.ellipse(s, INK, (hx + w * .09, hy - h * .05, w * .05, h * .035))
    emblem(s, "paw", int(hx), int(h * .88), int(w * .07), light)


def _monster(s, w, h, main, rng):
    cx, cy = w / 2, h * .55
    pts = []
    for i in range(28):
        a = i / 28 * math.tau
        r = w * (.42 if i % 2 == 0 else .34)
        pts.append((cx + r * math.cos(a), cy + r * 1.15 * math.sin(a)))
    _poly(s, main, pts)
    for dx in (-.15, .15):
        _ell(s, (250, 250, 240), (cx + w * dx - w * .1, cy - h * .12, w * .2, w * .22))
        pygame.draw.circle(s, INK, (int(cx + w * dx), int(cy - h * .12 + w * .12)), int(w * .06))
    pygame.draw.arc(s, INK, (cx - w * .14, cy + h * .02, w * .28, h * .08), 3.4, 6.0, 4)
    for dx in (-.25, .25):
        _poly(s, _lighter(main, .4), [(cx + w * dx - 14, cy - h * .25), (cx + w * dx * 1.4, cy - h * .38), (cx + w * dx + 14, cy - h * .25)], 3)


# ------------------------------------------------------------------ fondos
THEMES = [
    ("fuera_del_tiempo", "vacio"), ("tablero", "vacio"), ("cero", "vacio"),
    ("azotea", "azotea"), ("callejon", "calle"), ("calle", "calle"), ("ciudad", "ciudad"),
    ("estadio", "estadio"), ("arena", "estadio"), ("torneo", "estadio"), ("ceremonia", "estadio"),
    ("graduacion", "escenario"), ("teatro", "escenario"), ("set_tv", "escenario"), ("concierto", "escenario"),
    ("estudio", "escenario"), ("audicion", "escenario"), ("plaza", "plaza"), ("estatua", "plaza"),
    ("ovni", "ovni"), ("avion", "montana"), ("montana", "montana"), ("bosque", "bosque"),
    ("campamento", "bosque"), ("campo", "campo"), ("aldea", "campo"), ("pueblo", "mar"), ("mar", "mar"),
    ("puerto", "puerto"), ("lab", "laboratorio"), ("hospital", "hospital"), ("circo", "circo"),
    ("noticias", "noticias"), ("redes", "noticias"), ("carretera", "carretera"), ("autopista", "carretera"),
    ("barrio", "plaza"), ("orfanato_zombi", "ruinas"), ("ruinas", "ruinas"), ("miedo", "ruinas"),
    ("oscura", "ruinas"), ("dragon", "ruinas"), ("accidente", "ruinas"), ("destruida", "ruinas"),
    ("entrenamiento", "gimnasio"), ("fin_", "ciudad"), ("titulo", "ciudad"),
]


def theme_for(key: str) -> str:
    k = (key or "").lower()
    for word, theme in THEMES:
        if word in k:
            return theme
    return "interior"


def _grad(s, top, bot, y0=0, y1=None):
    w = s.get_width()
    y1 = y1 or s.get_height()
    for y in range(y0, y1):
        t = (y - y0) / max(1, y1 - y0)
        s.fill(tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)), (0, y, w, 1))


def _skyline(s, rng, base, col, lit=(255, 214, 120), dens=1.0, hmin=80, hmax=300):
    w = s.get_width()
    x = -20
    while x < w:
        bw = rng.randint(40, 110)
        bh = rng.randint(hmin, hmax)
        pygame.draw.rect(s, col, (x, base - bh, bw, bh + 400))
        if rng.random() < .3:
            pygame.draw.rect(s, col, (x + bw * .4, base - bh - rng.randint(10, 50), 4, 60))
        if lit:
            for wy in range(base - bh + 10, base - 6, 16):
                for wx in range(x + 6, x + bw - 8, 13):
                    if rng.random() < .28 * dens:
                        pygame.draw.rect(s, lit, (wx, wy, 6, 8))
        x += bw + rng.randint(-6, 8)


def _stars(s, rng, n=120, ymax=None):
    w, h = s.get_size()
    for _ in range(n):
        c = rng.randint(140, 255)
        s.set_at((rng.randint(0, w - 1), rng.randint(0, (ymax or h // 2))), (c, c, c))


def _rain(s, rng, n=500):
    w, h = s.get_size()
    lay = pygame.Surface((w, h), pygame.SRCALPHA)
    for _ in range(n):
        x, y = rng.randint(0, w), rng.randint(0, h)
        pygame.draw.line(lay, (180, 200, 255, 70), (x, y), (x - 6, y + 22), 1)
    s.blit(lay, (0, 0))


def _vignette(s):
    w, h = s.get_size()
    v = pygame.Surface((w, h), pygame.SRCALPHA)
    for i in range(14):
        a = int(10 + i * 7)
        pygame.draw.rect(v, (0, 0, 0, a), (-i * 30, -i * 22, w + i * 60, h + i * 44), 40)
    s.blit(v, (0, 0))


def _trust(s, rng, n=10, col=(120, 220, 255)):
    f = pygame.font.SysFont("bahnschrift,consolas", 22, bold=True)
    w, h = s.get_size()
    for _ in range(n):
        val = rng.choice(["+", "+", "-"]) + f"{rng.randint(10, 99999):,}"
        t = f.render(val, True, col if val[0] == "+" else (255, 90, 90))
        t.set_alpha(rng.randint(50, 130))
        s.blit(t, (rng.randint(0, w - 120), rng.randint(0, h // 2)))


def background(key: str, size, tint=(40, 40, 60)) -> pygame.Surface:
    w, h = size
    s = pygame.Surface(size)
    rng = random.Random(_seed(key or "x"))
    th = theme_for(key)
    k = (key or "").lower()
    night = any(t in k for t in ("noche", "lluvia", "oscura", "miedo")) or th in ("azotea", "calle", "puerto")
    if th in ("ciudad", "azotea", "calle", "plaza", "noticias"):
        if night or th == "calle":
            _grad(s, (8, 10, 30), _darker(tint, .2))
        else:
            _grad(s, (40, 80, 150), (240, 170, 120))
        _stars(s, rng, 80 if night else 0)
        if night:
            pygame.draw.circle(s, (240, 240, 220), (int(w * .82), int(h * .18)), 46)
        _skyline(s, rng, int(h * .78), _darker(tint, .65), hmax=380)
        _skyline(s, rng, int(h * .92), (14, 14, 22), hmin=60, hmax=260)
        if th == "azotea":
            pygame.draw.rect(s, (24, 24, 32), (0, int(h * .82), w, h))
            for x in range(0, w, 40):
                pygame.draw.line(s, (70, 70, 90), (x, int(h * .74)), (x, int(h * .82)), 4)
            pygame.draw.line(s, (90, 90, 110), (0, int(h * .74)), (w, int(h * .74)), 6)
        if th == "calle":
            pygame.draw.polygon(s, (26, 26, 34), [(0, h), (w * .4, h * .62), (w * .6, h * .62), (w, h)])
            for i in range(6):
                y = h * .64 + i * i * 8
                pygame.draw.line(s, (200, 190, 120), (w / 2, y), (w / 2, y + 10 + i * 3), 3 + i)
            for side in (0, 1):
                for i in range(4):
                    x = w * (.06 + i * .1) if side == 0 else w * (.94 - i * .1)
                    pygame.draw.line(s, (40, 40, 50), (x, h * .95 - i * 30), (x, h * .5 - i * 10), 5)
                    pygame.draw.circle(s, (255, 220, 140), (int(x), int(h * .5 - i * 10)), 9)
        if th == "plaza":
            pygame.draw.rect(s, (40, 38, 50), (0, int(h * .86), w, h))
            if "estatua" in k:
                _poly(s, (130, 130, 140), [(w * .45, h * .86), (w * .47, h * .3), (w * .53, h * .3), (w * .55, h * .86)], 3)
                pygame.draw.circle(s, (130, 130, 140), (w // 2, int(h * .25)), 34)
        if th == "noticias":
            pygame.draw.rect(s, (10, 10, 20), (w * .18, h * .12, w * .64, h * .52))
            pygame.draw.rect(s, (30, 120, 255), (w * .18, h * .12, w * .64, h * .52), 6)
            pygame.draw.rect(s, (200, 30, 40), (w * .18, h * .54, w * .64, h * .1))
            f = pygame.font.SysFont("bahnschrift,arialblack", 54, bold=True)
            t = f.render("ÚLTIMA HORA", True, (255, 255, 255))
            s.blit(t, t.get_rect(center=(w / 2, h * .59)))
            _trust(s, rng, 14)
        if "lluvia" in k or th == "calle":
            _rain(s, rng)
    elif th == "estadio":
        _grad(s, (6, 6, 20), _darker(tint, .3))
        pygame.draw.polygon(s, (24, 24, 36), [(0, h * .3), (w, h * .3), (w, h * .7), (0, h * .7)])
        for row in range(10):
            y = h * .32 + row * 18
            for x in range(0, w, 7):
                if rng.random() < .7:
                    c = rng.choice([(255, 200, 60), (90, 160, 255), (240, 80, 90), (230, 230, 240)])
                    s.set_at((x, int(y + rng.randint(0, 8))), c)
        pygame.draw.polygon(s, _darker(tint, .2), [(0, h), (w * .1, h * .7), (w * .9, h * .7), (w, h)])
        for lx in (w * .1, w * .9):
            cone = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.polygon(cone, (255, 255, 220, 30), [(lx, 0), (w / 2 - 300, h), (w / 2 + 300, h)])
            s.blit(cone, (0, 0))
            pygame.draw.circle(s, (255, 255, 230), (int(lx), 10), 28)
        _trust(s, rng, 8)
    elif th == "escenario":
        _grad(s, (20, 6, 14), (60, 14, 30))
        for i in range(12):
            x = i * w / 12
            pygame.draw.rect(s, (150 - i % 2 * 30, 18, 34), (x, 0, w / 24 + 10, h * .8))
        pygame.draw.rect(s, (80, 50, 30), (0, int(h * .78), w, h))
        for lx in (w * .3, w * .7):
            cone = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.polygon(cone, (255, 240, 200, 50), [(lx, 0), (lx - 180, h * .85), (lx + 180, h * .85)])
            s.blit(cone, (0, 0))
    elif th == "vacio":
        _grad(s, (10, 4, 30), (40, 12, 70))
        _stars(s, rng, 220, h)
        for i in range(-12, 13):
            pygame.draw.line(s, (120, 80, 200), (w / 2 + i * 30, h * .55), (w / 2 + i * 180, h), 1)
        for j in range(8):
            y = h * .55 + (j ** 1.6) * 9
            pygame.draw.line(s, (120, 80, 200), (0, y), (w, y), 1)
        for _ in range(7):
            cx, cy, r = rng.randint(80, w - 80), rng.randint(60, int(h * .5)), rng.randint(20, 60)
            pygame.draw.circle(s, (230, 210, 255), (cx, cy), r, 3)
            a1, a2 = rng.random() * math.tau, rng.random() * math.tau
            pygame.draw.line(s, (230, 210, 255), (cx, cy), (cx + r * .7 * math.cos(a1), cy + r * .7 * math.sin(a1)), 3)
            pygame.draw.line(s, (230, 210, 255), (cx, cy), (cx + r * .45 * math.cos(a2), cy + r * .45 * math.sin(a2)), 3)
        cols = [(255, 196, 64), (90, 170, 255), (240, 80, 90), (110, 220, 140), (240, 110, 170), (40, 200, 190)]
        for i in range(10):
            pts = [(x, h * .3 + math.sin(x / 120 + i) * 80 + i * 22) for x in range(0, w + 40, 40)]
            pygame.draw.lines(s, cols[i % len(cols)], False, pts, 2)
    elif th == "ovni":
        _grad(s, (6, 16, 20), (10, 40, 50))
        for y in range(0, h, 52):
            for x in range(0, w, 60):
                ox = 30 if (y // 52) % 2 else 0
                pts = [(x + ox + 30 * math.cos(math.radians(a)), y + 30 * math.sin(math.radians(a))) for a in range(30, 390, 60)]
                pygame.draw.polygon(s, (30, 110, 120), pts, 1)
        pygame.draw.circle(s, (90, 255, 220), (w // 2, int(h * .45)), 150, 4)
        g = pygame.Surface((w, h), pygame.SRCALPHA)
        pygame.draw.circle(g, (90, 255, 220, 40), (w // 2, int(h * .45)), 140)
        s.blit(g, (0, 0))
        if "ruinas" in k:
            for _ in range(20):
                x, y = rng.randint(0, w), rng.randint(int(h * .5), h)
                pygame.draw.polygon(s, (20, 30, 34), [(x, y), (x + rng.randint(30, 120), y - rng.randint(20, 120)), (x + 140, y)])
    elif th in ("montana", "carretera", "bosque", "campo"):
        if th == "campo" and not night:
            _grad(s, (110, 170, 230), (250, 220, 170))
        else:
            _grad(s, (8, 12, 26), _darker(tint, .3))
            _stars(s, rng, 120)
        for layer, col in enumerate([(40, 50, 70), (26, 34, 48), (14, 20, 30)]):
            pts = [(0, h)]
            for x in range(0, w + 60, 60):
                pts.append((x, h * (.45 + layer * .1) - rng.randint(0, 140)))
            pts.append((w, h))
            pygame.draw.polygon(s, col if th != "campo" or night else _lighter(col, .4), pts)
        if th == "bosque":
            for _ in range(40):
                x, y = rng.randint(-20, w), rng.randint(int(h * .55), h)
                th_ = rng.randint(120, 300)
                pygame.draw.polygon(s, (10, 18, 16), [(x, y), (x + 40, y - th_), (x + 80, y)])
            for _ in range(30):
                pygame.draw.circle(s, (200, 255, 140), (rng.randint(0, w), rng.randint(int(h * .4), h)), 2)
            if "campamento" in k:
                pygame.draw.polygon(s, (200, 90, 40), [(w * .45, h * .92), (w * .5, h * .72), (w * .58, h * .92)])
                g = pygame.Surface((w, h), pygame.SRCALPHA)
                pygame.draw.circle(g, (255, 160, 60, 50), (int(w * .5), int(h * .9)), 160)
                s.blit(g, (0, 0))
        if th == "carretera":
            pygame.draw.polygon(s, (30, 30, 36), [(w * .1, h), (w * .48, h * .58), (w * .52, h * .58), (w * .9, h)])
            for i in range(7):
                y = h * .6 + i * i * 7
                pygame.draw.line(s, (240, 220, 120), (w / 2, y), (w / 2, y + 8 + i * 2), 2 + i)
        if th == "montana":
            for _ in range(12):
                x, y = rng.randint(int(w * .2), int(w * .8)), rng.randint(int(h * .65), int(h * .9))
                pygame.draw.polygon(s, (60, 60, 70), [(x, y), (x + rng.randint(40, 140), y - rng.randint(10, 60)), (x + 160, y + 10)])
            smoke = pygame.Surface((w, h), pygame.SRCALPHA)
            for i in range(14):
                pygame.draw.circle(smoke, (120, 120, 130, 40), (int(w * .5 + i * 6), int(h * .7 - i * 30)), 40 + i * 6)
            s.blit(smoke, (0, 0))
        if th == "campo":
            pygame.draw.rect(s, (60, 110, 50) if not night else (16, 30, 20), (0, int(h * .8), w, h))
            pygame.draw.polygon(s, (120, 70, 50), [(w * .62, h * .8), (w * .62, h * .62), (w * .7, h * .52), (w * .78, h * .62), (w * .78, h * .8)])
    elif th in ("mar", "puerto"):
        _grad(s, (30, 30, 80) if night else (250, 140, 90), (250, 120, 90) if not night else (20, 30, 60), 0, int(h * .6))
        _grad(s, (20, 50, 90), (6, 14, 30), int(h * .6), h)
        for _ in range(60):
            x, y = rng.randint(0, w), rng.randint(int(h * .6), h)
            pygame.draw.line(s, (120, 160, 220), (x, y), (x + rng.randint(10, 50), y), 1)
        if th == "mar":
            for i in range(6):
                x = w * .05 + i * 70
                pygame.draw.rect(s, (230, 220, 200), (x, h * .5, 60, 60))
                pygame.draw.polygon(s, (190, 70, 50), [(x - 6, h * .5), (x + 30, h * .42), (x + 66, h * .5)])
        else:
            for i in range(14):
                c = rng.choice([(200, 60, 40), (40, 120, 200), (60, 160, 80), (220, 170, 40)])
                x = w * .45 + (i % 7) * 90
                y = h * .6 - (i // 7 + 1) * 46
                pygame.draw.rect(s, c, (x, y, 86, 44))
                pygame.draw.rect(s, INK, (x, y, 86, 44), 2)
            pygame.draw.line(s, (220, 180, 40), (w * .2, h * .6), (w * .2, h * .1), 10)
            pygame.draw.line(s, (220, 180, 40), (w * .2, h * .12), (w * .5, h * .12), 8)
    elif th == "ruinas":
        _grad(s, (30, 4, 10), (8, 4, 6))
        _skyline(s, rng, int(h * .9), (20, 8, 12), lit=None, hmax=340)
        for _ in range(26):
            x, y = rng.randint(0, w), rng.randint(int(h * .6), h)
            pygame.draw.polygon(s, (16, 10, 12), [(x, y), (x + rng.randint(20, 90), y - rng.randint(20, 120)), (x + 110, y)])
        fog = pygame.Surface((w, h), pygame.SRCALPHA)
        for _ in range(40):
            pygame.draw.circle(fog, (80, 0, 40, 30), (rng.randint(0, w), rng.randint(int(h * .4), h)), rng.randint(40, 140))
        s.blit(fog, (0, 0))
    elif th == "circo":
        _grad(s, (40, 10, 30), (10, 4, 10))
        for i in range(16):
            a1, a2 = i / 16 * math.pi, (i + 1) / 16 * math.pi
            col = (200, 30, 40) if i % 2 else (240, 230, 210)
            pygame.draw.polygon(s, col, [(w / 2, -40), (w / 2 + math.cos(a1) * w, h * .1 + math.sin(a1) * h * .5),
                                         (w / 2 + math.cos(a2) * w, h * .1 + math.sin(a2) * h * .5)])
        pygame.draw.ellipse(s, (120, 60, 30), (w * .15, h * .7, w * .7, h * .35))
        pygame.draw.ellipse(s, (240, 200, 60), (w * .15, h * .7, w * .7, h * .35), 8)
    elif th == "laboratorio":
        _grad(s, (200, 220, 235), (120, 140, 160))
        for i in range(5):
            x = 80 + i * 240
            pygame.draw.rect(s, (230, 240, 250), (x, h * .25, 60, h * .5), border_radius=30)
            pygame.draw.rect(s, (80, 220, 200) if "miedo" not in k else (130, 20, 90), (x + 6, h * .45, 48, h * .28), border_radius=24)
            pygame.draw.rect(s, INK, (x, h * .25, 60, h * .5), 3, border_radius=30)
        for i in range(3):
            pygame.draw.rect(s, (20, 30, 50), (180 + i * 330, 60, 240, 130))
            for j in range(6):
                pygame.draw.line(s, (90, 220, 255), (190 + i * 330, 80 + j * 18), (190 + i * 330 + rng.randint(40, 220), 80 + j * 18), 3)
        pygame.draw.rect(s, (90, 100, 115), (0, int(h * .82), w, h))
        if "ataque" in k or "miedo" in k:
            _poly(s, (20, 20, 30), [(w * .7, h * .2), (w * .78, h * .05), (w * .9, h * .3), (w * .85, h * .55), (w * .72, h * .45)])
    elif th == "hospital":
        _grad(s, (210, 230, 220), (160, 190, 180))
        pygame.draw.rect(s, (140, 190, 230), (w * .6, h * .12, w * .3, h * .38))
        pygame.draw.rect(s, (240, 240, 245), (w * .6, h * .12, w * .3, h * .38), 8)
        pygame.draw.rect(s, (245, 245, 250), (w * .1, h * .6, w * .5, h * .14), border_radius=10)
        pygame.draw.rect(s, (120, 170, 210), (w * .1, h * .66, w * .5, h * .1), border_radius=10)
        pygame.draw.rect(s, (130, 150, 150), (0, int(h * .85), w, h))
    elif th == "gimnasio":
        _grad(s, (50, 50, 60), (20, 20, 26))
        for i in range(6):
            pygame.draw.rect(s, (70, 70, 84), (60 + i * 210, h * .3, 12, h * .5))
        pygame.draw.rect(s, (60, 40, 30), (0, int(h * .8), w, h))
        pygame.draw.rect(s, (200, 40, 50), (0, int(h * .78), w, 10))
    else:  # interior
        warm = any(t in k for t in ("casa", "cuarto", "departamento", "boda", "orfanato", "patio", "escuela", "cafe"))
        base = (90, 70, 60) if warm else _darker(tint, .3)
        _grad(s, _lighter(base, .15), _darker(base, .5))
        pygame.draw.rect(s, (16, 18, 34), (w * .55, h * .1, w * .38, h * .45))
        sub = pygame.Surface((int(w * .38), int(h * .45)))
        _grad(sub, (10, 12, 30), (40, 40, 80))
        _skyline(sub, rng, int(h * .45), (20, 20, 34), hmin=40, hmax=200)
        s.blit(sub, (w * .55, h * .1))
        pygame.draw.rect(s, (40, 36, 40), (w * .55, h * .1, w * .38, h * .45), 10)
        pygame.draw.line(s, (40, 36, 40), (w * .74, h * .1), (w * .74, h * .55), 8)
        pygame.draw.rect(s, _darker(base, .6), (0, int(h * .78), w, h))
        for i in range(3):
            x = 60 + i * 260
            pygame.draw.rect(s, _darker(base, .35), (x, h * .62, 200, 24))
            pygame.draw.rect(s, _darker(base, .55), (x + 10, h * .66, 14, 90))
            pygame.draw.rect(s, _darker(base, .55), (x + 176, h * .66, 14, 90))
        if any(t in k for t in ("treeman", "mighty", "dos_", "fomo", "comision", "oficina", "archivo", "rock")):
            f = pygame.font.SysFont("bahnschrift,arialblack", 120, bold=True)
            word = next((n for t, n in (("treeman", "TREEMAN"), ("mighty", "MIGHTY GLORY"), ("dos_", "DOS"),
                                       ("fomo", "FOMO"), ("comision", "COMISIÓN"), ("rock", "MIGHTY GLORY")) if t in k), "")
            if word:
                t = f.render(word, True, (255, 255, 255))
                t.set_alpha(28)
                s.blit(t, (40, 40))
        if "sotano" in k or "escondite" in k or "carcel" in k:
            s.fill((60, 60, 60), special_flags=pygame.BLEND_RGB_SUB)
    # tinte del capítulo
    tint_s = pygame.Surface(size, pygame.SRCALPHA)
    tint_s.fill((*tint, 38))
    s.blit(tint_s, (0, 0))
    if "lluvia" in k and th != "calle":
        _rain(s, rng)
    _vignette(s)
    return s


def chapter_card(name: str, size, color, img: pygame.Surface | None = None,
                 art: pygame.Surface | None = None) -> pygame.Surface:
    """Arte de la carta de un capítulo: fondo de acción + retrato del representante."""
    w, h = size
    s = pygame.Surface(size)
    _grad(s, _lighter(color, .25), _darker(color, .6))
    rng = random.Random(_seed(name + "card"))
    for _ in range(14):
        x = rng.randint(-w, w)
        pygame.draw.line(s, _lighter(color, .5), (x, h), (x + h * .6, 0), rng.randint(2, 10))
    if art is not None:
        # arte oficial ancho: se escala para llenar la altura y se centra
        sc = max(h / art.get_height(), w / art.get_width())
        p = pygame.transform.smoothscale(art, (int(art.get_width() * sc), int(art.get_height() * sc)))
        s.blit(p, p.get_rect(center=(w // 2, h // 2)))
        return s
    if img is not None:
        sc = h * .95 / img.get_height()
        p = pygame.transform.smoothscale(img, (int(img.get_width() * sc), int(h * .95)))
    else:
        p = portrait(name, int(h * .92))
    s.blit(p, p.get_rect(midbottom=(w // 2, h)))
    return s
