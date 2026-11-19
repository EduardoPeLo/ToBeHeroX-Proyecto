"""Capítulo 9: Dragon Boy (episodios 21-22)."""
from engine.model import Chapter, C, M, X

ALTERADO = "rock_expuesto|nice_rebelde|miedo_liberado"

ch = Chapter(9, "Dragon Boy", "Episodios 21-22", start="c9_00", color=(150, 40, 20), intro="""
Cuanto más lo hieren, más fuerte se hace. Un niño al que el mundo golpeó demasiado decide golpearlo de vuelta.
""")

ch.scene("c9_00", bg="fuera_del_tiempo", text="""
Voz: Este hilo es de color sangre. Y este otro... es el mío. Y el de mi único amigo.
""", next="c9_01", redirect=[(ALTERADO, "c9_bC0")])

# ---------------- EPISODIO 21: CRIAR A UN DIOS ----------------
ch.scene("c9_01", bg="c9_casa_dragon", text="""
Liang Long es un niño. Sus padres le gritan, le pegan, lo culpan de todo.
Madre de Dragon Boy: ¡Ojalá no hubieras nacido!
Cada golpe que recibe lo hace un poco más duro.
""", ask="¿Qué hace el pequeño Liang Long?", opts=[
    C("Aguantar sin llorar", "c9_02"),
    M("Esconderse en el armario", "c9_02"),
    M("Mirar a su madre con odio", "c9_02", add={"odio_dragon": 1}),
])

ch.scene("c9_02", bg="c9_callejon", text="""
Años después, Liang Long es un joven que odia al mundo. Su poder despierta: cuanto más lo hieren, más fuerte se vuelve.
Rock lo encuentra después de una pelea callejera, cubierto de sangre ajena.
Rock: Al mundo no le gustas. Pues haz que se arrodille.
""", ask="¿Qué le responde Liang Long?", opts=[
    C("'¿Cómo?'", "c9_03"),
    M("'¿Y tú qué ganas?'", "c9_03"),
    M("Escupirle a los pies... y seguirlo igualmente", "c9_03", add={"odio_dragon": 1}),
])

ch.scene("c9_03", bg="c9_rock_oficina", text="""
Rock le muestra una figura antigua: Cero, el héroe legendario que casi destruyó el mundo.
Rock: Si monopolizas la fe, serás un dios como él. Primer paso: entrar en el top 10. Para eso tienes que eliminar a Smile.
Smile fue el número 1. Ahora es un veterano querido por todos.
""", ask="¿Qué piensa Dragon Boy de la misión?", opts=[
    C("Que Smile es un escalón más", "c9_04"),
    M("Que le encantará borrar esa sonrisa", "c9_04", add={"odio_dragon": 1}),
    M("Que no le importa a quién tenga que vencer", "c9_04"),
])

ch.scene("c9_04", bg="c9_treeman", text="""
En TREEMAN, Shand le da a Nice una orden parecida: aprovechar la pelea entre Smile y Dragon Boy para subir en el ranking.
Nice se arregla los guantes. Una, dos, tres. Smile es su ídolo desde niño.
Shand: ¿Algún problema, Nice?
""", ask="¿Qué responde Nice?", opts=[
    C("'Ninguno, señor'", "c9_05"),
    M("'Ninguno...', con la voz rota", "c9_05", add={"culpa_nice": 1}),
    M("Asiente sin poder hablar", "c9_05", add={"culpa_nice": 1}),
])

ch.scene("c9_05", bg="c9_azotea_x", text="""
Una azotea cualquiera de la ciudad. Un oficinista de corbata come un bocadillo. Es X.
Smile se sienta a su lado. Son amigos desde hace mucho. Smile es su único amigo.
Smile: La Comisión dio la orden. Tu confianza es demasiado alta. Te quieren muerto.
""", ask="Eres X. ¿Qué le respondes a Smile?", opts=[
    C("'Ya pensaba retirarme del torneo'", "c9_06"),
    M("'Lo sé. Lo vi venir'", "c9_06"),
    M("Seguir comiendo el bocadillo, en silencio", "c9_06"),
])

