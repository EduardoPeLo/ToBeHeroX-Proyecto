# To Be Hero X: Hilos del Destino

Novela gráfica de decisiones hecha 100 % en Python, basada en el anime **To Be Hero X** (Li Haoling, bilibili / Fuji TV, 2025).
Creado por **Eduardo Pedroza López** y **Rogelio Uriel Gutierrez Jimenez**.

## Cómo jugar

```bash
python -m pip install -r requirements.txt
```

```bash
python main.py
```

También hay una versión en texto que no necesita nada instalado. Con `--pistas` se ve qué opción es canon:

```bash
python main.py --consola
```

Controles: **clic / espacio** para avanzar, **1-4** para elegir, **ESC** para pausar, **M** para activar o desactivar el soundtrack, **P** para mostrar u ocultar los colores, **H** para ver el historial y **F11** para pantalla completa. La partida se guarda sola en cada decisión, con 3 espacios de guardado.

- **Colores de las respuestas:** 🟩 verde = canon · 🟨 amarillo = no afecta del todo al canon · 🟥 rojo = modifica el canon.
- **Menú de capítulos:** muestra los 11 capítulos como cartas de personaje. Solo el primero empieza desbloqueado; al terminar uno vuelves a este menú y ves cómo se desbloquea el siguiente. Los capítulos completados se pueden **repetir**. El de X se ve **sellado** si rompiste el canon.

## Requisitos del proyecto y cómo se cumplen

| Requisito | Cómo está resuelto |
|---|---|
| Novela gráfica con decisiones que cambian el futuro | Cada decisión puede cambiar banderas y relaciones que se leen en capítulos posteriores |
| Mínimo 300 puntos de decisión | **341** decisiones (`python tools/validar.py` las cuenta) |
| 150 decisiones para la historia original | **175** decisiones en la línea canónica |
| Final real y finales alternativos | **14 finales**: el canónico de X y 13 alternativos |
| Capítulos en el orden del anime | 11 capítulos, uno por arco (episodios 1-24) |
| Cada capítulo se termina siempre, canon o no | Las rutas alternativas tienen su propio cierre de capítulo |
| El capítulo de X solo con la historia del anime | El capítulo 11 se desbloquea solo si el **hilo del destino** sigue intacto; si no, se muestra uno de los finales alternativos |
| Se llega a X aunque se tomen decisiones poco importantes | Hay 3 tipos de opción: **canon**, **menor** (no rompe el hilo) y **mayor** (lo rompe) |
| Peleas del anime en la línea canónica | 24 peleas animadas (barras de vida, golpes, temblor de pantalla) que solo aparecen en la ruta canónica; si pones el video, se reproduce el clip del anime |
| Muertes y alejamientos fuera del canon se respetan | Un personaje que murió o se fue en tu partida no reaparece a la fuerza; los capítulos 8-10 tienen versiones "hilo alterado" y el texto cambia según cómo trataste a cada uno (por ejemplo Moon, Bowa, Qing o Nuonuo) |

## Capítulos

1. **Nice** (ep. 1-4) · 2. **E-Soul** (ep. 5-7) · 3. **Lucky Cyan** (ep. 8-10) · 4. **Queen** (ep. 11-12) · 5. **Loli** (ep. 13-14) · 6. **Ghostblade** (ep. 15-16) · 7. **Los Johnnies** (ep. 17-18) · 8. **El Incidente de las Ruinas** (ep. 19-20) · 9. **Dragon Boy** (ep. 21-22) · 10. **Ahu** (ep. 23) · 11. **X** (ep. 24, sellado)

Toda la historia se cuenta como X mostrándole a Ahu "los hilos del destino" desde fuera del tiempo, igual que en el episodio 24. Por eso tus cambios afectan a capítulos que en la cronología del anime pasan antes.

## Imágenes, videos y música

