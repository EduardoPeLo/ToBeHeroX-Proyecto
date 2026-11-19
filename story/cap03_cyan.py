"""Capítulo 3: Lucky Cyan (episodios 8-10)."""
from engine.model import Chapter, C, M, X

ch = Chapter(3, "Lucky Cyan", "Episodios 8-10", start="c3_00", color=(20, 140, 130), intro="""
Algunos nacen con suerte. Otros la reciben de cien desconocidos que rezan al mismo tiempo.
""")

ch.scene("c3_00", bg="fuera_del_tiempo", text="""
Voz: Ahora, un hilo de color cian. Empieza con un avión que cae.
Voz: Ahí comienza la historia de una niña y la de dos héroes que no llegaron.
""", next="c3_01")

# ---------------- EPISODIO 8: LA CHICA CIAN ----------------
ch.scene("c3_01", bg="c3_avion_restos", text="""
Restos humeantes de un avión en la montaña. Ningún héroe vino a salvarlos.
Liu Zhen, un periodista, avanza entre el metal retorcido y oye un llanto. Una niña pequeña, sin un rasguño.
""", ask="Liu Zhen encuentra a la niña. ¿Qué hace?", opts=[
    C("Tomarla en brazos y sacarla de allí", "c3_02"),
    M("Fotografiar el lugar antes de que llegue nadie", "c3_02", set={"fotos_zhen": True}),
    M("Buscar más sobrevivientes primero", "c3_02"),
])

ch.scene("c3_02", bg="c3_redaccion", text="""
Liu Zhen escribe un reportaje feroz: ningún héroe intervino en el accidente. Su editor se niega a publicarlo.
Liu Zhen: Entonces renuncio.
Deja a la niña en un orfanato y le da un nombre: Cyan.
""", ask="Antes de irse, ¿qué le deja Liu Zhen a la niña?", opts=[
    C("Solo su nombre", "c3_03"),
    M("Una pequeña cinta de color cian", "c3_03", set={"cinta_cian": True}),
    M("Una promesa de volver algún día", "c3_03"),
])

ch.scene("c3_03", bg="c3_orfanato_culto", text="""
Cinco años después. Todo lo que Cyan toca sale bien: si lanza una moneda, gana; si reza, llueve.
El director del orfanato descubre su suerte y la explota. El orfanato se convierte en un culto en torno a ella.
Huérfano: ¡Bendícenos, Cyan!
""", ask="¿Cómo se siente Cyan con su papel de 'santa'?", opts=[
    C("Confundida; solo hace lo que le piden", "c3_04"),
    M("Triste; quiere jugar como los demás niños", "c3_04"),
    M("Orgullosa, al menos un poco", "c3_04", add={"ego_cyan": 1}),
])

ch.scene("c3_04", bg="c3_patio", text="""
En un rincón del patio hay un niño al que todos evitan: Luo. Dicen que trae mala suerte.
Cuando Cyan se acerca, a Luo se le cae una maceta en la cabeza... y a ella no le pasa nada.
""", ask="¿Qué hace Cyan?", opts=[
    C("Sentarse a su lado y hablar con él", "c3_05", add={"rel_luo": 1}),
    M("Ayudarlo a limpiarse la tierra", "c3_05", add={"rel_luo": 1}),
    M("Reírse con él de la maceta", "c3_05", add={"rel_luo": 2}),
])

ch.scene("c3_05", bg="c3_orfanato_noche", text="""
Seis años más tarde, adolescentes, Cyan y Luo planean escapar del orfanato.
El director los descubre en la puerta. Es un antiguo héroe y tiene una obsesión: convertir a todos los huérfanos en héroes.
Director: La suerte de esta niña es mía.
""", ask="Los atrapan. ¿Qué hace Cyan?", opts=[
    C("Ponerse delante de Luo", "c3_06", add={"rel_luo": 1}),
    M("Suplicar que no castiguen a Luo", "c3_06"),
    M("Mirar al director a los ojos, sin miedo", "c3_06", add={"ego_cyan": 1}),
])

