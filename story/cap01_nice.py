"""Capítulo 1: Nice (episodios 1-4)."""
from engine.model import Chapter, C, M, X

ch = Chapter(1, "Nice", "Episodios 1-4", start="c1_00", color=(30, 70, 140), intro="""
En un mundo donde la confianza de la gente se convierte en poder, el héroe con más confianza recibe un nombre: X.
Lin Ling no es nadie. Está a punto de volverse alguien a la fuerza.
""")

ch.scene("c1_00", bg="fuera_del_tiempo", text="""
Un lugar sin arriba ni abajo. Relojes que flotan, ciudades suspendidas como piezas de un tablero.
Voz: Mira con atención. Cada héroe es un hilo, y cada hilo está enredado con los demás.
Voz: Si tiras de uno, todos se mueven. Empecemos por el más común de todos.
""", next="c1_01")

# ---------------- EPISODIO 1: NICE ----------------
ch.scene("c1_01", bg="c1_azotea", text="""
Noche. Una azotea en el centro de la ciudad. Lin Ling acaba de perder su trabajo y lleva una caja de cartón con sus cosas.
Su pulsera marca una confianza casi nula. Se asoma al borde.
Lin Ling: Nadie se daría cuenta si desapareciera...
""", ask="Lin Ling está en el borde de la azotea. ¿Qué hace?", opts=[
    C("Quedarse inmóvil, mirando el vacío", "c1_02"),
    M("Dar un paso atrás y respirar hondo", "c1_02", add={"valor": 1}),
    M("Sacar el teléfono para llamar a alguien... y no encontrar a nadie", "c1_02", add={"soledad": 1}),
])

ch.scene("c1_02", bg="c1_azotea", text="""
Una silueta pasa volando a su lado: es Nice, el héroe perfecto, el número 15 del ranking.
Nice no lo rescata. Se para en la cornisa, sonríe a nadie... y salta.
Lin Ling se queda paralizado. Abajo, el silencio. Detrás de él, unos tacones.
Miss J: Tú. Mírame. Viste algo que no deberías haber visto.
""", ask="Miss J, la representante de Nice, lo acorrala. ¿Cómo reacciona Lin Ling?", opts=[
    C("Tartamudear sin saber qué decir", "c1_03"),
    M("Exigirle que llame a una ambulancia", "c1_03", add={"rel_missj": -1}),
    X("Salir corriendo para contárselo a la prensa", "c1_bA1", flag="lin_confiesa", ending="E02"),
])

ch.scene("c1_03", bg="c1_treeman_oficina", text="""
Lin Ling despierta atado a una silla en la sede de TREEMAN. Delante de él está Shand, el director.
Shand: Nice no puede morir. Su confianza vale millones. Y tú te pareces bastante a él con el traje puesto.
Miss J: O te conviertes en Nice o desapareces con él. Tú eliges.
""", ask="¿Qué responde Lin Ling?", opts=[
    C("Aceptar ser Nice", "c1_04"),
    M("Aceptar, pero pedir un sueldo decente", "c1_04", add={"rel_missj": 1}),
    M("Aceptar en silencio, temblando", "c1_04", add={"soledad": 1}),
])

ch.scene("c1_04", bg="c1_entrenamiento", text="""
Días de entrenamiento: la sonrisa de Nice, su forma de saludar, su forma de caminar. Miss J lo corrige sin descanso.
Cuando se pone el traje, algo pasa: la confianza del público fluye hacia él. Puede volar.
Miss J: La gente no cree en ti. Cree en Nice. No lo olvides nunca.
""", ask="¿Cómo afronta Lin Ling su nuevo papel?", opts=[
    C("Imitar a Nice a la perfección", "c1_05"),
    M("Imitarlo, pero añadirle algo de sí mismo", "c1_05", add={"valor": 1}),
    M("Preguntar por qué Nice saltó", "c1_05", add={"rel_missj": -1}),
])

