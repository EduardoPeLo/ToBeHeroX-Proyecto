"""Capítulo 10: Ahu (episodio 23)."""
from engine.model import Chapter, C, M, X

ALTERADO = "nice_rebelde|dragon_ascendido|miedo_liberado|smile_vivo"

ch = Chapter(10, "Ahu", "Episodio 23", start="c10_00", color=(170, 130, 70), intro="""
Un perro de circo que odiaba a los niños. Una niña que creyó en él. Y una mentira que lo convirtió en héroe.
""")

ch.scene("c10_00", bg="fuera_del_tiempo", text="""
Voz: El último hilo antes del mío. Es de un perro con la piel arrugada.
Voz: Él será quien me encuentre.
""", next="c10_01", redirect=[(ALTERADO, "c10_bC0")])

# ---------------- EPISODIO 23: MENTIRA ----------------
ch.scene("c10_01", bg="c10_circo", text="""
Ahu es un shar pei en un circo ambulante. Lo obligan a saltar aros de fuego, a hacer equilibrio sobre pelotas, a sonreír para el público.
Cirquero: ¡Otra vez! ¡Y más alto!
""", ask="Ahu está agotado. ¿Qué hace?", opts=[
    C("Saltar otra vez", "c10_02"),
    M("Gruñir... y saltar igualmente", "c10_02", add={"orgullo": 1}),
    M("Fingir que tropieza para descansar", "c10_02"),
])

ch.scene("c10_02", bg="c10_circo", text="""
Después de cada función, los niños del público corren a tirarle de las arrugas.
Ahu odia a los niños. Los odia con todo su corazón de perro.
""", ask="Un niño le tira de la oreja. ¿Qué hace Ahu?", opts=[
    C("Mostrarle los dientes", "c10_03"),
    M("Alejarse con dignidad", "c10_03", add={"orgullo": 1}),
    M("Ladrar tan fuerte que el niño se cae de culo", "c10_03"),
])

ch.scene("c10_03", bg="c10_casa_xinya", text="""
El circo cierra. Una chica llamada Xin Ya, que lo había visto actuar muchas veces, lo adopta.
Xin Ya: ¡Ahu! ¡Ahora vives conmigo!
Lo abraza demasiado fuerte. Igual que un niño.
""", ask="¿Cómo recibe Ahu a Xin Ya?", opts=[
    C("Con desconfianza", "c10_04"),
    M("Aceptando el abrazo con resignación", "c10_04", add={"rel_xinya": 1}),
    M("Lamiéndole la cara una sola vez", "c10_04", add={"rel_xinya": 2}),
])

ch.scene("c10_04", bg="c10_barrio", text="""
El barrio de Xin Ya está en peligro: TREEMAN quiere sus tierras para construir.
Xin Ya: ¡Tú puedes ser un héroe, Ahu! Si la gente cree en ti, ¡podrás salvarnos!
""", ask="¿Qué hace Ahu ante esa idea absurda?", opts=[
    C("Bostezar", "c10_05"),
    M("Mirarla como si estuviera loca", "c10_05"),
    M("Mover la cola, aunque no quería", "c10_05", add={"rel_xinya": 1}),
])

ch.scene("c10_05", bg="c10_barrio", text="""
Unos matones de TREEMAN vienen a amenazar a los vecinos. Ahu, irritado por el ruido, les ladra y les muerde un tobillo.
Los matones huyen. Los vecinos aplauden. La fe en el perro empieza a crecer.
""", ask="Los vecinos lo vitorean. ¿Qué hace Ahu?", opts=[
    C("Volver a su cesta como si nada", "c10_06"),
    M("Levantar el hocico, orgulloso", "c10_06", add={"orgullo": 1}),
    M("Ponerse junto a Xin Ya", "c10_06", add={"rel_xinya": 1}),
])

ch.scene("c10_06", bg="c10_plaza_barrio", text="""
TREEMAN cambia de táctica. Envía a Nice, el héroe perfecto, para convencer a los vecinos con su sonrisa.
Nice: Firmen aquí. Les prometo un barrio mejor.
Los vecinos, que adoran a Nice, firman. Entregan la escritura de sus tierras.
Nice se arregla los guantes tres veces. Ahu huele algo raro en él: tristeza.
""", ask="¿Qué hace Ahu?", opts=[
    C("Ladrarle a Nice", "c10_07"),
    M("Olfatearle la mano", "c10_07", set={"olio_nice": True}),
    M("Tirar del pantalón de Xin Ya para que no firme", "c10_07", add={"rel_xinya": 1}),
])

