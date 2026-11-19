"""Capítulo 6: Ghostblade (episodios 15-16)."""
from engine.model import Chapter, C, M, X

ch = Chapter(6, "Ghostblade", "Episodios 15-16", start="c6_00", color=(50, 50, 60), intro="""
El público decidió que su silencio era 'genial'. Y la confianza le quitó la voz para siempre.
""")

ch.scene("c6_00", bg="fuera_del_tiempo", text="""
Voz: Un hilo gris, casi invisible. Corta a otros hilos sin hacer ruido.
Voz: Este hombre no puede hablar. Así que tendrás que escuchar lo que hace.
""", next="c6_01")

# ---------------- EPISODIO 15: TRASTORNO AFECTIVO ----------------
ch.scene("c6_01", bg="c6_escuela", text="""
Wang Yi siempre fue antisocial. En clase no hablaba con nadie y comía solo en la azotea.
Unos compañeros se acercan a burlarse de él.
""", ask="¿Qué hace Wang Yi?", opts=[
    C("Mirarlos fijamente sin decir nada", "c6_02"),
    M("Levantarse e irse", "c6_02"),
    M("Murmurar 'déjenme en paz'", "c6_02", add={"voz": 1}),
])

ch.scene("c6_02", bg="c6_ciudad", text="""
Años después, un video de él deteniendo a un ladrón sin pronunciar palabra se hace viral. La gente lo adora: 'Qué genial, ni siquiera habla'.
La confianza lo convierte en lo que creen que es. Un día intenta hablar... y no sale nada.
""", ask="Wang Yi descubre que está mudo. ¿Cómo reacciona?", opts=[
    C("Aceptarlo en silencio", "c6_03"),
    M("Intentar gritar una y otra vez", "c6_03", add={"voz": 1}),
    M("Escribir en un papel: '¿por qué?'", "c6_03"),
])

ch.scene("c6_03", bg="c6_mighty_glory", text="""
[!rock_expuesto] Rock, director de Mighty Glory, le ofrece un trabajo especial: cazar a héroes que se han vuelto rebeldes.
[rock_expuesto] Hace años, mucho antes de que Rock acabara entre rejas, le ofreció un trabajo especial: cazar a héroes que se habían vuelto rebeldes.
Rock: Eres perfecto, Wang Yi. Los muertos no hablan... y tú tampoco.
""", ask="¿Acepta ser el asesino de Mighty Glory?", opts=[
    C("Asentir", "c6_04"),
    M("Asentir y apretar la empuñadura de la espada", "c6_04"),
    M("Dudar mucho antes de asentir", "c6_04", add={"conciencia": 1}),
])

ch.scene("c6_04", bg="c6_noche_lluvia", text="""
Su primera misión: un héroe rebelde que extorsionaba a un barrio. Ghostblade lo encuentra en un tejado bajo la lluvia.
""", ask="¿Cómo cumple su misión?", opts=[
    C("Un solo corte, rápido y limpio", "c6_05"),
    M("Dejar que su objetivo vea quién lo mata", "c6_05"),
    M("Asegurarse primero de que de verdad es culpable", "c6_05", add={"conciencia": 1}),
])