ch.scene("c9_06", bg="c9_azotea_x", text="""
Smile: No te rindas solo por ellos. El mundo necesita a alguien como tú.
X: El mundo necesita dejar de necesitar a alguien como yo.
Smile se ríe. Se levanta para irse. Tiene asuntos pendientes.
""", ask="¿Qué le dices antes de que se vaya?", opts=[
    C("'Cuídate'", "c9_07"),
    M("'¿Quieres que te acompañe?'", "c9_07", set={"x_ofrecio": True}),
    M("Nada. Solo levantas la mano", "c9_07"),
])

ch.scene("c9_07", bg="c9_puerto", text="""
[x_ofrecio] Smile rechazó la compañía de X con una sonrisa: 'Esto lo tengo que hacer solo'.
En el puerto, Dragon Boy espera a Smile.
Dragon Boy: Tu hija... ¿Sabes quién la mató? Pregúntale a Rock.
La sonrisa de Smile desaparece.
""", ask="¿Cómo reacciona Smile?", opts=[
    C("Atacar a Dragon Boy", "c9_f1"),
    M("Exigir la verdad antes de atacar", "c9_f1"),
])

ch.fight("c9_f1", "Smile contra Dragon Boy", a="Smile", b="Dragon Boy", bg="c9_puerto", winner="none", beats=[
    "Smile, el veterano, golpea con una técnica impecable.",
    "Dragon Boy lo recibe todo de frente. Cada golpe lo hace más grande.",
    "Los contenedores del puerto vuelan por los aires.",
    "Ambos se detienen: alguien los observa desde un tejado.",
], next="c9_08")

ch.scene("c9_08", bg="c9_puerto", text="""
Es Nice, escondido, con una jeringa en el bolsillo. Lo han descubierto.
Dragon Boy: ¿Y tú quién eres?
""", ask="¿Qué hace Nice?", opts=[
    C("Bajar con su sonrisa perfecta", "c9_09"),
    M("Bajar sin sonreír", "c9_09", add={"culpa_nice": 1}),
])

# ---------------- EPISODIO 22: LA ÚLTIMA SONRISA ----------------
ch.scene("c9_09", bg="c9_puerto_noche", text="""
El auricular de Nice cruje con la voz de Shand.
Shand: Rock y su dragón van a por Smile. Cuando termine la pelea, inyecta miedo al ganador. Tú te llevarás la gloria.
""", ask="¿Qué hace Nice?", opts=[
    C("Esperar su momento", "c9_10"),
    M("Apretar la jeringa hasta que le duele la mano", "c9_10", add={"culpa_nice": 1}),
])

ch.scene("c9_10", bg="c9_puerto_noche", text="""
Dragon Boy, a propósito, deja una abertura: quiere que Nice ataque a Smile.
Smile mira a Nice. Lo reconoce: aquel niño que una vez le pidió un autógrafo.
Smile: Chico. Haz lo correcto.
""", ask="Nice tiene la jeringa en la mano. ¿Qué hace?", opts=[
    C("Inyectarle el miedo a Dragon Boy, no a Smile", "c9_11"),
    M("Dudar un segundo y luego inyectar a Dragon Boy", "c9_11", add={"culpa_nice": 1}),
    X("Tirar la jeringa al mar y advertir a Smile", "c9_bA1", flag="smile_vive", ending="E10"),
])

ch.scene("c9_11", bg="c9_puerto_noche", text="""
El miedo entra en Dragon Boy... y él lo devuelve. Su poder refleja el daño, duplicado, hacia Smile.
Smile se dobla. Sus ojos se vuelven negros. El héroe más querido se vuelve berserk.
Nice: No... no, no, no...
""", ask="¿Qué hace Nice?", opts=[
    C("Quedarse paralizado", "c9_f2"),
    M("Gritarle a Smile que resista", "c9_f2", add={"culpa_nice": 1}),
])

