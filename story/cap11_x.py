"""Capítulo 11: X (episodio 24). Solo se desbloquea con el hilo del destino intacto."""
from engine.model import Chapter, C, M, X

ch = Chapter(11, "X", "Episodio 24", start="c11_00", color=(15, 15, 25), intro="""
El número 1. Un epíteto, no un nombre. Un oficinista que puede doblar el espacio y que nunca pidió ser un dios.
""")

ch.scene("c11_00", bg="fuera_del_tiempo", text="""
Voz: Has recorrido todos los hilos sin romper ninguno. Pocas personas lo consiguen.
Voz: Supongo que ya es hora de que sepas quién te habla.
""", next="c11_01")

# ---------------- EPISODIO 24: X ----------------
ch.scene("c11_01", bg="c11_fomo_noche", text="""
La oficina de FOMO, de noche. Solo queda una lámpara encendida. Un oficinista de corbata termina un informe.
Ahu entra caminando sobre sus cuatro patas, con las orejas gachas.
Ahu: La Comisión me envió. Me pidió que te eliminara.
X: Lo sé.
""", ask="Eres Ahu. ¿Qué le dices a X?", opts=[
    C("'No quiero hacerlo'", "c11_02"),
    M("'¿Por qué no huyes?'", "c11_02"),
    M("'Me salvaste. No puedo'", "c11_02", add={"rel_x": 1}),
])

ch.scene("c11_02", bg="c11_fomo_noche", text="""
Ahu: Mañana empieza el 21.º Torneo. Si no te presentas, quizá te dejen en paz. Retírate. Por favor.
X lo mira con una expresión difícil de leer. Casi parece ternura.
""", ask="¿Cómo intenta convencerlo Ahu?", opts=[
    C("Insistir: 'Retírate del torneo'", "c11_03"),
    M("Hablarle de Smile", "c11_03", add={"rel_x": 1}),
    X("Cumplir la orden de la Comisión y atacarlo", "c11_bA1", flag="ahu_ataca", ending="E12"),
])

ch.scene("c11_03", bg="c11_fomo_ataque", text="""
Las ventanas estallan. Agentes de la Comisión y héroes de varias agencias entran por todas partes.
Rock investigó a X después de la muerte de Smile. Ahora todos saben quién es.
Agente: ¡X, quedas bajo custodia de la Comisión de Asuntos de Héroes!
""", ask="Eres X. ¿Qué haces?", opts=[
    C("Ponerte de pie y quitarte las gafas", "c11_f1"),
    M("Proteger a Ahu primero", "c11_f1", add={"rel_x": 1}),
])

ch.fight("c11_f1", "X contra la Comisión", a="X", b="Comisión", bg="c11_fomo_ataque", beats=[
    "Decenas de ataques al mismo tiempo: rayos, cuchillas, fuego, cadenas de fe.",
    "X levanta la mano. El espacio de la oficina se pliega como un origami.",
    "Los agentes caen unos sobre otros. Los héroes se quedan inmóviles en el aire.",
    "Un segundo. Todos en el suelo. Ni un solo papel del escritorio se ha movido.",
], next="c11_04")

ch.scene("c11_04", bg="fuera_del_tiempo", text="""
X toca la cabeza de Ahu. El mundo desaparece.
Están fuera del espacio y del tiempo, en el mismo lugar en el que empezó esta historia. Relojes que flotan. Ciudades como piezas de un tablero.
X: ¿Lo reconoces? Llevas mucho tiempo aquí, aunque no lo sabías.
La voz que te ha guiado en cada capítulo era la suya.
""", ask="¿Qué siente Ahu?", opts=[
    C("Miedo y asombro a la vez", "c11_05"),
    M("Ganas de ladrar", "c11_05"),
    M("Una calma extraña", "c11_05", add={"rel_x": 1}),
])