ch.scene("c6_05", bg="c6_puente", text="""
Durante una misión, una mujer queda atrapada en el fuego cruzado. Se llama Zhang Lan. Ghostblade la saca de allí en brazos.
Zhang Lan: No dices nada... pero tienes ojos tristes.
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Dejarla a salvo e irse", "c6_06"),
    M("Escribirle su nombre en un papel", "c6_06", add={"rel_lan": 1}),
    M("Quedarse a su lado hasta que llegue la ambulancia", "c6_06", add={"rel_lan": 1}),
])

ch.scene("c6_06", bg="c6_boda", text="""
Zhang Lan lo encuentra después. Con el tiempo, se casan. Nace una niña: Nuonuo.
Por primera vez, Wang Yi sonríe.
""", ask="Sostiene a su hija recién nacida. ¿Qué hace?", opts=[
    C("Mirarla en silencio durante horas", "c6_07"),
    M("Intentar decir su nombre, sin voz", "c6_07", add={"voz": 1}),
    M("Prometerse que la protegerá de todo", "c6_07", add={"rel_nuonuo": 1}),
])

ch.scene("c6_07", bg="c6_casa", text="""
Pero las misiones no se detienen. Llega a casa con sangre en el abrigo, a deshoras, sin explicaciones.
Zhang Lan: No puedo criarla con un fantasma, Wang Yi. O te quedas, o nos vamos.
""", ask="¿Qué elige?", opts=[
    C("Bajar la mirada. No puede dejar Mighty Glory", "c6_08", add={"rel_lan": -1}),
    M("Escribir 'lo siento' y salir a otra misión", "c6_08", add={"rel_lan": -1}),
    X("Romper su placa de Mighty Glory delante de ella", "c6_bA1", flag="ghost_padre", ending="E09"),
])

ch.scene("c6_08", bg="c6_calle_noche", text="""
Zhang Lan se divorcia de él y se lleva a la niña. Wang Yi no puede acercarse.
Así que la vigila desde lejos durante años, entre las sombras, como un fantasma. Desde fuera, parece un acosador.
[vio_mirada] Una justiciera con armadura lo confundió una vez con un criminal y lo persiguió por un callejón.
""", ask="Una noche, Nuonuo lo descubre siguiéndola. ¿Qué hace Ghostblade?", opts=[
    C("Desaparecer de un salto", "c6_09"),
    M("Dejarle una flor en el buzón antes de irse", "c6_09", add={"rel_nuonuo": 1}),
    M("Quedarse quieto un segundo de más", "c6_09"),
])

ch.scene("c6_09", bg="c6_mighty_glory", text="""
Se organiza una expedición secreta al ovni estrellado. Nuonuo va a formar parte del equipo.
[ovni_publico] Desde que se filtraron los datos, la expedición es pública, y está llena de cámaras.
Ghostblade se presenta voluntario como seguridad.
""", ask="¿Por qué se ofrece voluntario?", opts=[
    C("Para proteger a Nuonuo", "c6_10", add={"rel_nuonuo": 1}),
    M("Porque Rock se lo ordena, y le viene bien", "c6_10"),
    M("Para estar cerca de ella, aunque sea una vez", "c6_10", add={"rel_nuonuo": 1}),
])

# ---------------- EPISODIO 16: LA CURA ----------------
ch.scene("c6_10", bg="c6_campamento", text="""
El campamento junto al ovni.
[!loli_retirada] Allí están Ghostblade, Nuonuo, Loli, su padre y los Johnnies, un niño con un monstruo como mascota.
[loli_retirada] Allí están Ghostblade, Nuonuo, un equipo de científicos de la Comisión y los Johnnies, un niño con un monstruo como mascota.
Nuonuo le ofrece un plato de sopa.
Nuonuo: Toma. No hablas mucho, ¿eh?
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Aceptar la sopa sin mirarla", "c6_11"),
    M("Aceptarla y asentir como un 'gracias'", "c6_11", add={"rel_nuonuo": 1}),
    M("Rechazarla para no delatarse", "c6_11"),
], redirect=[])

ch.scene("c6_11", bg="c6_campamento", text="""
[!loli_retirada] Loli lo observa. Reconoce su forma de moverse: es el encapuchado que perseguía a Nuonuo.
[!loli_retirada] Loli: Tú eras el acosador. Aléjate de ella.
[loli_retirada] Uno de los científicos lo señala en voz baja: alguien lo ha visto siguiendo a Nuonuo por la ciudad.
La tensión en el campamento se puede cortar con un cuchillo.
""", ask="¿Cómo responde Ghostblade a la acusación?", opts=[
    C("No defenderse; alejarse del grupo", "c6_12"),
    M("Escribir 'no es lo que parece'", "c6_12", add={"voz": 1}),
    M("Mirar a Nuonuo, que no entiende nada", "c6_12"),
])