ch.scene("c1_05", bg="c1_plaza_fans", text="""
Primera aparición pública. Cientos de fans gritan su nombre... el nombre de otro.
Una niña le pide un autógrafo con los ojos brillantes.
Fan: ¡Nice! ¡Tú me salvaste el año pasado!
""", ask="¿Cómo responde Lin Ling a la niña?", opts=[
    C("Firmar con la sonrisa perfecta de Nice", "c1_06"),
    M("Firmar y preguntarle su nombre de verdad", "c1_06", add={"valor": 1}),
    M("Firmar con prisa, incómodo", "c1_06"),
])

ch.scene("c1_06", bg="c1_set_tv", text="""
Un programa de entrevistas. A su lado se sienta Moon, una heroína con fama de ser la novia de Nice.
Moon sonríe a la cámara, pero cuando nadie mira, le clava una mirada helada.
Moon: No sé quién eres. Pero no eres él.
""", ask="Moon le susurra durante la pausa comercial. ¿Qué hace Lin Ling?", opts=[
    C("Seguir actuando como si nada", "c1_07"),
    M("Susurrarle: 'Por favor, ayúdame'", "c1_07", add={"rel_moon": 1}),
    M("Responderle con frialdad", "c1_07", add={"rel_moon": -1}),
])

ch.scene("c1_07", bg="c1_calle_caos", text="""
Al salir del estudio, una explosión. Su antiguo jefe, el hombre que lo despidió, se ha convertido en un villano consumido por el miedo.
Shand llama por el auricular.
Shand: Es tu oportunidad. Derrótalo en directo.
""", ask="El ex-jefe destroza la calle. ¿Qué hace Lin Ling?", opts=[
    C("Lanzarse a pelear", "c1_f1"),
    M("Evacuar primero a los civiles y luego pelear", "c1_f1", add={"valor": 1}),
    M("Dudar, pero el público lo empuja a pelear", "c1_f1"),
])

ch.fight("c1_f1", "Nice contra el ex-jefe", a="Lin Ling", b="Ex-jefe", bg="c1_calle_caos", beats=[
    "El ex-jefe lanza un coche. Lin Ling lo esquiva volando por primera vez en combate.",
    "Los gritos de los fans le dan fuerza. Cada '¡Nice!' es un golpe más fuerte.",
    "El villano le escupe todo su desprecio: 'Siempre fuiste un inútil'.",
    "Lin Ling lo derriba de un puñetazo. El miedo abandona el cuerpo del hombre.",
], next="c1_08")

ch.scene("c1_08", bg="c1_noticias", text="""
Las pantallas de la ciudad repiten su victoria. Pero el último titular lo deja helado: Moon fue encontrada sin vida.
Miss J: No preguntes. Sonríe y sigue.
""", ask="¿Qué hace Lin Ling con la noticia?", opts=[
    C("Ir a buscar respuestas por su cuenta", "c1_09"),
    M("Preguntarle a Miss J directamente", "c1_09", add={"rel_missj": -1}),
    M("Llorar en silencio dentro del traje", "c1_09", add={"soledad": 1}),
])

# ---------------- EPISODIO 2: MOON ----------------
ch.scene("c1_09", bg="c1_departamento_moon", text="""
Moon está viva. Lo espera en su departamento con los brazos cruzados.
[rel_moon>0] Moon: Me pediste ayuda. Por eso sigues entero.
[rel_moon<0] Moon: Con esa actitud tuya, debería entregarte ahora mismo.
Moon: Nuestra relación era falsa. Un contrato. Y sé que Nice está muerto.
""", ask="Moon lo sabe todo. ¿Qué le dice Lin Ling?", opts=[
    C("Contarle la verdad sobre la azotea", "c1_10", add={"rel_moon": 1}),
    M("Contarle solo una parte", "c1_10"),
    M("Pedirle que no lo delate, de rodillas", "c1_10", add={"rel_moon": -1}),
])

ch.scene("c1_10", bg="c1_cuarto_cerrado", text="""
Miss J los encierra a los dos en un cuarto. La agencia quiere una boda: la noticia dispararía la confianza.
Moon: Los dos queremos ser libres. Hagamos un trato.
""", ask="¿Qué plan propone Lin Ling?", opts=[
    C("Fingir la propuesta y luego la muerte de Moon", "c1_11"),
    M("Fingir la propuesta y ganar tiempo", "c1_11"),
    M("Dejar que Moon decida el plan", "c1_11", add={"rel_moon": 1}),
])

