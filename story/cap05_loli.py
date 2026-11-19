"""Capítulo 5: Loli (episodios 13-14)."""
from engine.model import Chapter, C, M, X

ch = Chapter(5, "Loli", "Episodios 13-14", start="c5_00", color=(200, 90, 140), intro="""
Si la gente no cree en ti porque eres demasiado tierna, construye algo en lo que tenga que creer.
""")

ch.scene("c5_00", bg="fuera_del_tiempo", text="""
Voz: Un hilo rosa, enredado con tornillos y cables.
Voz: Esta chica todavía no lo sabe, pero lleva puesto un trozo del cielo.
""", next="c5_01")

# ---------------- EPISODIO 13: CHICA DURA ----------------
ch.scene("c5_01", bg="c5_cuarto_loli", text="""
Luo Li ve en la televisión un discurso de Queen sobre el esfuerzo y la dignidad.
[queen_caida] Es un video antiguo. Hoy, esa misma Queen es una zona prohibida del mapa. Aun así, sus palabras siguen siendo verdad.
[dos_expuesto] Desde que Queen expuso a DOS, sus discursos se ven más que nunca.
Luo Li: Quiero ser heroína.
""", ask="¿Qué hace Luo Li después del discurso?", opts=[
    C("Dibujar su primer diseño de heroína", "c5_02"),
    M("Practicar poses frente al espejo", "c5_02"),
    M("Contárselo a su padre", "c5_02", add={"rel_padre": 1}),
])

ch.scene("c5_02", bg="c5_audicion", text="""
Problema: Luo Li tiene cara de muñeca. La gente la encuentra adorable, pero nadie confía en que pueda pelear.
Su pulsera apenas se mueve.
Periodista: ¡Qué tierna! ¿Y cuál es tu poder, preciosa?
""", ask="¿Cómo responde Luo Li?", opts=[
    C("Inflar las mejillas, furiosa", "c5_03"),
    M("Responder con un dato técnico que nadie entiende", "c5_03", add={"genio": 1}),
    M("Irse sin responder", "c5_03"),
])

ch.scene("c5_03", bg="c5_laboratorio_padre", text="""
En el laboratorio de su padre, un científico, hay piezas extrañas que nadie sabe de dónde salieron.
Luo Li: Si no creen en mí... que crean en esto.
""", ask="¿Cómo construye su traje?", opts=[
    C("Con las piezas raras del laboratorio", "c5_04"),
    M("Con las piezas raras y un toque de diseño propio", "c5_04", add={"genio": 1}),
    M("Pidiendo permiso a su padre primero", "c5_04", add={"rel_padre": 1}),
])

ch.scene("c5_04", bg="c5_calle_noche", text="""
Nace 'Loli', una justiciera anónima con armadura mecánica. Patrulla de noche.
Ve a una chica acorralada en un callejón por una figura encapuchada que la ha estado siguiendo.
""", ask="¿Qué hace Loli?", opts=[
    C("Lanzarse contra el acosador", "c5_05"),
    M("Activar las luces del traje para asustarlo", "c5_05", add={"genio": 1}),
])

ch.scene("c5_05", bg="c5_calle_noche", text="""
El encapuchado huye con una velocidad inhumana. En el forcejeo, a Loli se le cae el casco.
La chica rescatada, Nuonuo, la mira fascinada.
Nuonuo: ¡Eres adorable!
""", ask="¿Cómo reacciona Loli?", opts=[
    C("Ponerse roja y recoger el casco", "c5_06", add={"rel_nuonuo": 1}),
    M("Exigirle que diga 'heroína', no 'adorable'", "c5_06"),
    M("Reírse con ella", "c5_06", add={"rel_nuonuo": 2}),
])

ch.scene("c5_06", bg="c5_glimmer_lab", text="""
Su padre le consigue un puesto en Glimmer Lab, un laboratorio de investigación.
El primer día, una cara conocida la saluda desde la otra mesa: es Nuonuo, que trabaja allí.
""", ask="¿Qué hace Loli?", opts=[
    C("Fingir que no la conoce", "c5_07"),
    M("Saludarla con entusiasmo", "c5_07", add={"rel_nuonuo": 1}),
    M("Esconderse detrás de un ordenador", "c5_07"),
])

ch.scene("c5_07", bg="c5_glimmer_lab", text="""
Nuonuo: ¡Tú eres la del casco! No te preocupes, no se lo diré a nadie.
Nuonuo le propone mejorar el traje juntas.
""", ask="¿Qué mejoras le hacen al traje?", opts=[
    C("Más blindaje y mejor movilidad", "c5_08"),
    M("Propulsores para volar", "c5_08", add={"genio": 1}),
    M("Un sistema de voz más grave para dar miedo", "c5_08"),
])