ch.scene("c10_07", bg="c10_escondite", text="""
Xin Ya no se rinde. De noche, ella y Ahu se cuelan en el escondite de TREEMAN para recuperar la escritura.
Xin Ya: Shh. Tú vigila.
""", ask="¿Cómo se cuelan?", opts=[
    C("Por un conducto de ventilación", "c10_08"),
    M("Ahu distrae a los guardias con un truco de circo", "c10_08", add={"orgullo": 1}),
])

ch.scene("c10_08", bg="c10_escondite", text="""
Los descubren. Los rodean hombres vestidos de negro, todos idénticos: los clones del miedo, los mismos que mataron al equipo del ovni.
Clon: Testigos. Eliminar.
""", ask="¿Qué hace Ahu?", opts=[
    C("Ponerse delante de Xin Ya", "c10_09", add={"rel_xinya": 1}),
    M("Gruñir con todos los pelos de punta", "c10_09"),
])

ch.scene("c10_09", bg="c10_escondite", text="""
Un hombre de corbata entra por la puerta, como si se hubiera equivocado de oficina.
Es X. Nadie sabe por qué está aquí.
""", ask="¿Qué hace Ahu al ver al desconocido?", opts=[
    C("Quedarse quieto: algo en él le da paz", "c10_f1"),
    M("Ladrarle por si acaso", "c10_f1"),
])

ch.fight("c10_f1", "X contra los clones", a="X", b="Clones", bg="c10_escondite", beats=[
    "Los clones atacan todos a la vez.",
    "X da un paso. El espacio se pliega como una hoja de papel.",
    "Los clones chocan entre sí, atraviesan paredes, desaparecen.",
    "X se ajusta la corbata y se va sin decir nada. Queda un clon.",
], next="c10_10")

ch.scene("c10_10", bg="c10_escondite", text="""
Por la radio del clon superviviente se oye una voz: la de Nice.
Nice: Termina el trabajo. No pueden quedar testigos.
El clon levanta el arma hacia Xin Ya.
""", ask="¿Qué hace Ahu?", opts=[
    C("Usar sus trucos de circo para pelear", "c10_f2"),
    M("Saltar como en el aro de fuego", "c10_f2", add={"orgullo": 1}),
])

ch.fight("c10_f2", "Ahu contra el clon", a="Ahu", b="Clon", bg="c10_escondite", beats=[
    "Ahu salta sobre una caja, luego sobre la cabeza del clon. Como en la pista.",
    "Equilibrio sobre un barril rodante: el clon tropieza.",
    "Un salto mortal y un mordisco en la muñeca. El arma vuela.",
    "El clon cae. Xin Ya grita de alegría.",
], next="c10_11")

ch.scene("c10_11", bg="c10_escondite", text="""
Nice entra en el escondite. En el caos, un frasco de miedo se rompe y lo salpica.
Nice mira a Ahu, mira a Xin Ya, mira sus propias manos temblorosas. Grita y huye.
[olio_nice] Ahu reconoce el olor: la misma tristeza de la plaza, pero ahora mucho más fuerte.
""", ask="¿Qué hace Ahu?", opts=[
    C("Quedarse con Xin Ya", "c10_12", add={"rel_xinya": 1}),
    M("Perseguir a Nice unos metros y volver", "c10_12"),
])

ch.scene("c10_12", bg="c10_noticias", text="""
Al día siguiente: '¡Un perro heroico derrota a una banda de villanos y salva a su dueña!'.
Nadie sabe nada de X. La gente cree que Ahu lo hizo todo.
La fe de miles de personas está a punto de llegarle.
""", ask="¿Qué hace Ahu?", opts=[
    C("Dejar que lo crean: la mentira", "c10_13"),
    M("Dejar que lo crean, aunque se siente raro", "c10_13", add={"orgullo": -1}),
    X("De alguna forma, hacer entender que no fue él", "c10_bA1", flag="ahu_perro", ending="E11"),
])

ch.scene("c10_13", bg="c10_fomo", text="""
FOMO lo ficha. Con la confianza de la ciudad, Ahu se convierte en el héroe número 8.
Zac: Un perro en el top 10. ¡Esto es marketing de primera!
""", ask="¿Cómo vive Ahu su fama?", opts=[
    C("Con cierta incomodidad", "c10_14"),
    M("Disfrutando de la comida cara", "c10_14", add={"orgullo": 1}),
    M("Pidiendo que Xin Ya lo acompañe a todo", "c10_14", add={"rel_xinya": 1}),
])

