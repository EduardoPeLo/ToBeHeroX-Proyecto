"""To Be Hero X — Hilos del Destino.

Novela gráfica de decisiones basada en el anime To Be Hero X.
Creado por Eduardo Pedroza López y Rogelio Uriel Gutierrez Jimenez.

Ejecutar:  python main.py            (versión gráfica, requiere pygame-ce)
           python main.py --consola  (versión en texto, sin dependencias)
"""
import sys


def main():
    if "--consola" in sys.argv:
        from jugar_consola import main as consola
        consola()
        return
    try:
        import pygame  # noqa: F401
    except ImportError:
        print("No se encontró pygame. Instálalo con:  python -m pip install -r requirements.txt")
        print("Mientras tanto, puedes jugar en modo texto:  python main.py --consola")
        sys.exit(1)
    from engine.ui import main as ui
    ui()


if __name__ == "__main__":
    main()
