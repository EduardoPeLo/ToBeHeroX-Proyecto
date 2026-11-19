"""Capítulo 2: E-Soul (episodios 5-7)."""
from engine.model import Chapter, C, M, X

ch = Chapter(2, "E-Soul", "Episodios 5-7", start="c2_00", color=(20, 90, 160), intro="""
Antes de ser el relámpago que cayó en aquel callejón, E-Soul era un disfraz de fieltro en un teatro infantil.
""")

ch.scene("c2_00", bg="fuera_del_tiempo", text="""
Voz: Ese relámpago tiene dueño. O, mejor dicho, tuvo dos.
Voz: Retrocedamos. Un huérfano, un teatro y un niño que creía en él.
""", next="c2_01")

# ---------------- EPISODIO 5: UN ACTOR ----------------
ch.scene("c2_01", bg="c2_teatro_infantil", text="""
Yang Cheng suda dentro de un disfraz barato de E-Soul, el héroe legendario del relámpago. Los niños gritan de emoción.
Su pulsera marca cero. Nadie cree en el chico que está dentro del traje.
Niño: ¡E-Soul! ¡Haz el rayo!
""", ask="¿Cómo actúa Yang Cheng frente a los niños?", opts=[
    C("Hacer la pose del Rayo con todo su entusiasmo", "c2_02"),
    M("Hacer la pose, pero cansado", "c2_02"),
    M("Inventar una pose nueva solo para ellos", "c2_02", add={"carisma": 1}),
])

ch.scene("c2_02", bg="c2_camerino", text="""
Detrás del escenario lo espera Xia Qing, la chica de la que está enamorado desde hace meses.
Xia Qing: Mi hermano Pomelo no para de hablar de tu E-Soul. ¿Podrías animarle sus fiestas?
""", ask="¿Qué le responde Yang Cheng?", opts=[
    C("Aceptar, nervioso y feliz", "c2_03", add={"rel_qing": 1}),
    M("Aceptar haciéndose el interesante", "c2_03"),
    M("Aceptar y confesarle que le gusta", "c2_03", add={"rel_qing": 2}),
])

ch.scene("c2_03", bg="c2_casa_qing", text="""
Yang Cheng se convierte en el animador personal de Pomelo. El niño lo adora.
Pomelo: Cuando sea grande, quiero ser igual que tú.
""", ask="¿Qué le dice a Pomelo?", opts=[
    C("'Yo solo soy un disfraz, campeón'", "c2_04"),
    M("'Entonces tendrás que ser valiente'", "c2_04", add={"rel_pomelo": 1}),
    M("Le revuelve el pelo sin decir nada", "c2_04"),
])

ch.scene("c2_04", bg="c2_audicion", text="""
Una audición para nuevos héroes. Yang Cheng hace su mejor número.
El jurado mira la pantalla: confianza, cero. Uno de los jueces, Shang Chao, lo observa en silencio.
""", ask="Lo rechazan delante de todos. ¿Cómo reacciona?", opts=[
    C("Agachar la cabeza e irse", "c2_05"),
    M("Dar las gracias con dignidad", "c2_05", add={"carisma": 1}),
    M("Gritarles que algún día se arrepentirán", "c2_05", add={"rabia": 1}),
])

ch.scene("c2_05", bg="c2_calle", text="""
De vuelta en casa de Qing, gritos. Dos antiguos compañeros del teatro se llevan a Pomelo en una furgoneta.
Xia Qing: ¡Pomelo!
""", ask="La furgoneta arranca. ¿Qué hace Yang Cheng?", opts=[
    C("Perseguirla en un coche prestado", "c2_06"),
    M("Llamar a la policía mientras corre detrás", "c2_06"),
    M("Pedirle a Qing que se quede a salvo y salir tras ellos", "c2_06", add={"rel_qing": 1}),
])

ch.scene("c2_06", bg="c2_autopista", text="""
Persecución por la autopista. La furgoneta va a escapar por una salida.
Yang Cheng aprieta el volante.
""", ask="¿Qué hace?", opts=[
    C("Chocar su coche contra la furgoneta", "c2_07"),
    M("Cerrarle el paso aunque el choque sea inevitable", "c2_07"),
])