ch.fight("c9_f2", "Dragon Boy contra Smile berserk", a="Dragon Boy", b="Smile", bg="c9_puerto_noche", beats=[
    "Smile, consumido por el miedo, ataca a todo lo que se mueve.",
    "La multitud que llega al puerto grita: '¡Dragon Boy, sálvanos!'.",
    "La fe de los espectadores fluye hacia Dragon Boy. Se transforma en un dragón.",
    "Un último golpe. Smile cae y ya no se levanta.",
], next="c9_12")

ch.scene("c9_12", bg="c9_puerto_noche", text="""
Dragon Boy, transformado, se gira hacia Nice.
Dragon Boy: Gracias por la ayuda, héroe perfecto.
""", ask="¿Qué hace Nice?", opts=[
    C("Atacarlo, aunque sabe que no puede ganar", "c9_f3"),
    M("Atacarlo gritando el nombre de Smile", "c9_f3", add={"culpa_nice": 1}),
])

ch.fight("c9_f3", "Nice contra Dragon Boy", a="Nice", b="Dragon Boy", bg="c9_puerto_noche", winner="b", beats=[
    "Nice golpea con todo. Su técnica es perfecta.",
    "Cada golpe hace crecer al dragón.",
    "Nice sangra, se levanta y vuelve a golpear. Una, dos, tres veces.",
    "Dragon Boy alza la garra sobre él...",
], next="c9_13")

ch.scene("c9_13", bg="c9_oficina_fomo", text="""
En la oficina de FOMO, un oficinista levanta la vista de su pantalla. Siente algo: un hilo que se rompe.
Eres X. Le prometiste al mundo retirarte. Pero ese hilo era el de Smile.
""", ask="¿Qué haces?", opts=[
    C("Ir al puerto", "c9_f4"),
    M("Aflojarte la corbata e ir al puerto", "c9_f4"),
    X("Quedarte. Prometiste no intervenir", "c9_bB1", flag="dragon_dios", ending="E05"),
])

ch.fight("c9_f4", "X contra Dragon Boy", a="X", b="Dragon Boy", bg="c9_puerto_noche", beats=[
    "El espacio se dobla. X aparece entre la garra y Nice.",
    "Dragon Boy ruge y golpea con toda la fe del puerto.",
    "X no se mueve. El golpe llega a otro lugar del espacio.",
    "Un toque. El dragón vuelve a ser un joven tirado en el suelo.",
], next="c9_14")

ch.scene("c9_14", bg="c9_puerto_noche", text="""
X camina entre los escombros. Encuentra a Smile.
Ya no respira. Sigue teniendo una sonrisa pequeña en los labios.
""", ask="¿Qué haces, X?", opts=[
    C("Arrodillarte junto a él en silencio", "c9_15"),
    M("Cerrarle los ojos", "c9_15"),
    M("Quedarte de pie, sin poder moverte", "c9_15"),
])

ch.scene("c9_15", bg="c9_puerto_noche", text="""
Nice se derrumba de rodillas. Las manos le tiemblan. No consigue arreglarse los guantes.
Nice: Yo lo maté... Yo...
""", ask="¿Qué hace Nice?", opts=[
    C("Llorar sin control", "c9_16", add={"culpa_nice": 1}),
    M("Arrancarse los guantes", "c9_16", add={"culpa_nice": 1}),
])

ch.scene("c9_16", bg="c9_rock_oficina", text="""
Rock lo vio todo a través de una cámara. Vio a X llegar en un instante. Vio cómo miraba a Smile.
Rock: Así que eran amigos... Entonces X tiene un rostro, una vida, una dirección.
""", ask="¿Qué decide Rock?", opts=[
    C("Investigar la identidad de X", "c9_fin"),
    M("Investigar a X y felicitar a Dragon Boy", "c9_fin"),
])