ch.scene("c6_12", bg="c6_bosque_noche", text="""
De noche, todos en el campamento están raros: lloran, discuten, tienen pesadillas.
Ghostblade ve una silueta entre los árboles: DJ Shindig, lleno de miedo, alimentándose de las emociones del grupo.
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Ir solo a por él", "c6_f1"),
    M("Dejar una nota de aviso y luego ir", "c6_f1"),
])

ch.fight("c6_f1", "Ghostblade contra DJ Shindig", a="Ghostblade", b="DJ Shindig", bg="c6_bosque_noche", beats=[
    "Shindig suelta una ola de miedo con su música. Los árboles se marchitan.",
    "Ghostblade no oye la música. No hay nada dentro de él que el miedo pueda tocar... o eso cree.",
    "Un paso, un destello.",
    "Shindig cae partido en dos antes de terminar su canción.",
], next="c6_13")

ch.scene("c6_13", bg="c6_bosque_noche", text="""
La sangre de Shindig humea: es miedo puro. Una parte le salpicó la mano.
Ghostblade siente algo extraño en el pecho. Una voz que no es suya le susurra.
""", ask="El miedo intenta entrar. ¿Qué hace?", opts=[
    C("Limpiarse la mano y volver en silencio", "c6_14"),
    M("Clavar la espada en el suelo y respirar hasta calmarse", "c6_14", add={"conciencia": 1}),
    X("Dejar que el miedo lo llene", "c6_bB1", flag="ghost_infectado", ending="E06"),
])

ch.scene("c6_14", bg="c6_campamento", text="""
Mientras él no está, Nuonuo encuentra en su mochila un cuaderno viejo. Lo abre.
Fotos de ella de pequeña. Dibujos de ella en el parque. Fechas de cumpleaños con una frase: 'Hoy tampoco me acerqué'.
""", ask="Ghostblade vuelve y la ve con el cuaderno. ¿Qué hace?", opts=[
    C("Quedarse inmóvil en la entrada de la tienda", "c6_15"),
    M("Extender la mano para pedirle el cuaderno", "c6_15"),
    M("Dar media vuelta para irse", "c6_15"),
])

ch.scene("c6_15", bg="c6_campamento", text="""
Nuonuo: Tú... eres mi padre.
No es una pregunta.
[rel_nuonuo>3] Nuonuo: Me dejabas flores en el buzón. Siempre supe que alguien me cuidaba.
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Asentir una sola vez", "c6_16", add={"rel_nuonuo": 1}),
    M("Escribir en la última página: 'Perdón'", "c6_16", add={"rel_nuonuo": 2}),
    M("No reaccionar, aunque le tiemblan las manos", "c6_16"),
])