ch.scene("c2_07", bg="c2_autopista", text="""
Metal retorcido. Humo. Yang Cheng sale arrastrándose con la frente sangrando.
Pomelo, desde la furgoneta volcada, grita con toda su alma:
Pomelo: ¡E-Soul! ¡Sabía que vendrías!
La pulsera de Yang Cheng marca uno. Una chispa le recorre los dedos.
""", ask="Los secuestradores salen armados. ¿Qué hace?", opts=[
    C("Ponerse en guardia como el E-Soul del teatro", "c2_f1"),
    M("Gritarle a Pomelo que cierre los ojos", "c2_f1", add={"rel_pomelo": 1}),
])

ch.fight("c2_f1", "Yang Cheng contra los secuestradores", a="Yang Cheng", b="Secuestradores", bg="c2_autopista", beats=[
    "Un solo niño cree en él, pero cree con todas sus fuerzas.",
    "La electricidad le recorre el cuerpo. Los secuestradores retroceden.",
    "Imita la pose del teatro, pero ahora el rayo es de verdad.",
    "Los dos hombres caen al asfalto, temblando. Pomelo está a salvo.",
], next="c2_08")

ch.scene("c2_08", bg="c2_autopista", text="""
Entre las luces de las patrullas aparece Shang Chao, el juez de la audición.
Shang Chao: Hoy no había nadie mirando. Y aun así lo hiciste.
""", ask="¿Qué le responde Yang Cheng?", opts=[
    C("'Solo hice lo que haría E-Soul'", "c2_09"),
    M("'Ahora sí cree que tengo confianza, ¿no?'", "c2_09", add={"rabia": 1}),
    M("No dice nada; solo abraza a Pomelo", "c2_09", add={"rel_pomelo": 1}),
])

# ---------------- EPISODIO 6: DOS E-SOUL ----------------
ch.scene("c2_09", bg="c2_redes", text="""
Alguien grabó el rescate con su teléfono. El video se hace viral: 'El NUEVO E-Soul'.
Su pulsera sube a miles. Y el E-Soul original, el legendario, no está contento.
""", ask="¿Cómo vive Yang Cheng la fama repentina?", opts=[
    C("Con miedo de no estar a la altura", "c2_10"),
    M("Leyendo cada comentario, emocionado", "c2_10", add={"carisma": 1}),
    M("Llamando primero a Qing para contárselo", "c2_10", add={"rel_qing": 1}),
])

ch.scene("c2_10", bg="c2_mighty_glory", text="""
Rock, director de Mighty Glory, y Shang Chao lo invitan a cenar.
Rock: El mundo necesita un E-Soul joven. Uno que no sea una leyenda vieja y cansada.
Shang Chao: Si aceptas, yo te construiré un cuartel.
""", ask="¿Acepta convertirse en héroe?", opts=[
    C("Aceptar", "c2_11"),
    M("Aceptar, pero con la condición de seguir en el teatro", "c2_11", add={"carisma": 1}),
    M("Aceptar mirando solo a Shang Chao, sin fiarse de Rock", "c2_11", set={"desconfia_rock": True}),
])

ch.scene("c2_11", bg="c2_cuartel", text="""
Shang Chao cumple su palabra: un pequeño cuartel con pantallas, un taller y un póster del E-Soul original en la pared.
Shang Chao: El nombre pesa. Vas a tener que ganártelo.
""", ask="¿Qué hace con el póster del E-Soul original?", opts=[
    C("Dejarlo como inspiración", "c2_12"),
    M("Quitarlo y poner una foto con Pomelo", "c2_12", add={"rel_pomelo": 1}),
    M("Dejarlo, pero mirarlo con recelo", "c2_12", add={"rabia": 1}),
])

ch.scene("c2_12", bg="c2_noticias", text="""
Escándalo: el mánager del E-Soul original filtra 'pruebas' de que Yang Cheng organizó el secuestro para hacerse famoso.
La confianza se le desploma. Entonces Enlighter, un periodista, publica una investigación que lo limpia por completo.
Enlighter: La verdad siempre tiene más audiencia que la mentira. A la larga.
""", ask="¿Qué siente Yang Cheng hacia el E-Soul original?", opts=[
    C("Rencor: cree que él está detrás de todo", "c2_13", add={"rabia": 1}),
    M("Confusión: no entiende por qué lo odian", "c2_13"),
    M("Ganas de hablar con él cara a cara", "c2_13", set={"quiere_hablar": True}),
])