ch.scene("c5_08", bg="c5_glimmer_lab_ataque", text="""
Explosión. Un muro del laboratorio salta por los aires.
Entra DJ Shindig, un antiguo héroe número 1 caído en desgracia, con unos auriculares enormes y música atronadora.
DJ Shindig: ¿Dónde está el contenedor?
""", ask="¿Qué hace Loli?", opts=[
    C("Ponerse el traje enseguida", "c5_09"),
    M("Poner primero a salvo a los científicos", "c5_09"),
    M("Proteger a Nuonuo", "c5_09", add={"rel_nuonuo": 1}),
])

# ---------------- EPISODIO 14: CONTRAATAQUE IMPROVISADO ----------------
ch.scene("c5_09", bg="c5_glimmer_lab_ataque", text="""
El objetivo de Shindig es un contenedor de miedo almacenado en el laboratorio.
Nuonuo lo confunde con el acosador que la perseguía y se lanza contra él con una llave inglesa.
Nuonuo: ¡Tú otra vez!
""", ask="¿Cómo pelean Loli y Nuonuo juntas?", opts=[
    C("Loli ataca de frente y Nuonuo lo distrae", "c5_f1"),
    M("Nuonuo hackea el sistema de sonido mientras Loli golpea", "c5_f1", add={"rel_nuonuo": 1}),
])

ch.fight("c5_f1", "Loli y Nuonuo contra DJ Shindig", a="Loli", b="DJ Shindig", bg="c5_glimmer_lab_ataque", beats=[
    "Las ondas sonoras de Shindig revientan las ventanas.",
    "Loli resiste dentro del traje: las piezas extrañas absorben el impacto.",
    "Nuonuo le arranca un cable de los auriculares. Un segundo de silencio.",
    "Loli lo agarra del cuello y lo levanta por encima del contenedor.",
], next="c5_10")

ch.scene("c5_10", bg="c5_glimmer_lab_ataque", text="""
Shindig se retuerce. Debajo, el contenedor de miedo brilla con una luz enferma.
""", ask="¿Qué hace Loli?", opts=[
    C("Lanzarlo dentro del contenedor", "c5_11"),
    M("Lanzarlo contra la pared, pero el contenedor se rompe igual", "c5_11"),
])

ch.scene("c5_11", bg="c5_glimmer_lab_miedo", text="""
El contenedor se rompe. El miedo se derrama sobre Shindig y lo transforma en algo peor.
Llega un equipo de respuesta encabezado por Ghostblade, un héroe silencioso. Contienen el miedo, pero Shindig escapa.
Ghostblade mira a Nuonuo un segundo más de lo normal.
""", ask="¿Qué hace Loli?", opts=[
    C("Ayudar a contener el miedo", "c5_12"),
    M("Fijarse en que Ghostblade mira a Nuonuo", "c5_12", set={"vio_mirada": True}),
    M("Perseguir a Shindig, sin éxito", "c5_12"),
])

ch.scene("c5_12", bg="c5_glimmer_lab_miedo", text="""
Todos los que estaban cerca del miedo están mareados o llorando. Loli no.
Científico: Su traje... resiste el miedo. ¿De qué está hecho?
""", ask="¿Qué responde Loli?", opts=[
    C("'Piezas del laboratorio de mi padre'", "c5_13"),
    M("'Secreto industrial'", "c5_13"),
    M("'No lo sé... de verdad'", "c5_13", add={"rel_padre": 1}),
])

ch.scene("c5_13", bg="c5_comision", text="""
El padre de Loli se presenta ante la Comisión de Asuntos de Héroes.
Padre de Loli: Esas piezas vienen de un ovni que se estrelló hace años. Si resisten al miedo... podrían cambiarlo todo.
La Comisión le da permiso para investigar el lugar del accidente, en secreto.
""", ask="¿Qué piensa Loli del secreto?", opts=[
    C("Que su padre sabe lo que hace", "c5_14", add={"rel_padre": 1}),
    M("Que el mundo debería saberlo algún día", "c5_14"),
    X("Que el mundo debe saberlo YA: publicarlo todo", "c5_bA1", flag="loli_publica", ending="E08"),
])

ch.scene("c5_14", bg="c5_laboratorio_padre", text="""
Se organiza una expedición al ovni. Irán ella, su padre, Nuonuo y un equipo de seguridad.
Padre de Loli: Esto puede ser peligroso, hija. Quizá deberías quedarte.
""", ask="¿Qué responde Loli?", opts=[
    C("'Voy contigo. Soy heroína'", "c5_15"),
    M("'Voy. Alguien tiene que protegerte'", "c5_15", add={"rel_padre": 1}),
    X("'Tienes razón... y tú tampoco deberías ir'", "c5_bB1", flag="loli_renuncia", ending="E09"),
])

