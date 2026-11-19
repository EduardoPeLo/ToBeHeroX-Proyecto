"""Estado de partida y lógica del juego (independiente de la interfaz)."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

from engine.model import Node, Option

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_DIR = os.path.join(ROOT, "saves")
GALLERY_FILE = os.path.join(SAVE_DIR, "galeria.json")

LAST_REGULAR_CHAPTER = 10   # Ahu
X_CHAPTER = 11              # X (sólo con el hilo del destino intacto)


@dataclass
class State:
    chapter: int = 1
    node: str | None = None
    flags: set = field(default_factory=set)
    vars: dict = field(default_factory=dict)
    done: list = field(default_factory=list)
    majors: list = field(default_factory=list)      # [[cap, bandera, final]]
    minors: int = 0
    canon_taken: int = 0
    decisions: int = 0
    scores: dict = field(default_factory=dict)
    ending: str | None = None
    log: list = field(default_factory=list)         # historial de decisiones
    checkpoints: dict = field(default_factory=dict)  # estado al empezar cada capítulo

    @property
    def thread_intact(self) -> bool:
        """El 'hilo del destino' sigue intacto si no hubo desviaciones mayores."""
        return not self.majors

    def to_json(self) -> dict:
        d = self.__dict__.copy()
        d["flags"] = sorted(self.flags)
        return d

    def snapshot(self) -> dict:
        d = self.to_json()
        d.pop("checkpoints", None)
        return json.loads(json.dumps(d))

    @classmethod
    def from_json(cls, d: dict) -> "State":
        s = cls()
        for k, v in d.items():
            setattr(s, k, v)
        s.flags = set(d.get("flags", []))
        s.checkpoints = dict(d.get("checkpoints", {}))
        return s


class Game:
    def __init__(self, story, state: State | None = None):
        self.story = story
        self.state = state or State()
        if self.state.node is None:
            self.state.checkpoints[str(self.state.chapter)] = self.state.snapshot()
            self.state.node = story.chapters[self.state.chapter].start
            self._enter(self.node)

    # ---------- utilidades ----------
    @property
    def node(self) -> Node:
        return self.story.node(self.state.node)

    @property
    def chapter(self):
        return self.story.chapters[self.state.chapter]

    def visible_lines(self, node: Node | None = None):
        node = node or self.node
        return [ln for ln in node.lines if ln.cond is None or ln.cond(self.state)]

    def options(self, node: Node | None = None) -> list[Option]:
        node = node or self.node
        return [o for o in node.opts if o.cond is None or o.cond(self.state)]

    def _apply(self, set_: dict, add: dict):
        for k, v in set_.items():
            if v:
                self.state.flags.add(k)
            else:
                self.state.flags.discard(k)
        for k, v in add.items():
            self.state.vars[k] = self.state.vars.get(k, 0) + v

    def _resolve(self, node_id: str) -> str:
        """Sigue redirecciones condicionales (p. ej. si un personaje murió)."""
        seen = set()
        while True:
            n = self.story.node(node_id)
            target = None
            for fn, _src, tgt in n.redirect:
                if fn(self.state):
                    target = tgt
                    break
            if target is None or target in seen:
                return node_id
            seen.add(node_id)
            node_id = target

    def _enter(self, node: Node):
        self._apply(node.set, node.add)

    def goto(self, node_id: str):
        node_id = self._resolve(node_id)
        self.state.node = node_id
        self._enter(self.node)

    # ---------- acciones ----------
    def choose(self, opt: Option):
        s = self.state
        s.decisions += 1
        if opt.tag == "canon":
            s.canon_taken += 1
        elif opt.tag == "minor":
            s.minors += 1
        elif opt.tag == "major":
            s.majors.append([s.chapter, opt.flag, opt.ending])
            s.flags.add(opt.flag)
            s.scores[opt.ending] = s.scores.get(opt.ending, 0) + 1
        s.log.append([s.chapter, self.node.ask or "", opt.text, opt.tag])
        self._apply(opt.set, opt.add)
        self.goto(opt.to)

    def advance(self):
        """Avanza en nodos sin decisión (escena lineal o pelea)."""
        if self.node.next:
            self.goto(self.node.next)

    def finish_chapter(self) -> str:
        """Llamar al llegar a un nodo 'end'. Devuelve:
        'next' (hay siguiente capítulo), 'x' (se desbloqueó X) o 'ending' (final)."""
        s = self.state
        node = self.node
        if s.chapter not in s.done:
            s.done.append(s.chapter)
        if s.chapter == X_CHAPTER:
            s.ending = self._ending_from_flags()
            return "ending"
        if s.chapter == LAST_REGULAR_CHAPTER:
            if s.thread_intact:
                self._start_chapter(X_CHAPTER)
                return "x"
            s.ending = self.compute_ending()
            return "ending"
        self._start_chapter(s.chapter + 1)
        return "next"

    def _ending_from_flags(self) -> str:
        for f in ("fin_x_ejecutado", "fin_x_retirado"):
            if f in self.state.flags:
                return {"fin_x_ejecutado": "E12", "fin_x_retirado": "E13"}[f]
        return "E01"

    def compute_ending(self) -> str:
        """Elige el final alternativo con más peso; empata a favor del más reciente."""
        s = self.state
        best, best_key = None, "E06"
        for idx, (cap, _flag, end) in enumerate(s.majors):
            score = (s.scores.get(end, 0), cap, idx)
            if best is None or score > best:
                best, best_key = score, end
        return best_key

    def _start_chapter(self, num: int):
        self.state.chapter = num
        self.state.node = None
        self.state.checkpoints[str(num)] = self.state.snapshot()
        self.goto(self.story.chapters[num].start)

    def can_replay(self, num: int) -> bool:
        return str(num) in self.state.checkpoints

    def replay(self, num: int):
        """Vuelve al inicio de un capítulo ya jugado (se pierde lo posterior)."""
        cps = {k: v for k, v in self.state.checkpoints.items() if int(k) <= num}
        snap = cps[str(num)]
        st = State.from_json(snap)
        st.checkpoints = cps
        st.chapter = num
        st.node = None
        self.state = st
        self.goto(self.story.chapters[num].start)


# ---------- guardado ----------
def save_path(slot: int) -> str:
    return os.path.join(SAVE_DIR, f"partida{slot}.json")


def save_game(state: State, slot: int):
    os.makedirs(SAVE_DIR, exist_ok=True)
    with open(save_path(slot), "w", encoding="utf-8") as f:
        json.dump(state.to_json(), f, ensure_ascii=False, indent=1)


def load_game(slot: int) -> State | None:
    try:
        with open(save_path(slot), encoding="utf-8") as f:
            return State.from_json(json.load(f))
    except (OSError, ValueError):
        return None


def load_gallery() -> list[str]:
    try:
        with open(GALLERY_FILE, encoding="utf-8") as f:
            return list(json.load(f))
    except (OSError, ValueError):
        return []


def unlock_ending(key: str):
    g = load_gallery()
    if key not in g:
        g.append(key)
        os.makedirs(SAVE_DIR, exist_ok=True)
        with open(GALLERY_FILE, "w", encoding="utf-8") as f:
            json.dump(g, f)