ch.scene("c2_13", bg="c2_cuartel_noche", text="""
Al día siguiente, Yang Cheng, Qing y Shang Chao celebran en el cuartel.
Uno de los secuestradores, que había escapado, entra por la puerta. Dispara.
Shang Chao cae frente a ellos. El asesino huye por la ventana.
""", ask="Shang Chao muere en sus brazos. ¿Qué hace Yang Cheng?", opts=[
    C("Gritar de rabia; jura vengarse del E-Soul original", "c2_14", add={"rabia": 2}),
    M("Quedarse con Chao hasta el final, llorando", "c2_14", add={"rabia": 1}),
    X("Contener la rabia y seguir el rastro del asesino", "c2_bA1", flag="cheng_perdona", ending="E04"),
])

# ---------------- EPISODIO 7: TRES ASIENTOS ----------------
ch.scene("c2_14", bg="c2_funeral", text="""
En el funeral de Shang Chao hay tres asientos vacíos en primera fila.
Yang Cheng anuncia que va a retar a duelo al E-Soul original.
Xia Qing: ¡Esto no te devolverá a Chao! ¡Te estás convirtiendo en otra persona!
""", ask="Xia Qing se opone al duelo. ¿Qué hace él?", opts=[
    C("Darle la espalda; se pelean y ella se va", "c2_15", add={"rel_qing": -2}),
    M("Pedirle perdón, pero seguir con el duelo", "c2_15", add={"rel_qing": -1}),
])

ch.scene("c2_15", bg="c2_mighty_glory", text="""
Rock lo recibe en su oficina, rodeado de figuras antiguas de un héroe llamado Cero.
Rock: El E-Soul original es más fuerte que tú. Pero es predecible: cuando lo presionan, siempre usa su Corte Relámpago.
Rock: Lanzaremos una campaña en internet. Lo obligaremos a pelear a nuestra manera.
""", ask="¿Acepta la estrategia de Rock?", opts=[
    C("Aceptar: solo quiere justicia para Chao", "c2_16"),
    M("Aceptar, pero sin atacar a la familia del rival", "c2_16"),
    X("Ofrecerse a Rock como su arma, para cualquier cosa", "c2_bB1", flag="cheng_sicario", ending="E05"),
])

ch.scene("c2_16", bg="c2_arena", text="""
La campaña funciona: todo internet exige el duelo. El E-Soul original acepta.
En la arena, el viejo héroe lo mira con desprecio.
E-Soul original: Tú no eres yo. Eres un disfraz con suerte.
""", ask="¿Qué le responde Yang Cheng?", opts=[
    C("'Hoy vas a pagar por Shang Chao'", "c2_17"),
    M("'Puede ser. Pero este disfraz sí salvó a alguien'", "c2_17", add={"carisma": 1}),
])

ch.scene("c2_17", bg="c2_arena", text="""
El duelo comienza. El E-Soul original es rapidísimo.
La presión del público crece. El viejo héroe concentra el relámpago: va a usar el Corte Relámpago, tal como dijo Rock.
""", ask="¿Cuál es el plan de Yang Cheng?", opts=[
    C("Esperar el Corte Relámpago para contraatacar", "c2_f2"),
    M("Provocarlo para que lo lance antes", "c2_f2"),
])

ch.fight("c2_f2", "E-Soul contra E-Soul", a="Yang Cheng", b="E-Soul original", bg="c2_arena", beats=[
    "Dos relámpagos chocan y la arena se queda sin luz.",
    "El E-Soul original lo acorrala: décadas de experiencia contra semanas.",
    "El público grita. La confianza oscila de uno a otro como un péndulo.",
    "Llega el Corte Relámpago. Yang Cheng ya lo estaba esperando.",
    "Su contraataque atraviesa la guardia del viejo héroe.",
], next="c2_18")

ch.scene("c2_18", bg="c2_arena", text="""
El E-Soul original está en el suelo, vencido. La multitud pide un final.
[quiere_hablar] Durante un instante, Yang Cheng recuerda que quería hablar con él.
[rel_qing<0] En las gradas no está Qing.
""", ask="¿Qué hace Yang Cheng?", opts=[
    C("Dar el golpe final", "c2_fin"),
    M("Dudar... pero el relámpago se le escapa de las manos", "c2_fin", add={"rabia": 1}),
])