ch.scene("c6_16", bg="c6_campamento_amanecer", text="""
Al amanecer, un grito: los Johnnies han desaparecido. Sus huellas van hacia el ovni.
[!loli_retirada] Loli: ¿Y ahora qué?
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Tomar la espada y seguir las huellas", "c6_fin"),
    M("Mirar a Nuonuo antes de irse", "c6_fin", add={"rel_nuonuo": 1}),
])

ch.end("c6_fin", "Fin del capítulo 6", """
Ghostblade se adentra hacia el ovni. Lleva una orden secreta que nadie más conoce.
Nuonuo lo mira desde el campamento con el cuaderno apretado contra el pecho.
Voz: Un padre sin voz y una hija que acaba de encontrarlo. Este hilo está a punto de cruzarse con el de un niño que busca al asesino de su padre.
""", bg="c6_campamento_amanecer")

# ================= RAMA A: Ghostblade deja Mighty Glory =================
ch.scene("c6_bA1", bg="c6_casa", text="""
El crujido de la placa al romperse suena más fuerte que cualquier palabra.
Zhang Lan lo mira, incrédula.
Zhang Lan: ¿De verdad?
""", ask="¿Cómo se lo demuestra?", opts=[
    M("Quedarse en casa esa noche y la siguiente", "c6_bA2", add={"rel_lan": 1}),
    M("Dejar la espada en el armario, envuelta", "c6_bA2", set={"espada_guardada": True}),
])

ch.scene("c6_bA2", bg="c6_mighty_glory", text="""
[!rock_expuesto] Rock no acepta renuncias. Envía a tres asesinos para dejar claro que nadie sale de Mighty Glory.
[rock_expuesto] Aunque Rock ya no tiene poder, sus antiguos hombres no aceptan renuncias.
""", ask="Tres sombras rodean la casa. ¿Qué hace Ghostblade?", opts=[
    M("Salir a enfrentarlos lejos de su familia", "c6_bA3"),
    M("Sacar a Lan y a Nuonuo por la ventana primero", "c6_bA3", add={"rel_lan": 1}),
])

ch.scene("c6_bA3", bg="c6_noche_lluvia", text="""
Es la pelea más difícil de su vida, porque por primera vez tiene algo que perder.
Cuando termina, está herido, pero vivo. Los asesinos no volverán.
""", ask="¿Qué hace después?", opts=[
    M("Volver a casa sangrando", "c6_bA4"),
    M("Curarse solo antes de que lo vea su hija", "c6_bA4"),
])

ch.scene("c6_bA4", bg="c6_casa", text="""
Los años pasan. Wang Yi aprende a ser padre sin voz: notas en la nevera, dibujos, gestos.
Nuonuo crece sabiendo exactamente quién es su padre.
Nuonuo: Papá, ¿por qué no hablas?
""", ask="¿Cómo se lo explica?", opts=[
    M("Escribiéndole un cuento", "c6_bA5", add={"rel_nuonuo": 2}),
    M("Haciéndole una mueca que la hace reír", "c6_bA5", add={"rel_nuonuo": 1}),
])

ch.scene("c6_bA5", bg="c6_ciudad", text="""
Ya no hay misiones. Su confianza pública cae, la gente lo olvida. Eso le da igual.
Un día, Nuonuo vuelve del laboratorio emocionada: la han invitado a una expedición a un ovni.
""", ask="¿Qué hace Wang Yi?", opts=[
    M("Prohibírselo, con una nota en mayúsculas", "c6_bA6"),
    M("Pedirle que lo deje ir como guardaespaldas", "c6_bA6"),
])

ch.scene("c6_bA6", bg="c6_casa", text="""
Nuonuo: Papá, no voy a ser una niña toda la vida.
Zhang Lan les sirve la cena a los dos.
Zhang Lan: Confía en ella. Como yo aprendí a confiar en ti.
""", ask="¿Qué decide?", opts=[
    M("Dejarla ir sola", "c6_bA7"),
    M("Dejarla ir, pero enseñarle a defenderse", "c6_bA7", add={"rel_nuonuo": 1}),
])

ch.scene("c6_bA7", bg="c6_casa", text="""
La noche antes de la partida, Wang Yi desenvuelve la vieja espada y la mira largo rato.
""", ask="¿Qué hace con ella?", opts=[
    M("Volver a guardarla", "c6_bA_fin"),
    M("Dársela a Nuonuo envuelta en un pañuelo", "c6_bA_fin", set={"nuonuo_espada": True}),
])

ch.end("c6_bA_fin", "Fin del capítulo 6 (hilo alterado)", """
Ghostblade no existe en el ranking. Wang Yi es un padre mudo que hace la mejor sopa del barrio.
Sin su espada en Mighty Glory, alguien más tendrá que hacer el trabajo sucio. Y algunos trabajos sucios ya estaban hechos.
Voz: Un hombre que eligió a su familia. Los hilos a su alrededor no saben dónde agarrarse.
""", bg="c6_casa", alt=True, set={"ghost_retirado": True})

# ================= RAMA B: El miedo llena a Ghostblade =================
ch.scene("c6_bB1", bg="c6_bosque_noche", text="""
Deja de resistirse. El miedo entra como agua helada en un vaso vacío.
Por primera vez en años oye algo dentro de su cabeza: miles de voces gritando.
""", ask="¿Qué hace?", opts=[
    M("Volver al campamento", "c6_bB2"),
    M("Alejarse más en el bosque", "c6_bB2", add={"conciencia": 1}),
])

ch.scene("c6_bB2", bg="c6_bosque_noche", text="""
Sus ojos se vuelven negros. Su espada corta árboles sin que él se lo proponga.
En la distancia, la luz del campamento. Nuonuo está allí.
""", ask="¿Qué queda de Wang Yi?", opts=[
    M("Solo el instinto de proteger a Nuonuo", "c6_bB3", add={"rel_nuonuo": 1}),
    M("Casi nada", "c6_bB3"),
])

ch.scene("c6_bB3", bg="c6_campamento", text="""
Llega al borde del campamento. Nuonuo sale de la tienda con una linterna.
Nuonuo: ¿Hola? ¿Eres tú, el callado?
""", ask="¿Qué hace Ghostblade?", opts=[
    M("Huir antes de hacerle daño", "c6_bB4"),
    M("Quedarse quieto, luchando contra sí mismo", "c6_bB4", add={"conciencia": 1}),
])

ch.scene("c6_bB4", bg="c6_bosque_noche", text="""
Se clava su propia espada en el muslo para no avanzar. El dolor le da un segundo de claridad. Corre hacia el ovni, lejos de todos.
""", ask="Escribe algo en un árbol con la espada. ¿Qué?", opts=[
    M("'No me busquen'", "c6_bB5"),
    M("'Nuonuo, perdón'", "c6_bB5", add={"rel_nuonuo": 1}),
])

ch.scene("c6_bB5", bg="c6_ovni_exterior", text="""
Los Johnnies lo encuentran cerca del ovni. Big Johnny gruñe: siente algo conocido en él.
Little Johnny: Ese corte en los árboles... lo he visto antes. Lo vi en mi casa, el día en que mataron a mi padre.
""", ask="¿Qué hace Ghostblade, consumido por el miedo?", opts=[
    M("Atacar", "c6_bB6"),
    M("Arrodillarse y ofrecer la espada", "c6_bB6", add={"conciencia": 1}),
])

ch.scene("c6_bB6", bg="c6_ovni_exterior", text="""
Big Johnny se transforma. El choque destroza el bosque.
Cuando el polvo se asienta, Ghostblade ha desaparecido en el interior del ovni, dejando un rastro de miedo negro.
""", ask="¿Qué le grita Little Johnny?", opts=[
    M("'¡Vuelve, asesino!'", "c6_bB7"),
    M("Nada. Solo llora de rabia", "c6_bB7"),
])

ch.scene("c6_bB7", bg="c6_campamento_amanecer", text="""
Al amanecer, Nuonuo encuentra el cuaderno en una mochila abandonada. Fotos de ella. Fechas de cumpleaños.
Nuonuo: Papá...
""", ask="¿Qué hace Nuonuo?", opts=[
    M("Guardar el cuaderno y esperar", "c6_bB_fin"),
    M("Ir hacia el ovni a buscarlo", "c6_bB_fin"),
])

ch.end("c6_bB_fin", "Fin del capítulo 6 (hilo alterado)", """
Ghostblade, el número 4, desaparece en el ovni convertido en una criatura de miedo.
Voz: El hombre sin voz por fin oye algo, y es lo peor que podía oír.
""", bg="c6_ovni_exterior", alt=True, set={"ghost_berserk": True})
