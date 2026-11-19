"""Genera assets/LISTA_DE_ARCHIVOS.md con todos los nombres de imágenes, videos y música
que el juego busca, indicando en qué capítulo/escena se usan.

Uso:  python tools/lista_assets.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from engine.assets import ASSETS, IMG_EXT, VIDEO_EXT, find, slug  # noqa: E402
from story import load_story  # noqa: E402


def mark(folder, key, exts):
    return "✅" if find(folder, key, exts) else "⬜"


def main():
    st = load_story()
    bgs, chars, fights = {}, {}, []
    for n in st.nodes.values():
        if n.bg:
            bgs.setdefault(n.bg, set()).add(n.chapter)
        for ln in n.lines:
            if ln.speaker:
                chars.setdefault(ln.speaker, set()).add(n.chapter)
        if n.fight:
            fights.append((n.chapter, n.fight.video, n.fight.title))
            for who in (n.fight.a, n.fight.b):
                chars.setdefault(who, set()).add(n.chapter)
    for e in st.endings.values():
        bgs.setdefault(e.bg, set()).add("final " + e.key)
    out = ["# Lista de archivos multimedia", "",
           "Generado por `python tools/lista_assets.py`. ✅ = ya existe, ⬜ = falta.",
           "Formatos de imagen: .png .jpg .jpeg .webp — video: .mp4 .webm .mkv .avi — audio: .ogg .mp3 .wav", "",
           "## Fondos (`assets/fondos/`)", "", "| Archivo | Capítulos | |", "|---|---|---|"]
    out.append(f"| titulo | menú principal | {mark('fondos', 'titulo', IMG_EXT)} |")
    for num in sorted(st.chapters):
        k = f"cap{num:02d}_titulo"
        out.append(f"| {k} | portada del capítulo {num} | {mark('fondos', k, IMG_EXT)} |")
    for k in sorted(bgs):
        caps = ", ".join(str(c) for c in sorted(bgs[k], key=str))
        out.append(f"| {k} | {caps} | {mark('fondos', k, IMG_EXT)} |")
    out += ["", "## Personajes (`assets/personajes/`, PNG con fondo transparente)", "",
            "| Archivo | Personaje | |", "|---|---|---|"]
    for name in sorted(chars):
        out.append(f"| {slug(name)} | {name} | {mark('personajes', slug(name), IMG_EXT)} |")
    out += ["", "## Videos de peleas (`assets/videos/`)", "",
            "Antes de cada pelea canónica se reproduce el archivo local si existe; si no, el video oficial de YouTube indicado en story/medios.py. Para que un archivo local tenga sonido, pon junto a él un audio con el mismo nombre (.mp3/.ogg).",
            "", "| Archivo | Capítulo | Pelea | |", "|---|---|---|---|"]
    for c, k, t in sorted(fights):
        out.append(f"| {k} | {c} | {t} | {mark('videos', k, VIDEO_EXT)} |")
    from story import medios
    out += ["", "## Cartas del menú de capítulos (`assets/cartas/`, opcional)", "",
            "Si no existen, la carta usa el retrato del personaje representante.", ""]
    out += [f"- `cap{n:02d}` — {st.chapters[n].title} (representa: {medios.REPRESENTANTE[n]})" for n in sorted(st.chapters)]
    out += ["", "## Otros videos opcionales (`assets/videos/`)", "",
            "- `opening` — se reproduce al abrir el juego (si no existe, se usa el opening oficial de YouTube)"]
    out += [f"- `trailer_cap{n:02d}` — tráiler del capítulo {n}" for n in sorted(st.chapters)]
    out += [f"- `cap{n:02d}_intro` — se reproduce al empezar el capítulo {n}" for n in sorted(st.chapters)]
    out += [f"- `fin_{k}` — se reproduce al llegar al final {k} ({e.title})" for k, e in sorted(st.endings.items())]
    out += ["", "## Música (`assets/musica/`)", "",
            "- `titulo` — menú principal", "- `fin_x` — final canónico", "- `fin` — finales alternativos"]
    out += [f"- `cap{n:02d}` — capítulo {n} ({st.chapters[n].title})" for n in sorted(st.chapters)]
    path = os.path.join(ASSETS, "LISTA_DE_ARCHIVOS.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("Escrito", path)


if __name__ == "__main__":
    main()