# ---------------- EPISODIO 9: PÉRDIDA Y GANANCIA ----------------
ch.scene("c3_06", bg="c3_orfanato_accidente", text="""
Esa misma noche, un camión se estrella contra el muro del orfanato. La suerte de Cyan y la desgracia de Luo se cruzan: el muro se abre justo delante de ella.
Luo: ¡Vete! ¡Yo los distraigo!
""", ask="Luo se queda atrás para que ella escape. ¿Qué hace Cyan?", opts=[
    C("Correr, llorando, sin mirar atrás", "c3_07"),
    M("Correr, prometiéndole que volverá por él", "c3_07", set={"promesa_luo": True}),
    X("No irse sin él: volver a buscarlo", "c3_bA1", flag="cyan_huye", ending="E09"),
])

ch.scene("c3_07", bg="c3_calles", text="""
En la calle, Cyan se arranca su identidad de 'santa'. Ya no quiere ser la diosa de nadie.
Sin el culto, su suerte desaparece y su confianza baja a cero. Sobrevive cantando por monedas.
""", ask="¿Qué canta Cyan en la calle?", opts=[
    C("Las canciones que cantaba en el orfanato", "c3_08"),
    M("Canciones que inventa sobre Luo", "c3_08", add={"rel_luo": 1}),
    M("Lo que la gente le pide", "c3_08"),
])

ch.scene("c3_08", bg="c3_dos_oficina", text="""
Una agente de DOS la escucha cantar. Al poco tiempo, Mickey, el director de la agencia, le hace una oferta.
Mickey: Te convertiremos en estrella. Y a cambio, sacaremos a tu amigo de ese orfanato.
""", ask="¿Acepta la oferta de DOS?", opts=[
    C("Aceptar por Luo", "c3_09"),
    M("Aceptar, pero exigiéndolo por escrito", "c3_09", set={"contrato_luo": True}),
    M("Aceptar sin pensar en nada más", "c3_09"),
])

ch.scene("c3_09", bg="c3_dos_oficina", text="""
DOS va al orfanato. El director les miente: Luo murió en el accidente.
En realidad, lo tiene encerrado en el sótano.
[promesa_luo] Cyan se rompe por dentro: le había prometido volver.
""", ask="Cyan cree que Luo está muerto. ¿Qué hace?", opts=[
    C("Cantar para honrarlo", "c3_10"),
    M("Encerrarse días enteros sin hablar con nadie", "c3_10"),
    M("Pedirle a DOS que investigue más", "c3_10", set={"duda_muerte": True}),
])

ch.scene("c3_10", bg="c3_concierto", text="""
Dos años después: 'Lucky Cyan' llena estadios. Dicen que sus canciones traen buena suerte.
Lejos de allí, en el orfanato abandonado, los huérfanos se han transformado en criaturas parecidas a zombis.
""", ask="Antes de un concierto, ¿qué hace Cyan?", opts=[
    C("Mirar una vieja foto del orfanato", "c3_11"),
    M("Ensayar hasta quedarse sin voz", "c3_11"),
    M("Firmar autógrafos con una sonrisa vacía", "c3_11"),
])

# ---------------- EPISODIO 10: LA VERDAD DETRÁS DE LA SUERTE ----------------
ch.scene("c3_11", bg="c3_noticias", text="""
Un escándalo: alguien filtra que Cyan fue la única superviviente del accidente aéreo. La gente empieza a decir que su suerte se 'robó' la vida de los pasajeros.
El miedo de la gente es tan grande que la zona del orfanato se pudre. Los zombis se multiplican.
""", ask="La opinión pública se vuelve contra ella. ¿Qué hace Cyan?", opts=[
    C("Volver al orfanato para enfrentar lo que pasa", "c3_12"),
    M("Volver, aunque DOS se lo prohíba", "c3_12", add={"ego_cyan": -1}),
    X("Abrazar el culto: anunciar que ella es su diosa", "c3_bB1", flag="cyan_culto", ending="E06"),
])