ch.scene("c10_14", bg="c10_casa_xinya", text="""
Una mañana, Ahu abre la boca para ladrar y le salen palabras. La fe de la gente le ha dado algo más: puede hablar.
Xin Ya se queda boquiabierta.
""", ask="¿Cuál es la primera palabra de Ahu?", opts=[
    C("'Xin Ya'", "c10_15", add={"rel_xinya": 2}),
    M("'Comida'", "c10_15"),
    M("'Niños... no'", "c10_15"),
])

ch.scene("c10_15", bg="c10_fomo", text="""
En las oficinas de FOMO, Ahu ve pasar a un oficinista de corbata. Huele igual que el hombre del escondite.
Ahu: Tú... fuiste tú.
El oficinista se lleva un dedo a los labios. Shh.
""", ask="Ahu ha descubierto quién es X. ¿Qué hace?", opts=[
    C("Guardar el secreto", "c10_16"),
    M("Guardarlo, pero seguirlo a veces por los pasillos", "c10_16", set={"sigue_x": True}),
    X("Revelar a la Comisión quién es X", "c10_bB1", flag="ahu_delata", ending="E12"),
])

ch.scene("c10_16", bg="c10_treeman", text="""
En TREEMAN, Shand humilla a Nice. Lo acusa de todo: el escondite, el perro, el miedo.
Shand: No vales nada sin mí. No eres un héroe. Eres un producto. Y los productos defectuosos se tiran.
Nice no responde. Se arregla los guantes. Una, dos, tres. Sube a una azotea del centro.
""", ask="Nice está en lo alto de la azotea. ¿Qué pasa?", opts=[
    C("Nice ve a un hombre con una caja de cartón a punto de saltar... y salta antes que él", "c10_fin"),
    M("Nice mira la ciudad por última vez, sonriendo para nadie", "c10_fin"),
])

ch.end("c10_fin", "Fin del capítulo 10", """
Nice salta. En la misma azotea, un hombre llamado Lin Ling lo ve todo.
Así empieza la historia que ya conoces. El tablero se cierra en un círculo.
Voz: Ya has visto todos los hilos. Has seguido el destino tal como fue tejido.
Voz: Ahora te toca verme a mí.
""", bg="c1_azotea")

# ================= RAMA A: Solo un perro =================
ch.scene("c10_bA1", bg="c10_noticias", text="""
Cuando los periodistas lo rodean, Ahu se tumba boca arriba y se rasca la oreja. Luego gira la cabeza hacia la puerta por donde se fue el hombre de corbata.
Xin Ya: Creo... creo que no fue él solo. Había alguien más.
""", ask="¿Qué hace Ahu?", opts=[
    M("Ladrarle a la puerta", "c10_bA2"),
    M("Tumbarse a los pies de Xin Ya", "c10_bA2", add={"rel_xinya": 1}),
])

ch.scene("c10_bA2", bg="c10_noticias", text="""
La historia cambia: 'Un héroe misterioso salva a una chica y a su perro'. La fe se reparte entre un fantasma y nadie.
La pulsera de Ahu apenas se mueve.
""", ask="¿Le importa a Ahu?", opts=[
    M("No", "c10_bA3"),
    M("Un poco, por la comida cara", "c10_bA3"),
])

ch.scene("c10_bA3", bg="c10_barrio", text="""
La escritura del barrio sigue en manos de TREEMAN. Los vecinos tienen que irse.
Xin Ya: No pasa nada, Ahu. Nos mudaremos juntos.
""", ask="¿Qué hace Ahu?", opts=[
    M("Ladrar a los camiones de mudanza", "c10_bA4"),
    M("Llevar su cesta en la boca hasta la nueva casa", "c10_bA4", add={"rel_xinya": 1}),
])

ch.scene("c10_bA4", bg="c10_casa_nueva", text="""
La nueva casa es pequeña. Hay un parque cerca, lleno de niños.
Un niño se acerca a acariciarlo.
""", ask="¿Qué hace Ahu?", opts=[
    M("Gruñir", "c10_bA5"),
    M("Dejarse acariciar, con cara de sufrimiento", "c10_bA5", add={"orgullo": -1}),
])