ch.end("c9_fin", "Fin del capítulo 9", """
Smile muere. Dragon Boy entra en el top 10 y llega al número 3. Nice se rompe por dentro.
Rock empieza a investigar a X. La Comisión también.
Voz: Mi único amigo. Lo vi todo desde fuera del tiempo y aun así llegué tarde. Eso también forma parte del tablero.
""", bg="c9_rock_oficina")

# ================= RAMA A: Smile vive =================
ch.scene("c9_bA1", bg="c9_puerto_noche", text="""
La jeringa cae al agua con un plop ridículo.
Nice: ¡Smile! ¡Es una trampa! ¡Shand y Rock quieren que mueras!
Shand grita en su auricular. Nice se lo arranca.
""", ask="Dragon Boy se lanza contra los dos. ¿Qué hace Nice?", opts=[
    M("Pelear junto a Smile", "c9_bA2"),
    M("Proteger a los civiles mientras Smile pelea", "c9_bA2", add={"culpa_nice": -1}),
])

ch.scene("c9_bA2", bg="c9_puerto_noche", text="""
Smile: Sus golpes lo hacen más fuerte. No le pegues: cánsalo.
Smile y Nice esquivan, giran, hacen que Dragon Boy golpee el vacío.
""", ask="¿Cuál es el plan de Nice?", opts=[
    M("Llevarlo hacia el agua", "c9_bA3"),
    M("Hacerlo enfadar hasta que pierda el control", "c9_bA3"),
])

ch.scene("c9_bA3", bg="c9_puerto_noche", text="""
Dragon Boy, furioso, se agota. Sin heridas, su poder no crece.
Aparece la multitud. Esta vez no gritan su nombre: gritan '¡Smile!' y '¡Nice!'.
""", ask="¿Cómo terminan la pelea?", opts=[
    M("Inmovilizándolo entre los dos", "c9_bA4"),
    M("Dejando que Smile hable con él", "c9_bA4"),
])

ch.scene("c9_bA4", bg="c9_puerto_noche", text="""
Smile: Rock también te está usando, chico. Igual que a mí me quitó a mi hija.
Dragon Boy duda por primera vez. Luego huye en la oscuridad.
""", ask="¿Lo persiguen?", opts=[
    M("No. Smile está herido", "c9_bA5"),
    M("No. Ya ha perdido suficiente", "c9_bA5"),
])

ch.scene("c9_bA5", bg="c9_azotea_x", text="""
Esa noche, X encuentra a Smile en la azotea de siempre, con vendas y su sonrisa de siempre.
Smile: Me salvó un chico que se arregla los guantes tres veces.
""", ask="Eres X. ¿Qué le dices?", opts=[
    M("'Me alegro de que sigas aquí'", "c9_bA6"),
    M("Le ofreces la mitad de tu bocadillo", "c9_bA6"),
])

ch.scene("c9_bA6", bg="c9_treeman", text="""
Nice entra en el despacho de Shand y deja su placa sobre la mesa.
Shand: Sin mí no eres nada. Tu confianza es mía.
""", ask="¿Qué responde Nice?", opts=[
    M("'Entonces quédatela'", "c9_bA7"),
    M("Se arregla los guantes una sola vez y se va", "c9_bA7", add={"culpa_nice": -1}),
])

ch.scene("c9_bA7", bg="c9_azotea_x", text="""
Los tres comparten la azotea una tarde: el veterano, el chico perfecto que dejó de serlo y el oficinista.
Smile: La Comisión sigue queriendo tu cabeza.
""", ask="¿Qué responde X?", opts=[
    M("'Ahora tengo quien me cuide la espalda'", "c9_bA_fin"),
    M("'Que vengan'", "c9_bA_fin"),
])