ch.scene("c3_12", bg="c3_dos_oficina", text="""
Queen, la heroína número 2 de DOS, aparece en la reunión.
Queen: La caja negra de ese avión nunca se encontró. Si la recupero, sabremos la verdad.
""", ask="¿Qué le dice Cyan a Queen?", opts=[
    C("'Yo iré al orfanato. Tú busca la caja'", "c3_13"),
    M("'¿Por qué me ayudas?'", "c3_13", add={"rel_queen": 1}),
    M("'No necesito ayuda'", "c3_13", add={"rel_queen": -1}),
])

ch.scene("c3_13", bg="c3_orfanato_zombi", text="""
El orfanato está irreconocible. Los huérfanos convertidos la rodean, gimiendo. En el centro, el director, deformado por el miedo.
Director: ¡Tu suerte era mía! ¡Devuélvemela!
""", ask="¿Cómo pelea Cyan?", opts=[
    C("Cantando: su música está hecha de fe", "c3_f1"),
    M("Cantando la canción que inventó para Luo", "c3_f1", add={"rel_luo": 1}),
])

ch.fight("c3_f1", "Lucky Cyan contra el director", a="Cyan", b="Director", bg="c3_orfanato_zombi", beats=[
    "La voz de Cyan llena el patio. Cada nota es un golpe de buena suerte.",
    "Los zombis tropiezan, las vigas caen justo donde ella necesita.",
    "El director se lanza sobre ella, enorme y retorcido.",
    "La última nota lo derriba. Los huérfanos dejan de moverse.",
], next="c3_14")

ch.scene("c3_14", bg="c3_sotano", text="""
Del sótano sale alguien más: Luo. Vivo, pero infectado por el miedo, con los ojos negros.
Luo: ¿Sabes quiénes iban en ese avión? Mis padres, Cyan. Tu suerte los mató.
""", ask="Luo la ataca. ¿Qué hace Cyan?", opts=[
    C("Defenderse sin hacerle daño", "c3_f2"),
    M("Gritarle que lo creía muerto", "c3_f2", add={"rel_luo": 1}),
])

ch.fight("c3_f2", "Lucky Cyan contra Luo", a="Cyan", b="Luo", bg="c3_sotano", winner="none", beats=[
    "La desgracia de Luo y la suerte de Cyan chocan. Todo a su alrededor se rompe a la vez.",
    "Cyan no quiere golpearlo. Solo canta, y canta más fuerte.",
    "Luo vacila. Las lágrimas le limpian el negro de los ojos.",
], next="c3_15")

ch.scene("c3_15", bg="c3_sotano", text="""
Queen llega con la caja negra. La grabación suena en el sótano: los pasajeros, antes de morir, rezaban por la niña. Pedían que al menos ella viviera.
Su suerte no era robada. Era un regalo.
""", ask="¿Qué hace Cyan al oír la grabación?", opts=[
    C("Abrazar a Luo", "c3_16", add={"rel_luo": 1}),
    M("Llorar sin poder moverse", "c3_16"),
    M("Darle las gracias a Queen", "c3_16", add={"rel_queen": 1}),
])

ch.scene("c3_16", bg="c3_sotano", text="""
Luo se recupera. Los dos se reconcilian entre los escombros.
Luo: Tu suerte... y mi mala suerte. Quizá se equilibran.
""", ask="¿Qué le responde Cyan?", opts=[
    C("'Entonces no te separes de mí'", "c3_17", add={"rel_luo": 1}),
    M("'La suerte se comparte'", "c3_17"),
    M("Se ríe y le cae una gota del techo a él", "c3_17", add={"rel_luo": 1}),
])

ch.scene("c3_17", bg="c3_concierto", text="""
Cyan queda limpia ante el público y entra en el ranking como número 7.
En su primer concierto como heroína, la gente canta con ella.
""", ask="¿A quién le dedica la primera canción?", opts=[
    C("A los pasajeros del avión", "c3_fin"),
    M("A Luo", "c3_fin", add={"rel_luo": 1}),
    M("A Liu Zhen, el hombre que la salvó", "c3_fin", set={"dedica_zhen": True}),
])

ch.end("c3_fin", "Fin del capítulo 3", """
Detrás del escenario, Liu Zhen y Mickey conversan en voz baja. Todo esto, desde la filtración, fue orquestado para sacar a la luz el poder del miedo.
En TREEMAN, Shand mira la misma transmisión. Esa noche ordena empezar experimentos con el miedo.
Voz: Una canción salva a una niña. La misma canción le enseña a un hombre malo un arma nueva.
""", bg="c3_concierto")