ch.scene("c1_11", bg="c1_azotea_propuesta", text="""
La propuesta se transmite en vivo y la ciudad se derrite de ternura. Luego, la falsa muerte de Moon.
La noticia atrae a Wreck, el rival fabricado de Nice. Cuando descubre que el Nice de verdad se suicidó, enloquece.
Wreck: ¡Entonces toda mi vida fue una mentira!
""", ask="Wreck se vuelve berserk. ¿Qué hace Lin Ling?", opts=[
    C("Enfrentarlo", "c1_f2"),
    M("Intentar calmarlo antes de pelear", "c1_f2", add={"valor": 1}),
    M("Pedirle a Moon que se aleje", "c1_f2", add={"rel_moon": 1}),
])

ch.fight("c1_f2", "Nice contra Wreck", a="Lin Ling", b="Wreck", bg="c1_azotea_propuesta", beats=[
    "Wreck destroza la azotea. Llevaba años odiando a un héroe que ni siquiera lo conocía.",
    "Lin Ling recibe un golpe brutal y atraviesa un anuncio luminoso.",
    "Se levanta. 'Yo tampoco soy quien crees', le dice.",
    "Un último choque. Wreck pierde el equilibrio y cae al vacío.",
], next="c1_12")

ch.scene("c1_12", bg="c1_azotea_propuesta", text="""
Lin Ling se asoma al borde. Abajo ya no queda nada de Wreck.
Moon se teletransporta lejos sin despedirse. En otra parte de la ciudad, un periodista llamado Enlighter se une en secreto a la Organización Spotlight y adopta un nuevo nombre: God Eye.
""", ask="Lin Ling se queda solo en la azotea. ¿Qué piensa?", opts=[
    C("Que tiene que seguir siendo Nice, aunque duela", "c1_13"),
    M("Que algún día va a contar la verdad", "c1_13", add={"valor": 1}),
    M("Que Moon fue la única persona sincera con él", "c1_13", add={"rel_moon": 1}),
])

# ---------------- EPISODIO 3: EL HÉROE INQUEBRANTABLE ----------------
ch.scene("c1_13", bg="c1_estatua", text="""
Nueva misión: capturar a Wolf Girl, que planea volar la estatua de Firm-Man, el héroe inquebrantable.
Si Nice lo logra, entrará en el top 10.
Wolf Girl: Un paso más y el niño cae.
Tiene a un niño como rehén en lo alto de la estatua.
""", ask="Wolf Girl amenaza al rehén. ¿Cómo actúa Lin Ling?", opts=[
    C("Hablar con ella para entender por qué lo hace", "c1_14"),
    M("Acercarse despacio, con las manos en alto", "c1_14"),
    M("Gritarle que suelte al niño", "c1_14", add={"valor": -1}),
])

ch.scene("c1_14", bg="c1_estatua", text="""
Lin Ling lo entiende: Wolf Girl fue la primera persona a la que Firm-Man rescató. Quiere que él pierda su 'inquebrantabilidad', porque ese poder lo está destruyendo por dentro.
Firm-Man pierde sus poderes. La estatua gigante empieza a caer sobre la multitud.
""", ask="La estatua se viene abajo. ¿Qué hace Lin Ling?", opts=[
    C("Atrapar la estatua con todas sus fuerzas", "c1_f3"),
    M("Gritarle a la gente que corra y después atraparla", "c1_f3", add={"valor": 1}),
])

ch.fight("c1_f3", "Nice contra la estatua de Firm-Man", a="Lin Ling", b="Estatua", bg="c1_estatua", beats=[
    "Toneladas de piedra se desploman sobre la plaza.",
    "Lin Ling vuela debajo y la sostiene. Sus brazos crujen.",
    "La multitud empieza a gritar su nombre... el de Nice. La confianza sube como una marea.",
    "La estatua queda en pie. El ranking se actualiza: Nice, número 10.",
], next="c1_15")