ch.scene("c11_05", bg="c11_tablero", text="""
X le muestra los hilos: un hombre común con un traje prestado, un relámpago fabricado, una niña con la suerte de cien desconocidos, una reina sin corona, una armadura de otro planeta, un padre sin voz, un niño y su monstruo, un dragón criado por el odio.
X: Los diez mejores son piezas de ajedrez que mueve el destino. Yo también lo soy.
""", ask="¿Qué hilo mira Ahu más tiempo?", opts=[
    C("Todos a la vez, sin entender", "c11_06"),
    M("El de Nice y el hombre de la caja de cartón", "c11_06"),
    M("El suyo propio, entrelazado con el de Xin Ya", "c11_06"),
])

ch.scene("c11_06", bg="c11_cero", text="""
X le muestra algo más: Cero, el héroe legendario.
X: No se convirtió en monstruo por accidente. Mató a propósito a los héroes que se oponían a su orden.
X: La Comisión inventó la versión oficial, 'la Caída', para controlar a la gente. Y Cero nunca murió de verdad. Su legado sigue vivo a través de Rock.
""", ask="¿Qué pregunta Ahu?", opts=[
    C("'¿Y tú qué eres, entonces?'", "c11_07"),
    M("'¿Rock es Cero?'", "c11_07"),
    M("'¿Por qué me lo cuentas a mí?'", "c11_07", add={"rel_x": 1}),
])

ch.scene("c11_07", bg="c11_tablero", text="""
X no responde directamente.
X: ¿Lo entiendes?
Ahu no lo entiende del todo. Es un perro que hace muy poco aprendió a hablar. Pero entiende que X está muy solo.
""", ask="¿Qué responde Ahu?", opts=[
    C("'No del todo'", "c11_08"),
    M("'Entiendo que estás solo'", "c11_08", add={"rel_x": 1}),
    M("Apoyar la cabeza en su pierna", "c11_08", add={"rel_x": 1}),
])

ch.scene("c11_08", bg="c11_azotea_noche", text="""
Vuelven al mundo, a una azotea. La de Smile. Es la noche antes del torneo.
Ahu: ¿Y ahora? Mañana van a estar todos allí. La Comisión, Rock, todos.
""", ask="¿Qué hace Ahu?", opts=[
    C("Esperar a que X decida", "c11_09"),
    M("Quedarse a dormir a su lado en la azotea", "c11_09", add={"rel_x": 1}),
    X("Suplicarle que desaparezca para siempre", "c11_bB1", flag="ahu_suplica", ending="E13"),
])

ch.scene("c11_09", bg="c11_ceremonia", text="""
La ceremonia de apertura del 21.º Torneo de Héroes. El estadio está lleno.
Entran los diez mejores. Queen, Lucky Cyan, Loli, los Johnnies, Ghostblade, Dragon Boy, Ahu...
Y Nice. Vivo. Con grietas que le recorren la piel como porcelana rota.
E-Soul también está, aunque ya no figura entre los diez.
""", ask="Desde el escenario, ¿qué hace Ahu?", opts=[
    C("Buscar a X entre el público", "c11_10"),
    M("Mirar a Nice, sin entender cómo está vivo", "c11_10"),
    M("Buscar a Xin Ya en las gradas", "c11_10"),
])

ch.scene("c11_10", bg="c11_ceremonia", text="""
Las luces se apagan. Se enciende un foco. Un hombre sube al escenario: sin traje, sin máscara, sin agencia.
De corbata. Con cara de cansancio. Un oficinista cualquiera.
Locutor: Es... es... ¡X!
""", ask="Eres X. Estás frente al mundo entero. ¿Qué haces?", opts=[
    C("Mostrarte tal como eres", "c11_fin"),
    M("Ajustarte la corbata y mostrarte tal como eres", "c11_fin"),
])

ch.end("c11_fin", "Fin del capítulo 11", """
X se presenta ante el mundo con su forma civil. Al mostrarse, deja de ser una pieza que la Comisión puede controlar.
""", bg="c11_ceremonia")