ch.end("c9_bA_fin", "Fin del capítulo 9 (hilo alterado)", """
Smile sobrevive. Dragon Boy no entra en el top 10. Nice deja TREEMAN y nunca llegará a aquella azotea donde debía saltar.
Voz: Mi único amigo sigue vivo. No sé si me lo merezco. Pero lo acepto.
""", bg="c9_azotea_x", alt=True, set={"smile_vivo": True, "nice_rebelde": True})

# ================= RAMA B: X no interviene =================
ch.scene("c9_bB1", bg="c9_oficina_fomo", text="""
X vuelve a mirar la pantalla. Termina el informe. Lo envía.
Muy lejos, un hilo termina de romperse.
""", ask="¿Qué siente X?", opts=[
    M("Nada que pueda nombrar", "c9_bB2"),
    M("Que acaba de perder algo enorme", "c9_bB2"),
])

ch.scene("c9_bB2", bg="c9_puerto_noche", text="""
En el puerto, la garra cae. Nice consigue apartarse en el último segundo y huye, malherido.
Dragon Boy ruge. Absorbe la confianza que la gente tenía en Smile.
""", ask="¿Qué hace Nice mientras huye?", opts=[
    M("Mirar atrás una última vez", "c9_bB3"),
    M("No mirar atrás", "c9_bB3"),
])

ch.scene("c9_bB3", bg="c9_noticias", text="""
'¡Dragon Boy salva el puerto de un Smile enloquecido!' La fe de la ciudad se vuelca en él.
Rock lo presenta ante las cámaras.
Rock: El mundo tiene un nuevo protector.
""", ask="¿Qué hace Dragon Boy ante las cámaras?", opts=[
    M("Sonreír", "c9_bB4"),
    M("Mirar a la cámara con odio", "c9_bB4", add={"odio_dragon": 1}),
])

ch.scene("c9_bB4", bg="c9_ciudad_dragon", text="""
Semanas de misiones fabricadas. Villanos de Spotlight que caen ante él. Su confianza crece y crece.
Su cuerpo ya no vuelve a ser humano. Es un dragón todo el tiempo.
""", ask="¿Qué queda de Liang Long?", opts=[
    M("El niño del armario", "c9_bB5"),
    M("Nada", "c9_bB5"),
])

ch.scene("c9_bB5", bg="c9_comision", text="""
La Comisión de Asuntos de Héroes convoca a Dragon Boy. Quiere controlarlo.
Dragon Boy los mira desde arriba.
Dragon Boy: Ustedes ya no deciden nada.
""", ask="¿Qué hace la Comisión?", opts=[
    M("Arrodillarse", "c9_bB6"),
    M("Pedirle a X que lo detenga", "c9_bB6"),
])

ch.scene("c9_bB6", bg="c9_azotea_x", text="""
X está en la azotea, solo. Ya no hay nadie que se siente a su lado.
La pulsera de Dragon Boy supera a la suya.
""", ask="¿Qué hace X?", opts=[
    M("Retirarse del ranking", "c9_bB7"),
    M("Mirar la ciudad sin hacer nada", "c9_bB7"),
])

ch.scene("c9_bB7", bg="c9_ciudad_dragon", text="""
Rock levanta una estatua: un dragón enroscado sobre la figura de Cero.
Rock: Por fin.
""", ask="¿Qué piensa la gente?", opts=[
    M("Que por fin hay un dios que los protege", "c9_bB_fin"),
    M("Que tiene miedo, pero no puede decirlo", "c9_bB_fin"),
])

ch.end("c9_bB_fin", "Fin del capítulo 9 (hilo alterado)", """
Dragon Boy se convierte en el número 1. La fe del mundo se concentra en una sola criatura.
Voz: Le dejé el tablero a quien quería romperlo. Rock ha ganado.
""", bg="c9_ciudad_dragon", alt=True, set={"dragon_ascendido": True})

# ================= RUTA C: Hilo ya alterado =================
ch.scene("c9_bC0", bg="fuera_del_tiempo", text="""
Voz: El dragón despierta en un tablero que ya no es el original.
""", next="c9_bC1")