ch.scene("c1_15", bg="c1_noticias", text="""
Lin Ling celebra su entrada en el top 10 con una sonrisa prestada.
Entonces todas las pantallas se apagan. Aparece God Eye.
God Eye: Nice. Tengo a tu prometida. Ven solo o la ciudad verá cómo muere de verdad.
""", ask="God Eye ha secuestrado a 'Moon'. ¿Qué hace Lin Ling?", opts=[
    C("Ir a rescatarla", "c1_16"),
    M("Pedirle refuerzos a Shand", "c1_16", add={"rel_missj": 1}),
    M("Ir, aunque sospecha que es una trampa", "c1_16", add={"valor": 1}),
])

# ---------------- EPISODIO 4: EL HOMBRE COMÚN ----------------
ch.scene("c1_16", bg="c1_estadio", text="""
Shand envía a Blankster, un héroe que puede borrar recuerdos, para limpiar el desastre. God Eye lo vence en segundos: expone sus trampas del pasado frente a todos y su confianza se derrumba.
God Eye: Ahora tú, Nice. Dile al mundo quién eres de verdad.
Las cámaras lo enfocan. Millones de pulseras esperan.
""", ask="Todo el mundo está mirando. ¿Qué hace Lin Ling?", opts=[
    C("Confesar en directo que Nice se suicidó", "c1_f4"),
    M("Confesar y señalar también a TREEMAN", "c1_f4", add={"rel_missj": -2}),
])

ch.fight("c1_f4", "El Hombre Común contra God Eye", a="Lin Ling", b="God Eye", bg="c1_estadio", beats=[
    "Sin la confianza de Nice, Lin Ling no tiene poderes. God Eye lo derriba una y otra vez.",
    "Se levanta. Cae. Se levanta. La gente empieza a mirar al hombre, no al traje.",
    "Grita la verdad: ama a Moon, aunque todo lo demás fuera mentira.",
    "Una pulsera, luego diez, luego mil: la gente cree en Lin Ling.",
    "Un puñetazo de hombre común derrota a God Eye. La Moon secuestrada era falsa.",
], next="c1_17")

ch.scene("c1_17", bg="c1_estadio", text="""
Los periodistas le preguntan qué nombre de héroe va a usar ahora.
Lin Ling: No soy Nice. Soy... un hombre común.
""", ask="¿Cómo se presenta ante el mundo?", opts=[
    C("Como 'El Hombre Común'", "c1_18"),
    M("Como 'El Hombre Común', con la voz temblorosa", "c1_18", add={"soledad": 1}),
    M("Como 'El Hombre Común', con el puño en alto", "c1_18", add={"valor": 1}),
])

ch.scene("c1_18", bg="c1_callejon_lluvia", text="""
Lin Ling encuentra a la verdadera Moon en un callejón, bajo la lluvia.
[rel_moon>1] Moon corre hacia él. Por primera vez, su sonrisa no es para las cámaras.
[rel_moon<=1] Moon lo mira con cautela, pero no se va.
Un destello azul ilumina el callejón. Es E-Soul, el héroe del relámpago.
""", ask="E-Soul levanta la mano hacia Moon. ¿Qué hace Lin Ling?", opts=[
    C("Correr hacia ella... pero no llega a tiempo", "c1_fin"),
    X("Usar toda su confianza para lanzarse entre Moon y el relámpago", "c1_bB1",
      flag="moon_salvada", ending="E03"),
])

ch.end("c1_fin", "Fin del capítulo 1", """
El relámpago cae. Moon muere en los brazos de Lin Ling.
E-Soul desaparece sin decir una palabra.
Voz: Un hombre común ha subido al tablero. Pero para entender ese relámpago hay que mirar otro hilo.
""", bg="c1_callejon_lluvia")

# ================= RAMA A: Lin Ling huye y cuenta la verdad =================
ch.scene("c1_bA1", bg="c1_calle_noche", text="""
Lin Ling baja las escaleras de la azotea a toda velocidad, con el corazón en la garganta.
Miss J: ¡Atrápenlo!
Dos guardias de TREEMAN lo persiguen por la avenida.
""", ask="¿Hacia dónde escapa?", opts=[
    M("Hacia el metro, entre la multitud", "c1_bA2"),
    M("Hacia un callejón oscuro", "c1_bA2", add={"valor": 1}),
])