ch.end("c2_fin", "Fin del capítulo 2", """
El E-Soul original muere. Su confianza fluye hacia Yang Cheng, que se convierte en el único E-Soul, número 9 del ranking.
Esa noche, en su oficina, Rock brinda en solitario. El secuestro de Pomelo y el asesinato de Shang Chao fueron obra suya.
Voz: Un relámpago fabricado. Algún día caerá sobre un callejón bajo la lluvia.
""", bg="c2_mighty_glory")

# ================= RAMA A: Yang Cheng investiga =================
ch.scene("c2_bA1", bg="c2_cuartel_noche", text="""
Yang Cheng aprieta los dientes y deja que la electricidad se apague.
Yang Cheng: No. Primero la verdad.
Sigue el rastro de sangre hasta la ventana. El asesino dejó caer un teléfono.
""", ask="¿Qué hace con el teléfono?", opts=[
    M("Revisarlo él mismo", "c2_bA2"),
    M("Dárselo a Enlighter, el periodista", "c2_bA2", set={"ayuda_enlighter": True}),
])

ch.scene("c2_bA2", bg="c2_cuartel_noche", text="""
[ayuda_enlighter] Enlighter descifra los mensajes en una noche.
En el teléfono hay transferencias. Todas desde una cuenta fantasma vinculada a Mighty Glory.
""", ask="¿Qué piensa Yang Cheng?", opts=[
    M("Que Rock lo traicionó", "c2_bA3"),
    M("Que aún falta una prueba definitiva", "c2_bA3"),
])

ch.scene("c2_bA3", bg="c2_almacen", text="""
Encuentra al asesino escondido en un almacén del puerto, temblando.
Secuestrador: ¡Si hablo, me matan!
""", ask="¿Cómo lo hace hablar?", opts=[
    M("Prometerle protección", "c2_bA4"),
    M("Amenazarlo con el relámpago", "c2_bA4", add={"rabia": 1}),
])

ch.scene("c2_bA4", bg="c2_almacen", text="""
Secuestrador: Fue Rock. Él organizó lo de Pomelo, la filtración... y lo de Chao. Quería fabricar un héroe nuevo y quedarse con el viejo nombre.
En la puerta del almacén aparece el E-Soul original. Él también estaba siguiendo la pista.
""", ask="El E-Soul original está frente a él. ¿Qué hace?", opts=[
    M("Proponerle una tregua", "c2_bA5"),
    M("Mostrarle las pruebas en silencio", "c2_bA5"),
])

ch.scene("c2_bA5", bg="c2_almacen", text="""
E-Soul original: Ese mánager que te acusó trabajaba para Rock. A mí también me usaron.
Los dos relámpagos se miran. No hace falta un duelo.
""", ask="¿Cómo exponen a Rock?", opts=[
    M("Ante la Comisión de Asuntos de Héroes", "c2_bA6"),
    M("En directo, en la arena del duelo", "c2_bA6", add={"carisma": 1}),
])

ch.scene("c2_bA6", bg="c2_arena", text="""
Las pruebas salen a la luz ante millones de pulseras. La confianza en Mighty Glory se desploma.
Rock no se inmuta ante las cámaras. Sonríe como si fuera parte del plan.
Rock: La fe es un río, chico. Siempre encuentra otro cauce.
""", ask="¿Qué le dice Yang Cheng a Rock?", opts=[
    M("'Esta vez el río te arrastra a ti'", "c2_bA7"),
    M("Nada. Solo lo mira mientras se lo llevan", "c2_bA7"),
])

ch.scene("c2_bA7", bg="c2_teatro_infantil", text="""
Semanas después, Yang Cheng vuelve al teatro infantil. Xia Qing está en primera fila con Pomelo.
Xia Qing: ¿Vas a seguir siendo E-Soul?
""", ask="¿Qué responde?", opts=[
    M("'Los dos lo seremos. Hay sitio para dos rayos'", "c2_bA_fin", add={"rel_qing": 1}),
    M("'Para Pomelo, siempre'", "c2_bA_fin", add={"rel_pomelo": 1}),
])

