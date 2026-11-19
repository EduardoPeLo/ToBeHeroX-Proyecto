"""Carga todos los capítulos y finales de la historia."""
from importlib import import_module

CHAPTER_MODULES = [
    "cap01_nice", "cap02_esoul", "cap03_cyan", "cap04_queen", "cap05_loli",
    "cap06_ghostblade", "cap07_johnnies", "cap08_ruinas", "cap09_dragon",
    "cap10_ahu", "cap11_x",
]


class Story:
    def __init__(self):
        self.chapters = {}
        self._nodes = {}
        for name in CHAPTER_MODULES:
            ch = import_module(f"story.{name}").ch
            self.chapters[ch.num] = ch
            for nid, node in ch.nodes.items():
                if nid in self._nodes:
                    raise ValueError(f"Nodo repetido entre capítulos: {nid}")
                self._nodes[nid] = node
        from story.finales import ENDINGS
        self.endings = ENDINGS

    def node(self, nid):
        try:
            return self._nodes[nid]
        except KeyError:
            raise KeyError(f"No existe el nodo '{nid}'") from None

    @property
    def nodes(self):
        return self._nodes


_story = None


def load_story() -> Story:
    global _story
    if _story is None:
        _story = Story()
    return _story