# ================= RAMA A: Cyan y Luo huyen juntos =================
ch.scene("c3_bA1", bg="c3_orfanato_accidente", text="""
Cyan da media vuelta y corre hacia el humo.
Luo: ¡¿Qué haces?! ¡Te van a atrapar!
Le agarra la mano. Algo raro pasa: una viga cae... y se detiene, atascada justo sobre sus cabezas.
""", ask="¿Por dónde escapan?", opts=[
    M("Por el muro roto", "c3_bA2"),
    M("Por el tejado", "c3_bA2", add={"rel_luo": 1}),
])

ch.scene("c3_bA2", bg="c3_calles", text="""
Juntos, la suerte y la desgracia se anulan: nada sale ni muy bien ni muy mal. Por primera vez, son normales.
Duermen bajo un puente.
Luo: ¿Y ahora qué?
""", ask="¿Qué responde Cyan?", opts=[
    M("'Ahora vivimos'", "c3_bA3"),
    M("'Ahora buscamos al hombre que me salvó'", "c3_bA3", set={"busca_zhen": True}),
])

ch.scene("c3_bA3", bg="c3_calles", text="""
Cantan en la calle, Cyan la voz, Luo un tambor hecho con un cubo. Ganan lo justo.
Un día ven al director del orfanato buscándolos con fotos.
""", ask="¿Qué hacen?", opts=[
    M("Esconderse y cambiar de ciudad", "c3_bA4"),
    M("Enfrentarlo en público", "c3_bA4", add={"ego_cyan": 1}),
])

ch.scene("c3_bA4", bg="c3_redaccion", text="""
[busca_zhen] Encuentran a Liu Zhen en una redacción pequeña.
[!busca_zhen] Es Liu Zhen quien los encuentra a ellos: los reconoce por la cinta cian.
Liu Zhen: Puedo convertirte en estrella. Hay una agencia, DOS...
""", ask="¿Acepta Cyan?", opts=[
    M("No. No quiere ser la diosa ni la estrella de nadie", "c3_bA5"),
    M("Pregunta qué le pasaría a Luo", "c3_bA5", add={"rel_luo": 1}),
])

ch.scene("c3_bA5", bg="c3_redaccion", text="""
Liu Zhen: Luo no entra en el plan.
Cyan lo entiende: para la agencia, Luo es un estorbo.
""", ask="¿Qué decide?", opts=[
    M("Rechazar a Zhen y a DOS para siempre", "c3_bA6"),
    M("Pedirle a Zhen ayuda para cerrar el orfanato", "c3_bA6", set={"orfanato_cerrado": True}),
])

ch.scene("c3_bA6", bg="c3_pueblo", text="""
[orfanato_cerrado] Zhen publica un reportaje sobre el culto. El orfanato se cierra y los niños son trasladados.
Cyan y Luo se instalan en un pueblo de montaña. Ella canta en las bodas y él arregla cosas que siempre se vuelven a romper.
""", ask="¿Cyan quiere volver a ser 'afortunada'?", opts=[
    M("No. La normalidad es su suerte", "c3_bA7"),
    M("Solo un poco, para ayudar al pueblo", "c3_bA7"),
])

ch.scene("c3_bA7", bg="c3_pueblo", text="""
Una noche de tormenta, Luo le enseña una noticia: van a buscar la caja negra del avión.
Luo: ¿Quieres saber la verdad?
""", ask="¿Qué responde Cyan?", opts=[
    M("'Ya sé lo que necesito saber'", "c3_bA_fin", add={"rel_luo": 1}),
    M("'Algún día. Ahora no'", "c3_bA_fin"),
])

ch.end("c3_bA_fin", "Fin del capítulo 3 (hilo alterado)", """
Lucky Cyan nunca existió. No hubo estadios ni canciones de la suerte. Hubo dos huérfanos que se equilibraron.
Sin el escándalo de Cyan, nadie vio el poder del miedo. Shand tardará más en encontrar su arma.
Voz: Un hilo cian que se aparta del tablero. Algunos aplaudirían. Otros se quedarán sin compañera.
""", bg="c3_pueblo", alt=True, set={"cyan_libre": True})

