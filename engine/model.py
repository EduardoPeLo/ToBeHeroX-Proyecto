"""Modelo de datos de la historia: capítulos, nodos, opciones y condiciones.

Los capítulos se escriben en story/capXX_*.py usando un mini-lenguaje:

    ch.scene("id", bg="fondo", text='''
    Narración sin nombre.
    Lin Ling: Diálogo con nombre.
    [?moon_viva] Moon: Esta línea sólo aparece si la bandera moon_viva está activa.
    [rel_moon<0] Moon: Esta aparece si la relación con Moon es negativa.
    ''', ask="Pregunta", opts=[C(...), M(...), X(...)])

Tipos de opción:
    C  -> opción CANÓNICA (lo que pasa en el anime).
    M  -> desviación MENOR (no rompe el hilo del destino; puede cambiar actitudes).
    X  -> desviación MAYOR (rompe el canon, activa una bandera y suma a un final).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Callable

SPEAKER_RE = re.compile(r"^([A-ZÁÉÍÓÚÑ¿][\wÁÉÍÓÚáéíóúñü.\-' ]{0,24}):\s+(.*)$")
COND_RE = re.compile(r"^\[([^\]]+)\]\s*(.*)$")
# Sólo estos nombres se interpretan como "Personaje: diálogo". Cualquier otra
# línea con dos puntos se trata como narración.
SPEAKERS = {
    "Voz", "X", "Lin Ling", "Miss J", "Shand", "Moon", "Fan", "Ex-jefe", "Wreck",
    "Wolf Girl", "Firm-Man", "God Eye", "Blankster", "E-Soul", "Presentador", "Niño",
    "Enlighter", "Yang Cheng", "Xia Qing", "Pomelo", "Shang Chao", "Rock", "Secuestrador",
    "Mánager", "Liu Zhen", "Cyan", "Luo", "Directora", "Mickey", "Queen", "Liu Yuwei",
    "Bowa", "Loli", "Luo Li", "Nuonuo", "Padre de Loli", "DJ Shindig", "Ghostblade",
    "Wang Yi", "Zhang Lan", "Little Johnny", "Big Johnny", "Ah Sheng", "Vortex", "Zac",
    "Nice", "Dragon Boy", "Smile", "Ahu", "Xin Ya", "Clon", "Agente", "Comisionado",
    "Periodista", "Aldeano", "Huérfano", "Científico", "Cirquero", "Madre de Dragon Boy",
    "Ejecutivo", "Locutor", "Director", "E-Soul original",
}
CMP_RE = re.compile(r"^([a-z_0-9]+)\s*(<=|>=|==|!=|<|>)\s*(-?\d+)$")


def compile_cond(expr: str | None) -> Callable | None:
    """Convierte una condición de texto en una función(state) -> bool.

    Sintaxis: 'bandera', '!bandera', 'var<0', 'a&b', 'a|b' (| tiene menor prioridad).
    """
    if not expr:
        return None
    expr = expr.strip()

    def atom(tok: str):
        tok = tok.strip()
        if tok.startswith("!"):
            inner = atom(tok[1:])
            return lambda s: not inner(s)
        m = CMP_RE.match(tok)
        if m:
            var, op, num = m.group(1), m.group(2), int(m.group(3))
            ops = {
                "<": lambda a, b: a < b, ">": lambda a, b: a > b,
                "<=": lambda a, b: a <= b, ">=": lambda a, b: a >= b,
                "==": lambda a, b: a == b, "!=": lambda a, b: a != b,
            }
            f = ops[op]
            return lambda s: f(s.vars.get(var, 0), num)
        return lambda s: tok in s.flags

    ors = []
    for part in expr.split("|"):
        ands = [atom(t) for t in part.split("&")]
        ors.append(lambda s, ands=ands: all(a(s) for a in ands))
    return lambda s: any(o(s) for o in ors)


@dataclass
class Line:
    speaker: str | None
    text: str
    cond: Callable | None = None
    cond_src: str | None = None


def parse_text(text: str) -> list[Line]:
    lines: list[Line] = []
    for raw in text.strip().splitlines():
        raw = raw.strip()
        if not raw:
            continue
        cond_src = None
        m = COND_RE.match(raw)
        if m:
            cond_src, raw = m.group(1), m.group(2)
        sm = SPEAKER_RE.match(raw)
        if sm and sm.group(1).strip() in SPEAKERS:
            speaker, body = sm.group(1).strip(), sm.group(2).strip()
        else:
            speaker, body = None, raw
        lines.append(Line(speaker, body, compile_cond(cond_src), cond_src))
    return lines


@dataclass
class Option:
    text: str
    to: str
    tag: str  # 'canon' | 'minor' | 'major'
    flag: str | None = None
    ending: str | None = None
    set: dict = field(default_factory=dict)
    add: dict = field(default_factory=dict)
    cond: Callable | None = None
    cond_src: str | None = None


def C(text, to, set=None, add=None, cond=None):
    """Opción canónica."""
    return Option(text, to, "canon", set=set or {}, add=add or {},
                  cond=compile_cond(cond), cond_src=cond)


def M(text, to, set=None, add=None, cond=None):
    """Desviación menor: no rompe el canon."""
    return Option(text, to, "minor", set=set or {}, add=add or {},
                  cond=compile_cond(cond), cond_src=cond)


def X(text, to, flag, ending, set=None, add=None, cond=None):
    """Desviación mayor: rompe el canon, activa `flag` y suma puntos al final `ending`."""
    return Option(text, to, "major", flag=flag, ending=ending, set=set or {},
                  add=add or {}, cond=compile_cond(cond), cond_src=cond)


@dataclass
class Fight:
    title: str
    a: str
    b: str
    beats: list[str]
    winner: str = "a"  # 'a', 'b' o 'none'
    video: str | None = None


@dataclass
class Node:
    id: str
    chapter: int
    kind: str = "scene"  # scene | fight | end
    canon: bool = False
    bg: str | None = None
    lines: list[Line] = field(default_factory=list)
    ask: str | None = None
    opts: list[Option] = field(default_factory=list)
    next: str | None = None
    redirect: list = field(default_factory=list)  # [(cond_fn, cond_src, node_id)]
    set: dict = field(default_factory=dict)
    add: dict = field(default_factory=dict)
    fight: Fight | None = None
    end_title: str | None = None
    alt_end: bool = False
    video: str | None = None

    @property
    def is_decision(self) -> bool:
        return bool(self.opts)


class Chapter:
    def __init__(self, num: int, title: str, eps: str, start: str, color=(40, 40, 60),
                 intro: str = "", music: str | None = None):
        self.num = num
        self.title = title
        self.eps = eps
        self.start = start
        self.color = color
        self.intro = intro.strip()
        self.music = music or f"cap{num:02d}"
        self.nodes: dict[str, Node] = {}

    def _add(self, node: Node) -> Node:
        if node.id in self.nodes:
            raise ValueError(f"Nodo duplicado: {node.id}")
        self.nodes[node.id] = node
        return node

    def scene(self, id, text="", bg=None, ask=None, opts=None, next=None, canon=None,
              set=None, add=None, redirect=None, video=None):
        if canon is None:
            # Por convención, los nodos de rama empiezan con 'cN_b'.
            canon = "_b" not in id
        red = []
        for cond_src, target in (redirect or []):
            red.append((compile_cond(cond_src), cond_src, target))
        return self._add(Node(id, self.num, "scene", canon, bg, parse_text(text), ask,
                              list(opts or []), next, red, set or {}, add or {}, video=video))

    def fight(self, id, title, a, b, beats, next, bg=None, winner="a", video=None,
              text="", canon=None, set=None, add=None):
        if canon is None:
            canon = "_b" not in id
        n = Node(id, self.num, "fight", canon, bg, parse_text(text), next=next,
                 set=set or {}, add=add or {},
                 fight=Fight(title, a, b, list(beats), winner, video or id))
        return self._add(n)

    def end(self, id, title, text, bg=None, alt=False, set=None, add=None):
        n = Node(id, self.num, "end", not alt, bg, parse_text(text), set=set or {},
                 add=add or {}, end_title=title, alt_end=alt)
        return self._add(n)


@dataclass
class Ending:
    key: str
    title: str
    text: str
    bg: str | None = None
    canon: bool = False