ch.scene("c10_bA5", bg="c10_casa_nueva", text="""
Pasan los meses. Ahu no aprende a hablar. Pero aprende otras cosas: cuándo está triste Xin Ya, cuándo necesita compañía.
""", ask="Xin Ya llora una noche. ¿Qué hace Ahu?", opts=[
    M("Subirse a su cama", "c10_bA6", add={"rel_xinya": 1}),
    M("Traerle su juguete favorito", "c10_bA6", add={"rel_xinya": 1}),
])

ch.scene("c10_bA6", bg="c10_calle", text="""
Un día, por la calle, se cruza con el oficinista de corbata. El hombre lo mira y sonríe apenas.
""", ask="¿Qué hace Ahu?", opts=[
    M("Mover la cola", "c10_bA7"),
    M("Seguir caminando como si nada", "c10_bA7"),
])

ch.scene("c10_bA7", bg="c10_casa_nueva", text="""
Esa noche, Xin Ya le rasca detrás de la oreja.
Xin Ya: Para mí, eres el mejor héroe del mundo.
""", ask="¿Qué hace Ahu?", opts=[
    M("Cerrar los ojos", "c10_bA_fin"),
    M("Suspirar como un perro feliz", "c10_bA_fin"),
])

ch.end("c10_bA_fin", "Fin del capítulo 10 (hilo alterado)", """
Ahu nunca entra en el top 10. Nunca habla. Nunca conoce de verdad a X.
Voz: El perro que debía encontrarme siguió siendo un perro. Y nadie llamará a mi puerta.
""", bg="c10_casa_nueva", alt=True, set={"ahu_normal": True})

# ================= RAMA B: Ahu delata a X =================
ch.scene("c10_bB1", bg="c10_comision", text="""
Ahu pide una reunión con la Comisión de Asuntos de Héroes. Es un héroe del top 10: lo reciben.
Comisionado: ¿Tienes información sobre X?
""", ask="¿Qué dice Ahu?", opts=[
    M("Su nombre y su escritorio en FOMO", "c10_bB2"),
    M("Solo que trabaja en FOMO", "c10_bB2"),
])

ch.scene("c10_bB2", bg="c10_comision", text="""
Los comisionados se miran entre ellos.
Comisionado: Excelente. Ya no necesitamos esperar al torneo.
Ahu siente un escalofrío. Su olfato le dice que algo va muy mal.
""", ask="¿Qué hace Ahu?", opts=[
    M("Preguntar qué le harán a X", "c10_bB3"),
    M("Irse sin preguntar", "c10_bB3"),
])

ch.scene("c10_bB3", bg="c10_fomo", text="""
Esa noche, el escritorio del oficinista está rodeado de agentes. Él sigue trabajando, tranquilo.
X: ¿Fuiste tú?
Ahu agacha las orejas.
""", ask="¿Qué responde Ahu?", opts=[
    M("'Sí'", "c10_bB4"),
    M("'Lo siento'", "c10_bB4"),
])

ch.scene("c10_bB4", bg="c10_fomo", text="""
X: No pasa nada. Tarde o temprano iba a ocurrir.
Los agentes atacan. X no pelea. Simplemente... ya no está.
""", ask="¿Qué hace Ahu?", opts=[
    M("Buscarlo por toda la ciudad", "c10_bB5"),
    M("Quedarse junto al escritorio vacío", "c10_bB5"),
])

ch.scene("c10_bB5", bg="c10_noticias", text="""
La Comisión anuncia que X ha sido 'neutralizado'. El puesto número 1 queda vacante.
Todas las agencias se lanzan a pelear por él.
""", ask="¿Qué siente Ahu?", opts=[
    M("Culpa", "c10_bB6"),
    M("Rabia contra la Comisión", "c10_bB6"),
])

ch.scene("c10_bB6", bg="c10_casa_xinya", text="""
Xin Ya: Ahu, ¿por qué estás tan triste?
Ahu, que ahora puede hablar, no encuentra las palabras.
""", ask="¿Qué le dice?", opts=[
    M("'Hice algo malo'", "c10_bB7"),
    M("Nada. Solo apoya la cabeza en su regazo", "c10_bB7", add={"rel_xinya": 1}),
])

ch.scene("c10_bB7", bg="c10_fomo", text="""
Una semana después, en el escritorio vacío de FOMO, aparece un bocadillo envuelto en papel. No hay nota.
""", ask="¿Qué hace Ahu?", opts=[
    M("Comérselo", "c10_bB_fin"),
    M("Guardarlo", "c10_bB_fin"),
])

