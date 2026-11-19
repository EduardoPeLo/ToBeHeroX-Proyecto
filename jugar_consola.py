"""Versión en texto del juego (útil para probar rutas rápido)."""
import sys

from engine.game import Game, State, load_game, save_game, unlock_ending
from story import load_story

TAGS = {"canon": "[canon]", "minor": "[menor]", "major": "[ROMPE EL CANON]"}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    story = load_story()
    hints = "--pistas" in sys.argv
    st = load_game(9) if "--continuar" in sys.argv else None
    g = Game(story, st or State())
    print("=== TO BE HERO X — Hilos del Destino (modo texto) ===")
    print("Escribe el número de la opción. 'q' guarda y sale.\n")
    shown_ch = None
    while True:
        node = g.node
        if shown_ch != g.state.chapter:
            ch = g.chapter
            print(f"\n######## CAPÍTULO {ch.num}: {ch.title} ({ch.eps}) ########\n{ch.intro}\n")
            shown_ch = g.state.chapter
        for ln in g.visible_lines():
            print(f"{ln.speaker}: {ln.text}" if ln.speaker else ln.text)
        if node.kind == "fight":
            print(f"\n*** PELEA: {node.fight.title} ***")
            for b in node.fight.beats:
                print("  >", b)
            g.advance()
            continue
        if node.kind == "end":
            print(f"\n--- {node.end_title} ---  (hilo {'intacto' if g.state.thread_intact else 'alterado'})")
            r = g.finish_chapter()
            save_game(g.state, 9)
            if r == "x":
                print("\n*** Seguiste el destino tal como fue tejido. Se desbloquea el capítulo final: X ***")
            if r == "ending":
                e = story.endings[g.state.ending]
                unlock_ending(e.key)
                print(f"\n================ FINAL {e.key}: {e.title} ================\n{e.text.strip()}\n")
                return
            continue
        opts = g.options()
        if not opts:
            g.advance()
            continue
        print(f"\n>> {node.ask}")
        for i, o in enumerate(opts, 1):
            print(f"  {i}. {o.text} {TAGS[o.tag] if hints else ''}")
        while True:
            a = input("> ").strip().lower()
            if a == "q":
                save_game(g.state, 9)
                print("Partida guardada en el espacio 9 (usa --continuar).")
                return
            if a.isdigit() and 1 <= int(a) <= len(opts):
                g.choose(opts[int(a) - 1])
                break
        print()


if __name__ == "__main__":
    main()
