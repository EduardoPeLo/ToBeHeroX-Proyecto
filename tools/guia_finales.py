"""Genera GUIA_DE_FINALES.md: qué decisión mayor lleva a cada final."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from story import load_story  # noqa: E402

st = load_story()
by_end = {}
for n in st.nodes.values():
    for o in n.opts:
        if o.tag == "major":
            by_end.setdefault(o.ending, []).append((n.chapter, n.ask, o.text))
out = ["# Guía de finales (¡spoilers!)", "",
       "Si hay varias desviaciones mayores en una partida, gana el final con más puntos; si empatan, el de la decisión más reciente.", "",
       "## E01: X (final canónico)", "",
       "Sigue la historia del anime en los capítulos 1-10 (puedes usar opciones *menores*). Así se desbloquea el capítulo 11. Allí, elige las opciones canónicas.", ""]
for k in sorted(st.endings):
    if k == "E01":
        continue
    e = st.endings[k]
    out.append(f"## {k}: {e.title}")
    out.append("")
    for cap, ask, txt in sorted(by_end.get(k, [])):
        out.append(f"- Capítulo {cap}: *{ask}* → **{txt}**")
    out.append("")
open("GUIA_DE_FINALES.md", "w", encoding="utf-8").write("\n".join(out))
print("ok")