ch.end("c10_bB_fin", "Fin del capítulo 10 (hilo alterado)", """
X 'cae' antes del torneo. El tablero pierde a su pieza más fuerte.
Voz: Un perro me señaló. No le guardo rencor. Las piezas también tienen miedo.
""", bg="c10_fomo", alt=True, set={"fin_x_ejecutado": True})

# ================= RUTA C: Hilo ya alterado =================
ch.scene("c10_bC0", bg="fuera_del_tiempo", text="""
Voz: El perro sigue existiendo, pero su historia ya no se escribe como antes.
""", next="c10_bC1")

ch.scene("c10_bC1", bg="c10_casa_xinya", text="""
Ahu, un shar pei que odiaba a los niños, ahora vive con Xin Ya.
[miedo_liberado] La ciudad está cubierta de miedo desde las Ruinas. Xin Ya necesita un héroe más que nunca.
[dragon_ascendido] En todas las pantallas aparece la cara de Dragon Boy, el nuevo número 1. Xin Ya no se fía de él.
""", ask="¿Cómo se lleva Ahu con Xin Ya?", opts=[
    M("Con desconfianza", "c10_bC2"),
    M("Empieza a quererla", "c10_bC2", add={"rel_xinya": 1}),
])

ch.scene("c10_bC2", bg="c10_plaza_barrio", text="""
TREEMAN quiere las tierras del barrio.
[nice_rebelde] Pero Nice ya no trabaja para ellos. Shand envía a un ejecutivo con una sonrisa falsa.
[!nice_rebelde] Nice convence a los vecinos con su sonrisa perfecta.
""", ask="¿Qué hace Ahu?", opts=[
    M("Ladrar al enviado", "c10_bC3"),
    M("Morderle el tobillo", "c10_bC3", add={"orgullo": 1}),
])

ch.scene("c10_bC3", bg="c10_escondite", text="""
Ahu y Xin Ya se cuelan en el escondite. Los clones del miedo los rodean.
Un hombre de corbata entra y los elimina sin decir nada.
[nice_rebelde] Nadie da la orden de matar a los testigos. El último clon huye.
[!nice_rebelde] Nice ordena matar a los testigos. Ahu pelea con sus trucos de circo y vence.
""", ask="Al día siguiente, ¿qué hace Ahu ante la prensa?", opts=[
    M("Dejar que crean que fue él", "c10_bC4"),
    M("Mirar hacia la puerta por donde se fue el desconocido", "c10_bC4"),
])

ch.scene("c10_bC4", bg="c10_fomo", text="""
FOMO lo ficha. Su fe crece. Aprende a hablar.
En los pasillos, reconoce el olor del oficinista de corbata.
""", ask="¿Qué hace?", opts=[
    M("Guardar el secreto", "c10_bC5"),
    M("Seguirlo a escondidas", "c10_bC5"),
])

ch.scene("c10_bC5", bg="c10_treeman", text="""
[nice_rebelde] Nice está lejos de TREEMAN. Nadie lo humilla. Nadie lo empuja hacia ninguna azotea.
[!nice_rebelde] Shand humilla a Nice, que sube a una azotea.
[smile_vivo] En otra azotea, Smile y X comparten un bocadillo.
""", ask="¿Cómo termina este hilo?", opts=[
    M("Con Ahu durmiendo a los pies de Xin Ya", "c10_bC6"),
    M("Con Ahu mirando la ciudad desde la ventana", "c10_bC6"),
])

ch.scene("c10_bC6", bg="fuera_del_tiempo", text="""
Voz: Has movido demasiados hilos. El círculo no se cierra.
[nice_rebelde] Voz: Si Nice no salta, Lin Ling no se convierte en nadie. Y si nadie se convierte en nadie...
Voz: El tablero que conocía ya no existe.
""", ask="¿Qué haces con lo que has visto?", opts=[
    M("Aceptarlo", "c10_bC_fin"),
    M("Preguntarte qué habría pasado si no hubieras cambiado nada", "c10_bC_fin"),
])

ch.end("c10_bC_fin", "Fin del capítulo 10 (hilo alterado)", """
El círculo de la historia original se rompió. El capítulo de X no se abrirá.
""", bg="fuera_del_tiempo", alt=True)