ch.scene("c5_15", bg="c5_glimmer_lab", text="""
Mientras preparan el equipo, la Organización Spotlight recibe de vuelta a Shindig, ahora lleno de miedo.
Loli recibe un mensaje: 'Nos vemos en el ovni'. Sin remitente.
""", ask="¿Qué hace con el mensaje?", opts=[
    C("Ignorarlo y seguir preparándose", "c5_16"),
    M("Contárselo a Nuonuo", "c5_16", add={"rel_nuonuo": 1}),
    M("Reforzar el traje esa misma noche", "c5_16", add={"genio": 1}),
])

ch.scene("c5_16", bg="c5_azotea_lab", text="""
La noche antes de partir, Loli y Nuonuo miran las estrellas desde la azotea del laboratorio.
Nuonuo: ¿Crees que allá arriba hay alguien que nos mira?
""", ask="¿Qué le responde Loli?", opts=[
    C("'Si lo hay, que se prepare'", "c5_fin"),
    M("'Seguro que sí. Y seguro que es raro'", "c5_fin", add={"rel_nuonuo": 1}),
])

ch.end("c5_fin", "Fin del capítulo 5", """
Loli entra en el ranking como número 6. Su traje no depende de la confianza... y eso asusta a más de uno.
La expedición parte hacia el ovni. Alguien la vigila desde las sombras, en silencio.
Voz: Un trozo del cielo en manos de una niña. Varias agencias acaban de ponerse nerviosas.
""", bg="c5_azotea_lab")

# ================= RAMA A: Loli lo publica todo =================
ch.scene("c5_bA1", bg="c5_cuarto_loli", text="""
Esa noche, Loli abre el portátil. Tiene escaneos de las piezas, informes de su padre y la grabación del laboratorio.
Luo Li: Si esto resiste el miedo, la gente tiene derecho a saberlo.
""", ask="¿Cómo lo publica?", opts=[
    M("De forma anónima", "c5_bA2"),
    M("Con su cara y su nombre", "c5_bA2", add={"genio": 1}),
])

ch.scene("c5_bA2", bg="c5_redes", text="""
El archivo se vuelve viral en horas. 'Material alienígena que suprime el miedo.' 'Las agencias lo sabían.'
Las pulseras de la ciudad empiezan a fluctuar de forma extraña.
""", ask="Su padre la llama, alarmado. ¿Qué le dice Loli?", opts=[
    M("'Lo siento, papá. Era lo correcto'", "c5_bA3", add={"rel_padre": 1}),
    M("'Tú también lo sabías y te callaste'", "c5_bA3", add={"rel_padre": -1}),
])

ch.scene("c5_bA3", bg="c5_glimmer_lab", text="""
Llegan agentes de la Comisión y de varias agencias al laboratorio. Quieren confiscar todo.
Nuonuo se pone delante de ella.
Nuonuo: No se la van a llevar.
""", ask="¿Qué hace Loli?", opts=[
    M("Ponerse el traje y negarse a entregarlo", "c5_bA4"),
    M("Entregar el traje para proteger a Nuonuo", "c5_bA4", add={"rel_nuonuo": 1}),
])

ch.scene("c5_bA4", bg="c5_redes", text="""
Las agencias lanzan una campaña: 'Fake news'. Pero los científicos independientes confirman los datos.
Los héroes del ranking empiezan a perder confianza a la vez. La gente se pregunta si los poderes son reales.
""", ask="¿Qué hace Loli ante el caos?", opts=[
    M("Dar una rueda de prensa explicando todo", "c5_bA5", add={"genio": 1}),
    M("Esconderse unos días con su padre", "c5_bA5", add={"rel_padre": 1}),
])

ch.scene("c5_bA5", bg="c5_calle_noche", text="""
DJ Shindig, lleno de miedo, ataca la ciudad. Pero esta vez los ciudadanos llevan placas fabricadas con copias del material y resisten.
Loli: ¡Funciona!
""", ask="¿Cómo enfrenta Loli a Shindig?", opts=[
    M("Junto a los ciudadanos", "c5_bA6"),
    M("Sola, para proteger a la gente", "c5_bA6"),
])

ch.scene("c5_bA6", bg="c5_comision", text="""
Shindig es detenido. La Comisión no puede ocultar nada más: convoca una sesión pública sobre el futuro del sistema de confianza.
Comisionado: Señorita Luo, ¿sabe lo que ha provocado?
""", ask="¿Qué responde Loli?", opts=[
    M("'Que la gente pueda defenderse sola'", "c5_bA7"),
    M("'Que dejen de mentir'", "c5_bA7"),
])