ch.scene("c9_bC1", bg="c9_casa_dragon", text="""
Liang Long creció entre golpes. Cada golpe lo hizo más fuerte.
[rock_expuesto] Rock, desde la cárcel, le escribe cartas. Le promete un trono si consigue lo que él no pudo.
[!rock_expuesto] Rock lo recluta y le muestra la figura de Cero.
[miedo_liberado] Afuera, la ciudad está cubierta por la ola de miedo de las Ruinas. Es el mejor momento para presentarse como salvador.
""", ask="¿Qué decide Dragon Boy?", opts=[
    M("Ir a por Smile, como le dijeron", "c9_bC2"),
    M("Ir a por Smile por su cuenta", "c9_bC2", add={"odio_dragon": 1}),
])

ch.scene("c9_bC2", bg="c9_azotea_x", text="""
Smile visita a X en la azotea. La Comisión lo quiere muerto.
X: Ya pensaba retirarme del torneo.
[nice_rebelde] Smile: Por cierto, ese chico, Nice, dejó TREEMAN. Dicen que se negó a cumplir una orden.
""", ask="¿Qué le dice X a Smile cuando se va?", opts=[
    M("'Cuídate'", "c9_bC3"),
    M("'¿Quieres que te acompañe?'", "c9_bC3", set={"x_ofrecio": True}),
])

ch.scene("c9_bC3", bg="c9_puerto_noche", text="""
Dragon Boy provoca a Smile en el puerto. Pelean.
[nice_rebelde] Nadie espía desde los tejados. No hay ninguna jeringa de miedo. Solo dos hombres y una mentira sobre una hija muerta.
[!nice_rebelde] Nice observa la pelea desde un tejado, con una jeringa en el bolsillo.
""", ask="¿Cómo sigue la pelea?", opts=[
    M("Smile resiste con su técnica de veterano", "c9_bC4"),
    M("Dragon Boy recibe golpes a propósito para crecer", "c9_bC4"),
])

ch.scene("c9_bC4", bg="c9_puerto_noche", text="""
[nice_rebelde] Sin el miedo, Smile no se vuelve berserk. Pero Dragon Boy sigue creciendo. Smile cae, agotado.
[!nice_rebelde] Nice inyecta el miedo. Dragon Boy lo refleja hacia Smile, que se vuelve berserk.
[x_ofrecio] X ya estaba en camino.
X llega y detiene al dragón con un toque.
""", ask="¿Sobrevive Smile?", opts=[
    M("X llega justo a tiempo... o eso parece", "c9_bC5"),
    M("X llega tarde", "c9_bC5"),
])

ch.scene("c9_bC5", bg="c9_puerto_noche", text="""
[nice_rebelde] Smile sobrevive, malherido. Sin el miedo de por medio, su cuerpo aguanta.
[!nice_rebelde] Smile muere con una sonrisa pequeña en los labios.
X se queda mirando a su amigo durante mucho tiempo.
""", ask="¿Qué hace X?", opts=[
    M("Llevarse a Smile en brazos", "c9_bC6"),
    M("Quedarse quieto", "c9_bC6"),
])

ch.scene("c9_bC6", bg="c9_rock_oficina", text="""
[rock_expuesto] Desde su celda, Rock ve las noticias. Sonríe: ahora sabe que X tiene un amigo.
[!rock_expuesto] Rock lo ve todo por cámara. Ahora sabe que X tiene un amigo.
""", ask="¿Qué hace Rock?", opts=[
    M("Investigar la identidad de X", "c9_bC_fin"),
    M("Esperar", "c9_bC_fin"),
])

ch.end("c9_bC_fin", "Fin del capítulo 9 (hilo alterado)", """
El dragón despertó, pero el puerto no fue el mismo de la historia original.
[nice_rebelde] Smile sigue vivo, por poco.
Voz: Incluso con los hilos movidos, alguien acabó descubriendo quién soy.
""", bg="c9_rock_oficina", alt=True)