# ================= RAMA A: Ahu ataca a X =================
ch.scene("c11_bA1", bg="c11_fomo_noche", text="""
Ahu salta con los colmillos al aire. X no se mueve.
El mordisco nunca llega: Ahu aparece al otro lado de la oficina, sentado, sin saber cómo.
X: Está bien. Es tu trabajo.
""", ask="¿Qué hace Ahu?", opts=[
    M("Volver a atacar", "c11_bA2"),
    M("Quedarse quieto, avergonzado", "c11_bA2"),
])

ch.scene("c11_bA2", bg="c11_fomo_ataque", text="""
Los agentes de la Comisión entran por las ventanas. Ahu les abrió la puerta.
X se queda mirando a Ahu, no a los agentes.
""", ask="¿Qué le dice Ahu a X?", opts=[
    M("'Lo siento'", "c11_bA3"),
    M("Nada", "c11_bA3"),
])

ch.scene("c11_bA3", bg="c11_fomo_ataque", text="""
X: Que crean que ganaron. Será más fácil para todos.
Una explosión de luz. Cuando se apaga, en el escritorio solo quedan unas gafas y una corbata.
""", ask="¿Qué hace Ahu con la corbata?", opts=[
    M("Llevársela en la boca", "c11_bA4"),
    M("Dejarla donde está", "c11_bA4"),
])

ch.scene("c11_bA4", bg="c11_ceremonia", text="""
Al día siguiente, la Comisión anuncia la 'neutralización' de X. El 21.º Torneo empieza con el puesto número 1 vacío.
""", ask="Desde el escenario, ¿qué hace Ahu?", opts=[
    M("Mirar al cielo", "c11_bA_fin"),
    M("Bajar la cabeza", "c11_bA_fin"),
])

ch.end("c11_bA_fin", "Fin del capítulo 11 (hilo alterado)", """
X desaparece del tablero.
""", bg="c11_ceremonia", alt=True, set={"fin_x_ejecutado": True})

# ================= RAMA B: X se retira =================
ch.scene("c11_bB1", bg="c11_azotea_noche", text="""
Ahu: Desaparece. Sé un oficinista. Nadie tiene que saberlo. Yo guardaré el secreto.
X mira la ciudad mucho rato.
""", ask="¿Qué añade Ahu?", opts=[
    M("'Smile habría querido que vivieras'", "c11_bB2"),
    M("'No le debes nada a nadie'", "c11_bB2"),
])

ch.scene("c11_bB2", bg="c11_azotea_noche", text="""
X: ...Puede que tengas razón.
Saca el teléfono y envía un mensaje a la organización del torneo: 'X se retira'.
""", ask="¿Qué siente Ahu?", opts=[
    M("Alivio", "c11_bB3"),
    M("Una duda que no sabe explicar", "c11_bB3"),
])

ch.scene("c11_bB3", bg="c11_ceremonia", text="""
El torneo empieza sin X. Dragon Boy sonríe. Rock aplaude desde un palco.
La Comisión archiva la orden de ejecución.
""", ask="¿Qué hace Ahu durante la ceremonia?", opts=[
    M("Buscar a X entre el público, sin encontrarlo", "c11_bB4"),
    M("Mirar a Rock con desconfianza", "c11_bB4"),
])

ch.scene("c11_bB4", bg="c11_fomo_noche", text="""
El lunes, en FOMO, un oficinista de corbata llega a su escritorio a las nueve en punto. Saluda a Ahu con un gesto.
""", ask="¿Qué hace Ahu?", opts=[
    M("Devolverle el saludo moviendo la cola", "c11_bB_fin"),
    M("Dejarle medio bocadillo en la mesa", "c11_bB_fin"),
])

ch.end("c11_bB_fin", "Fin del capítulo 11 (hilo alterado)", """
X ya no es X. Es solo un hombre que trabaja en una oficina.
""", bg="c11_fomo_noche", alt=True, set={"fin_x_retirado": True})