ch.end("c2_bA_fin", "Fin del capítulo 2 (hilo alterado)", """
Rock es detenido. Mighty Glory pasa a manos de la Comisión.
El E-Soul original sigue vivo. Yang Cheng no entra en el top 10, pero la gente lo quiere.
Voz: Un relámpago que no mató. Me pregunto adónde irá ahora.
""", bg="c2_teatro_infantil", alt=True, set={"rock_expuesto": True, "esoul_original_vivo": True})

# ================= RAMA B: El arma de Rock =================
ch.scene("c2_bB1", bg="c2_mighty_glory", text="""
Rock: Arma. Me gusta esa palabra.
Le entrega un sobre. Dentro está la rutina diaria del E-Soul original: horarios, rutas, su casa.
""", ask="¿Qué hace Yang Cheng con la información?", opts=[
    M("Estudiarla toda la noche", "c2_bB2", add={"rabia": 1}),
    M("Dudar un momento y luego aceptarla", "c2_bB2"),
])

ch.scene("c2_bB2", bg="c2_calle", text="""
Xia Qing lo espera en la puerta de su casa.
Xia Qing: Tus ojos ya no son los tuyos. ¿Qué te prometió ese hombre?
""", ask="¿Qué le dice a Qing?", opts=[
    M("'Justicia'", "c2_bB3", add={"rel_qing": -1}),
    M("Cierra la puerta sin responder", "c2_bB3", add={"rel_qing": -2}),
])

ch.scene("c2_bB3", bg="c2_calle_noche", text="""
No hay duelo ni arena. Yang Cheng embosca al E-Soul original en un callejón.
E-Soul original: ¿Así que esto eres? ¿Un perro de Rock?
""", ask="¿Cómo ataca?", opts=[
    M("De frente, con todo el relámpago", "c2_bB4"),
    M("Por la espalda", "c2_bB4", add={"rabia": 1}),
])

ch.scene("c2_bB4", bg="c2_calle_noche", text="""
Es rápido y brutal. El viejo héroe cae. Su confianza fluye hacia Yang Cheng, sucia, oscura.
Rock lo llama por teléfono.
Rock: Hay más nombres en la lista.
""", ask="¿Acepta la siguiente misión?", opts=[
    M("Sí, sin preguntar", "c2_bB5"),
    M("Sí, pero pregunta para qué", "c2_bB5", set={"pregunto_rock": True}),
])

ch.scene("c2_bB5", bg="c2_mighty_glory", text="""
[pregunto_rock] Rock: Para que vuelva Cero, chico. Para que el mundo tenga un solo dios.
[!pregunto_rock] Rock sonríe. No necesita explicarle nada a un arma.
Pomelo le escribe un mensaje: '¿Por qué ya no vienes al teatro?'.
""", ask="¿Qué hace con el mensaje de Pomelo?", opts=[
    M("Borrarlo", "c2_bB6", add={"rel_pomelo": -1}),
    M("Leerlo diez veces y no responder", "c2_bB6"),
])

ch.scene("c2_bB6", bg="c2_calle_noche", text="""
Misiones, una tras otra. Héroes rebeldes. Periodistas molestos. El relámpago ya no tiembla en sus manos.
Una noche, su objetivo es Enlighter, el periodista que una vez lo salvó.
""", ask="¿Qué hace?", opts=[
    M("Cumplir la orden", "c2_bB7", set={"enlighter_atacado": True}),
    M("Dejarlo escapar y mentirle a Rock", "c2_bB7"),
])

ch.scene("c2_bB7", bg="c2_mighty_glory", text="""
Rock lo nombra su campeón. Yang Cheng es el número 9 del ranking, y el más temido.
Rock: Ahora eres el relámpago de un dios que todavía no ha nacido.
""", ask="¿Cómo se ve Yang Cheng en el espejo?", opts=[
    M("Como un héroe", "c2_bB_fin"),
    M("Como alguien que ya no conoce", "c2_bB_fin"),
])

ch.end("c2_bB_fin", "Fin del capítulo 2 (hilo alterado)", """
Xia Qing y Pomelo se mudan lejos. Yang Cheng es ahora el relámpago personal de Rock.
Voz: Un arma leal es más peligrosa que un héroe vengativo. Rock acaba de ganar una pieza.
""", bg="c2_mighty_glory", alt=True, set={"cheng_oscuro": True})
