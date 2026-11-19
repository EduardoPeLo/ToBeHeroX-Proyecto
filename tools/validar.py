"""Valida la historia: referencias, conteo de decisiones y finales alcanzables.

Uso:  python tools/validar.py
"""
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine.game import Game, State, X_CHAPTER  # noqa: E402
from engine.model import SPEAKER_RE, SPEAKERS  # noqa: E402
from story import load_story  # noqa: E402


def check_refs(story):
    errors, warnings = [], []
    for nid, n in story.nodes.items():
        targets = [o.to for o in n.opts] + ([n.next] if n.next else []) + [t for _, _, t in n.redirect]
        for t in targets:
            if t not in story.nodes:
                errors.append(f"{nid} -> {t} (no existe)")
        if n.kind != "end" and not n.opts and not n.next:
            errors.append(f"{nid}: nodo sin salida")
        for ln in n.lines:
            if ln.speaker is None:
                m = SPEAKER_RE.match(ln.text)
                if m and len(m.group(1).split()) <= 2 and m.group(1) not in SPEAKERS:
                    warnings.append(f"{nid}: se lee como narración: '{m.group(1)}:'")
    return errors, warnings


def count(story):
    total = canon = 0
    per = {}
    for n in story.nodes.values():
        if n.is_decision:
            total += 1
            per.setdefault(n.chapter, [0, 0])
            per[n.chapter][0] += 1
            if n.canon:
                canon += 1
                per[n.chapter][1] += 1
    return total, canon, per


def play(story, policy, rng=None, max_steps=5000):
    g = Game(story, State())
    seen = set()
    for _ in range(max_steps):
        node = g.node
        seen.add(node.id)
        if node.kind == "end":
            r = g.finish_chapter()
            if r == "ending":
                return g.state, seen
            continue
        if node.opts:
            g.choose(policy(g, g.options(), rng))
        else:
            g.advance()
    raise RuntimeError(f"Partida sin terminar en {g.node.id}")


def canon_policy(g, opts, rng):
    return next((o for o in opts if o.tag == "canon"), opts[0])


def minor_policy(g, opts, rng):
    for tag in ("minor", "canon"):
        for o in opts:
            if o.tag == tag:
                return o
    return opts[0]


def random_policy(g, opts, rng):
    return rng.choice(opts)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    story = load_story()
    errs, warns = check_refs(story)
    for w in warns:
        print("aviso:", w)
    for e in errs:
        print("ERROR:", e)

    total, canon, per = count(story)
    print(f"\nPuntos de decisión totales: {total}  (mínimo 300)")
    print(f"Decisiones de la historia original: {canon}  (mínimo 150)")
    print(f"Decisiones de rutas alternativas: {total - canon}")
    for ch in sorted(per):
        print(f"  Capítulo {ch:2d} {story.chapters[ch].title:28s} total {per[ch][0]:3d}  canon {per[ch][1]:3d}")
    print(f"Finales definidos: {len(story.endings)}")

    st, _ = play(story, canon_policy)
    assert st.ending == "E01" and X_CHAPTER in st.done, "La ruta canónica no llega al final de X"
    print("\nRuta 100% canónica -> final", st.ending, "(OK)")
    st, _ = play(story, minor_policy)
    assert st.ending == "E01", "Con solo desviaciones menores debería llegarse a X"
    print("Ruta con desviaciones menores -> final", st.ending, "(OK)")

    rng = random.Random(1)
    reached, visited = {}, set()
    for _ in range(20000):
        st, seen = play(story, random_policy, rng)
        visited |= seen
        reached[st.ending] = reached.get(st.ending, 0) + 1

    # Forzar cada desviación mayor individualmente desde la ruta canónica.
    majors = [(nid, i) for nid, n in story.nodes.items() for i, o in enumerate(n.opts) if o.tag == "major"]
    for nid, idx in majors:
        def pol(g, opts, rng, nid=nid, idx=idx):
            if g.node.id == nid:
                return g.node.opts[idx]
            return canon_policy(g, opts, rng)
        st, seen = play(story, pol)
        visited |= seen
        reached[st.ending] = reached.get(st.ending, 0) + 1

    print("\nFinales alcanzados:")
    for k in sorted(story.endings):
        print(f"  {k} {story.endings[k].title:28s} {'OK' if k in reached else 'NO ALCANZADO'}")
    missing = [k for k in story.endings if k not in reached]
    unvisited = sorted(set(story.nodes) - visited)
    if unvisited:
        print(f"\nNodos nunca visitados ({len(unvisited)}):", ", ".join(unvisited[:40]))
    ok = not errs and total >= 300 and canon >= 150 and not missing and len(story.endings) >= 11
    print("\nRESULTADO:", "TODO CORRECTO" if ok else "HAY PROBLEMAS")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