**Sin descargar nada, el juego ya trae:**
- **Retratos generados** de cada personaje que habla (Lin Ling, E-Soul, Queen, X, Ahu...) y **fondos alegóricos** para cada lugar: azotea, callejón con lluvia, estadio, ovni, bosque, puerto, oficina de cada agencia o el espacio fuera del tiempo. Todo está en `engine/arte.py`.
- **Videos y música oficiales de YouTube** del canal oficial de To Be Hero X ([tbhx.net](https://tbhx.net/en/movie/)). Se reproducen incrustados en un recuadro dentro de la pantalla del juego (con pywebview; necesitan internet):
  - Al abrir el juego suena el **opening sin créditos** ("INERTIA").
  - En la línea canónica, antes de cada pelea se reproduce el **"HERO's Highlight"** oficial de ese episodio o un clip oficial de Crunchyroll (por ejemplo X contra Dragon Boy y X contra los clones). Algunas escenas también tienen su clip: el salto de Nice, la llegada al torneo, etc. Si un video no se puede ver dentro del juego, se abre en el navegador.
  - Cada capítulo tiene de **soundtrack el tema oficial de su héroe** (PARAGON, NEON RAIN, Queen of the stars...). Se activa o desactiva con la tecla **M** o desde Ajustes.
  - En el menú de capítulos, el botón **VER TRÁILER** abre el "Character Story Movie" oficial.
  - Los IDs de todos los videos están en `story/medios.py`, por si quieres cambiar alguno.

**Imágenes reales del anime (ya incluidas):** en `assets/` hay ilustraciones oficiales de los héroes y capturas de los personajes secundarios de la web oficial, y miniaturas de los videos oficiales de YouTube que sirven de fondo de cada escena (desenfocadas para que se lea el texto). `tools/importar_imagenes.py` las recorta y las coloca; en ese archivo se elige qué imagen va en cada escena. Las escenas que no tienen una imagen real siguen con el fondo generado. Los personajes sin foto aparecen como una silueta negra de estilo anime, como los personajes por desbloquear de los videojuegos. Fuente: tbhx.net y su canal de YouTube, ©bilibili/BeDream, Aniplex. Se usan solo para este proyecto escolar sin fines de lucro.

**Para poner tus propias capturas o clips**, que tienen prioridad sobre lo generado y sobre YouTube:
1. Ejecuta `python tools/lista_assets.py`. Genera [assets/LISTA_DE_ARCHIVOS.md](assets/LISTA_DE_ARCHIVOS.md) con el nombre exacto de cada archivo.
2. Copia los archivos a `assets/fondos/`, `assets/personajes/` (PNG con fondo transparente), `assets/cartas/`, `assets/videos/` o `assets/musica/`.

## Estructura

```
main.py               ← arranque (gráfico o --consola)
jugar_consola.py      ← versión en texto
engine/model.py       ← mini-lenguaje para escribir la historia (escenas, opciones C/M/X, peleas)
engine/game.py        ← lógica: banderas, hilo del destino, finales, guardado
engine/ui.py          ← interfaz pygame (menú estilo hero shooter, cartas de capítulos, escenas, peleas)
engine/arte.py        ← retratos y fondos alegóricos generados por código
engine/reproductor.py ← soundtrack por capítulo, ajustes y videos
engine/visor_web.py   ← visor de los videos oficiales de YouTube (pywebview)
engine/assets.py      ← carga de imágenes, música y videos locales
story/medios.py       ← IDs de los videos y temas oficiales de YouTube
story/cap01..cap11    ← los 11 capítulos
story/finales.py      ← los 14 finales
tools/validar.py      ← comprueba conteos, enlaces y que todos los finales se alcanzan
tools/lista_assets.py ← genera la lista de archivos multimedia
GUIA_DE_FINALES.md    ← cómo conseguir cada final (con spoilers)
```

## Editar la historia

Cada escena se escribe así (en `story/capXX_*.py`):

```python
ch.scene("c1_05", bg="c1_plaza_fans", text="""
Narración sin nombre.
Lin Ling: Diálogo de un personaje.
[rel_moon<0] Moon: Esta línea solo aparece si trataste mal a Moon.
""", ask="¿Qué hace Lin Ling?", opts=[
    C("Opción canónica", "c1_06"),
    M("Desviación menor", "c1_06", add={"rel_moon": 1}),
    X("Desviación mayor", "c1_bA1", flag="lin_confiesa", ending="E02"),
])
```

Después de editar, ejecuta `python tools/validar.py` para comprobar que todo sigue conectado.

---
*To Be Hero X y sus personajes pertenecen a sus creadores (Li Haoling / bilibili / Fuji TV). Este proyecto escolar es de fans y no tiene fines de lucro. Los textos son una adaptación libre y resumida de la trama.*