ch.scene("c1_bA2", bg="c1_cafe", text="""
Lo despista. En un café de 24 horas busca en internet a un periodista que se atreva con la historia.
Hay un nombre que se repite en artículos incómodos: Enlighter.
""", ask="¿A quién contacta?", opts=[
    M("A Enlighter", "c1_bA3", set={"contacto_enlighter": True}),
    M("A un canal de noticias pequeño e independiente", "c1_bA3"),
])

ch.scene("c1_bA3", bg="c1_cafe", text="""
[contacto_enlighter] Enlighter le responde enseguida, demasiado rápido. Le pide pruebas.
[!contacto_enlighter] El canal independiente le pide pruebas antes de publicar nada.
Lin Ling no tiene nada. Solo su palabra. Y la confianza que marca su pulsera es casi cero.
""", ask="¿Cómo consigue pruebas?", opts=[
    M("Volver a la azotea a buscar cámaras de seguridad", "c1_bA4"),
    M("Buscar a Moon, la 'novia' de Nice", "c1_bA4", add={"rel_moon": 1}),
])

ch.scene("c1_bA4", bg="c1_departamento_moon", text="""
Moon lo encuentra antes que él a ella. Se teletransporta delante de él.
Moon: TREEMAN te está buscando. Yo también quiero salir de su contrato.
Moon: Tengo las grabaciones de la azotea. Pero si las publicamos, nos van a destruir a los dos.
""", ask="¿Publican las pruebas?", opts=[
    M("Sí, ahora mismo", "c1_bA5"),
    M("Sí, pero primero ponen a salvo a Moon", "c1_bA5", add={"rel_moon": 1}),
])

ch.scene("c1_bA5", bg="c1_noticias", text="""
El video se vuelve viral en minutos: Nice saltando y TREEMAN ocultándolo.
La confianza de la agencia se desploma. La de Lin Ling sube un poco: la gente quiere creerle al testigo.
Shand aparece en televisión acusándolo de mentir.
""", ask="¿Cómo responde Lin Ling ante las acusaciones?", opts=[
    M("Dar la cara con su propio nombre", "c1_bA6", add={"valor": 1}),
    M("Dejar que las pruebas hablen solas", "c1_bA6"),
])

ch.scene("c1_bA6", bg="c1_calle_caos", text="""
Esa noche, un villano consumido por el miedo ataca su edificio. Es su antiguo jefe. Alguien le dio la dirección.
Moon: ¡Esto es cosa de Shand!
Lin Ling no tiene poderes de héroe. Solo una escoba y unas ganas tremendas de vivir.
""", ask="El villano lo acorrala. ¿Qué hace?", opts=[
    M("Hacerle frente y transmitirlo en vivo", "c1_bA7"),
    M("Proteger a los vecinos y huir con ellos", "c1_bA7", add={"valor": 1}),
])

ch.scene("c1_bA7", bg="c1_calle_caos", text="""
Mientras la transmisión crece, la gente le cree. La confianza fluye y, sin traje ni máscara, Lin Ling logra derribar al villano.
Shand llega con abogados y cámaras para negociar.
Shand: Únete a nosotros con tu nombre real. Lo olvidaremos todo.
""", ask="¿Qué le responde a Shand?", opts=[
    M("'No.' Y le cierra la puerta", "c1_bA_fin"),
    M("'Nunca.' Y lo dice mirando a la cámara", "c1_bA_fin", add={"valor": 1}),
])

ch.end("c1_bA_fin", "Fin del capítulo 1 (hilo alterado)", """
TREEMAN pierde la mitad de su confianza en una semana. Nice muere de verdad para el público, y nadie ocupa su lugar.
Moon rompe su contrato y se va de la ciudad. Lin Ling sigue siendo un hombre común, pero un hombre libre.
Voz: Interesante. Has tirado de un hilo que no debía moverse. Todo lo demás temblará.
""", bg="c1_noticias", alt=True, set={"treeman_expuesto": True, "moon_viva": True})