# ================= RAMA B: La diosa del culto =================
ch.scene("c3_bB1", bg="c3_orfanato_zombi", text="""
Cyan vuelve al orfanato, pero no para pelear. Sube al altar.
Cyan: Si me tienen miedo, que me teman. Si me adoran, que me adoren. Yo soy su suerte.
Los zombis se arrodillan.
""", ask="¿Qué les ordena Cyan?", opts=[
    M("Que la protejan", "c3_bB2"),
    M("Que traigan al director ante ella", "c3_bB2", add={"ego_cyan": 1}),
])

ch.scene("c3_bB2", bg="c3_orfanato_zombi", text="""
El director, deformado, cae a sus pies. El miedo y la fe se mezclan en algo nuevo, una adoración que da escalofríos.
Su pulsera marca números que suben y bajan sin control.
""", ask="¿Qué hace con el director?", opts=[
    M("Perdonarlo y convertirlo en su sirviente", "c3_bB3"),
    M("Dejarlo encerrado en el sótano, como él hizo con otros", "c3_bB3", set={"sotano_abierto": True}),
])

ch.scene("c3_bB3", bg="c3_sotano", text="""
[sotano_abierto] Al abrir el sótano encuentra a Luo, infectado, con los ojos negros.
[!sotano_abierto] Desde el sótano se oye una voz conocida: Luo está vivo.
Luo: Tu suerte mató a mis padres... y ahora te adoran por eso.
""", ask="¿Qué hace la 'diosa' con Luo?", opts=[
    M("Pedirle que se arrodille", "c3_bB4", add={"rel_luo": -2}),
    M("Abrazarlo, aunque el miedo los contagie a los dos", "c3_bB4", add={"rel_luo": 1}),
])

ch.scene("c3_bB4", bg="c3_noticias", text="""
El culto crece. Sus fieles llevan el miedo a la ciudad: donde va la diosa, todo se pudre o se llena de una suerte enfermiza.
DOS pierde el control de la situación. Mickey envía a Queen.
""", ask="¿Cómo recibe Cyan a Queen?", opts=[
    M("Con una canción de bienvenida", "c3_bB5"),
    M("Con un ejército de fieles", "c3_bB5", add={"ego_cyan": 1}),
])

ch.scene("c3_bB5", bg="c3_orfanato_zombi", text="""
Queen: Esto no es suerte, niña. Es miedo con un vestido bonito.
Queen crea su área: dentro, las reglas las pone ella. Pero la fe de los fieles empuja contra sus límites.
""", ask="¿Qué hace Cyan?", opts=[
    M("Cantar para romper el área de Queen", "c3_bB6"),
    M("Dudar por primera vez", "c3_bB6", add={"ego_cyan": -1}),
])

ch.scene("c3_bB6", bg="c3_orfanato_zombi", text="""
El choque es terrible. Queen resiste, pero no puede ganar sin herir a cientos de fieles.
Se retira. Es la primera vez que retrocede.
""", ask="¿Qué siente Cyan al ver retirarse a Queen?", opts=[
    M("Triunfo", "c3_bB7"),
    M("Un vacío enorme", "c3_bB7"),
])

ch.scene("c3_bB7", bg="c3_altar", text="""
De noche, sola en el altar, Cyan escucha un murmullo: miles de personas rezando y temiendo a la vez.
Ninguna de ellas le pregunta cómo está.
""", ask="¿Qué hace?", opts=[
    M("Seguir cantando", "c3_bB_fin"),
    M("Callarse por primera vez en años", "c3_bB_fin"),
])

ch.end("c3_bB_fin", "Fin del capítulo 3 (hilo alterado)", """
El culto de la Diosa Cian se extiende. El miedo encuentra un altar y una voz.
En TREEMAN, Shand toma nota. El miedo, al parecer, puede organizarse.
Voz: Has dado de comer al miedo. Y el miedo nunca está satisfecho.
""", bg="c3_altar", alt=True, set={"cyan_diosa": True})