ch.scene("c5_bA7", bg="c5_azotea_lab", text="""
Nuonuo y Loli miran la ciudad. Muchas pantallas ya no muestran el ranking.
Nuonuo: ¿Y si ya nadie cree en los héroes?
""", ask="¿Qué responde Loli?", opts=[
    M("'Entonces tendremos que ganárnoslo de otra manera'", "c5_bA_fin"),
    M("'Mejor. Así nadie tendrá que fingir'", "c5_bA_fin"),
])

ch.end("c5_bA_fin", "Fin del capítulo 5 (hilo alterado)", """
La expedición al ovni se vuelve pública, con cámaras y periodistas. Nadie puede atacarla en secreto.
La confianza ya no es un dato sagrado. Es una pregunta.
Voz: Has puesto una lupa sobre las reglas del juego. Los jugadores no te lo perdonarán.
""", bg="c5_azotea_lab", alt=True, set={"ovni_publico": True})

# ================= RAMA B: Loli renuncia =================
ch.scene("c5_bB1", bg="c5_laboratorio_padre", text="""
Luo Li: Papá, si es peligroso para mí, también lo es para ti. Quédate.
Su padre la mira mucho rato.
Padre de Loli: Es la investigación de mi vida...
""", ask="¿Cómo lo convence?", opts=[
    M("Recordándole a su madre", "c5_bB2", add={"rel_padre": 1}),
    M("Diciéndole que ella lo necesita más que la ciencia", "c5_bB2", add={"rel_padre": 2}),
])

ch.scene("c5_bB2", bg="c5_laboratorio_padre", text="""
Su padre cede. Renuncian a la expedición. La Comisión envía a otro equipo, sin ellos.
Loli guarda el traje en una caja.
""", ask="¿Qué hace con el traje?", opts=[
    M("Guardarlo para siempre", "c5_bB3"),
    M("Guardarlo... pero dejar la caja sin cerrar", "c5_bB3", set={"traje_guardado": True}),
])

ch.scene("c5_bB3", bg="c5_glimmer_lab", text="""
Nuonuo se entera. Está dolida.
Nuonuo: ¿Te rindes? ¡Tú eras la heroína más genial que conocía!
""", ask="¿Qué le responde Loli?", opts=[
    M("'Prefiero ser una hija que una heroína'", "c5_bB4"),
    M("'Ven conmigo. Quédate tú también'", "c5_bB4", add={"rel_nuonuo": 1}),
])

ch.scene("c5_bB4", bg="c5_glimmer_lab", text="""
[rel_nuonuo>2] Nuonuo duda mucho, pero decide quedarse cerca de Loli.
[rel_nuonuo<=2] Nuonuo decide ir a la expedición de todos modos, como becaria.
Luo Li trabaja de día en el laboratorio. De noche, ya no patrulla.
""", ask="Una noche oye gritos en la calle. ¿Qué hace?", opts=[
    M("Llamar a los héroes y esperar", "c5_bB5"),
    M("Salir sin traje a ayudar", "c5_bB5", add={"genio": 1}),
])

ch.scene("c5_bB5", bg="c5_calle_noche", text="""
Es un pequeño robo. Lo resuelve sola, con una llave inglesa y mucha cara de enfado.
Un niño la mira.
Niño: ¿Eres una heroína?
""", ask="¿Qué le responde?", opts=[
    M("'No. Solo soy una vecina'", "c5_bB6"),
    M("'Algo así'", "c5_bB6"),
])

ch.scene("c5_bB6", bg="c5_laboratorio_padre", text="""
Su padre le prepara la cena. Hablan de ciencia, de su madre y de cosas pequeñas.
Padre de Loli: Gracias por no dejarme ir.
""", ask="¿Qué siente Loli?", opts=[
    M("Paz", "c5_bB7"),
    M("Paz... y una pizca de nostalgia por el traje", "c5_bB7"),
])

ch.scene("c5_bB7", bg="c5_azotea_lab", text="""
Mira las estrellas sola. En algún lugar, el ovni espera a otro equipo.
""", ask="¿Qué desea Loli?", opts=[
    M("Que todos vuelvan a salvo", "c5_bB_fin"),
    M("Que algún día el traje vuelva a servir para algo bueno", "c5_bB_fin"),
])

ch.end("c5_bB_fin", "Fin del capítulo 5 (hilo alterado)", """
Loli nunca entra en el ranking. Su padre vive. El traje duerme en una caja.
Voz: Una pieza que se retira a tiempo. Su padre tenía una cita con la muerte, y ahora no va a llegar.
""", bg="c5_azotea_lab", alt=True, set={"loli_retirada": True, "padre_loli_vivo": True})