# ================= RAMA B: Lin Ling salva a Moon =================
ch.scene("c1_bB1", bg="c1_callejon_lluvia", text="""
El relámpago le atraviesa la espalda. El dolor es blanco. Pero Moon está viva detrás de él.
E-Soul lo mira, sorprendido. Por primera vez, duda.
""", ask="Lin Ling, herido, se enfrenta a E-Soul. ¿Qué le dice?", opts=[
    M("'¿Quién te envió?'", "c1_bB2"),
    M("'Si quieres matarla, tendrás que matarme a mí'", "c1_bB2", add={"valor": 1}),
])

ch.scene("c1_bB2", bg="c1_callejon_lluvia", text="""
E-Soul no responde. Prepara otro relámpago.
Moon agarra la mano de Lin Ling.
Moon: Agárrate fuerte.
""", ask="¿Qué hace Lin Ling?", opts=[
    M("Agarrarse a Moon y cerrar los ojos", "c1_bB3", add={"rel_moon": 1}),
    M("Empujarla para que se vaya sola", "c1_bB3"),
])

ch.scene("c1_bB3", bg="c1_bosque", text="""
[rel_moon>1] Se teletransportan juntos a un bosque a las afueras.
[rel_moon<=1] Moon no lo suelta y se teletransportan juntos a un bosque a las afueras.
La herida de Lin Ling humea. Moon le rompe un trozo de su capa para vendarlo.
""", ask="Mientras Moon lo cura, ¿de qué hablan?", opts=[
    M("De por qué alguien quiere matarla", "c1_bB4"),
    M("De lo que harían si fueran libres", "c1_bB4", add={"rel_moon": 1}),
])

ch.scene("c1_bB4", bg="c1_bosque", text="""
Moon: Sé cosas, Lin Ling. Cosas de TREEMAN, de otras agencias... de cómo se fabrica la confianza.
Moon: Por eso enviaron a E-Soul. No soy una heroína. Soy un cabo suelto.
""", ask="¿Qué deciden hacer con ese secreto?", opts=[
    M("Guardarlo como seguro de vida", "c1_bB5"),
    M("Olvidarlo y empezar de cero", "c1_bB5", add={"rel_moon": 1}),
])

ch.scene("c1_bB5", bg="c1_pueblo_mar", text="""
Semanas después, en un pueblo junto al mar. Nadie los reconoce sin sus trajes.
La pulsera de Lin Ling marca una confianza pequeña: la del panadero, la de los pescadores, la de Moon.
""", ask="¿Vuelve Lin Ling a ser héroe?", opts=[
    M("No. Se queda en el pueblo", "c1_bB6"),
    M("Solo si alguien del pueblo lo necesita", "c1_bB6", add={"valor": 1}),
])

ch.scene("c1_bB6", bg="c1_pueblo_mar", text="""
Una noche, Moon le enseña un mensaje anónimo: 'Sabemos dónde estás'.
Moon: Podemos huir otra vez. O podemos grabar un último mensaje para que, si nos pasa algo, todo salga a la luz.
""", ask="¿Qué eligen?", opts=[
    M("Grabar el mensaje y quedarse", "c1_bB7", add={"valor": 1}),
    M("Huir otra vez, juntos", "c1_bB7", add={"rel_moon": 1}),
])

ch.scene("c1_bB7", bg="c1_pueblo_mar", text="""
Lin Ling mira el mar. Ya no es Nice. Tampoco es El Hombre Común de las noticias.
Moon: ¿Te arrepientes?
""", ask="¿Qué le responde?", opts=[
    M("'De nada'", "c1_bB_fin"),
    M("'Solo de no haberte conocido antes'", "c1_bB_fin", add={"rel_moon": 1}),
])

ch.end("c1_bB_fin", "Fin del capítulo 1 (hilo alterado)", """
Moon sobrevive. Lin Ling desaparece del ranking. TREEMAN anuncia que Nice se retira por motivos personales.
En algún lugar, E-Soul informa de que falló su misión.
Voz: Una muerte que no ocurrió es una pieza que sigue en el tablero. Eso lo cambia todo.
""", bg="c1_pueblo_mar", alt=True, set={"moon_viva": True, "lin_retirado": True})
