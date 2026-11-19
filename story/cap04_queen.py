"""Capítulo 4: Queen (episodios 11-12)."""
from engine.model import Chapter, C, M, X

ch = Chapter(4, "Queen", "Episodios 11-12", start="c4_00", color=(130, 30, 70), intro="""
Una niña prodigio, una lanza, una corona. Y un hombre sin nombre que se la arrebató.
""")

ch.scene("c4_00", bg="fuera_del_tiempo", text="""
Voz: Este hilo es rojo y está muy tenso. Es el de alguien que nunca se permitió perder.
Voz: Y es aquí donde aparezco por primera vez.
""", next="c4_01")

# ---------------- EPISODIO 11: EL CAMINO A LA CORONA ----------------
ch.scene("c4_01", bg="c4_graduacion", text="""
Liu Yuwei se gradúa de la universidad con catorce años. Las cámaras la adoran.
Entre el público no está su padre, Liu Zhen. Hace años que casi no se hablan.
""", ask="Le dan el micrófono. ¿Qué dice Liu Yuwei?", opts=[
    C("Un discurso perfecto y frío", "c4_02"),
    M("Un discurso sobre el esfuerzo de los demás", "c4_02", add={"humildad": 1}),
    M("Busca a su padre con la mirada antes de hablar", "c4_02", add={"rel_zhen": 1}),
])

ch.scene("c4_02", bg="c4_dos_oficina", text="""
Mickey, director de DOS, la recibe con los brazos abiertos.
Mickey: Con tu talento, en un año estarás en el top 10. Yo me encargo del resto.
""", ask="¿Qué le responde Liu Yuwei?", opts=[
    C("'En seis meses'", "c4_03"),
    M("'Solo si es por mis méritos'", "c4_03", add={"humildad": 1}),
    M("'¿Qué gana usted con esto?'", "c4_03", set={"sospecha_mickey": True}),
])

ch.scene("c4_03", bg="c4_ceremonia", text="""
Lo consigue: es la heroína más joven en entrar en el top 10. La prensa la corona con un nombre: Queen.
Su lanza crea un área donde ella dicta las reglas del mundo, dentro de ciertos límites.
""", ask="¿Cómo recibe el apodo 'Queen'?", opts=[
    C("Lo acepta como si siempre hubiera sido suyo", "c4_04"),
    M("Lo acepta con una leve sonrisa", "c4_04"),
    M("Dice que preferiría que la llamaran por su nombre", "c4_04", add={"humildad": 1}),
])

ch.scene("c4_04", bg="c4_torneo16", text="""
En DOS hay otra estrella: Bowa. Gana el 16.º Torneo de Héroes y no deja de recordárselo.
Bowa: La reina todavía tiene que aprender a hacer reverencias.
""", ask="¿Cómo trata Queen a Bowa?", opts=[
    C("Con indiferencia helada", "c4_05", add={"rel_bowa": -1}),
    M("Felicitándola de verdad", "c4_05", add={"rel_bowa": 1}),
    M("Retándola a entrenar juntas", "c4_05", add={"rel_bowa": 1}),
])

ch.scene("c4_05", bg="c4_torneo18", text="""
El 18.º Torneo de Héroes. Queen y Bowa son las favoritas.
Entre los participantes hay un hombre sin agencia ni historial. Nadie sabe quién es.
""", ask="Queen se cruza con el desconocido en el pasillo. ¿Qué hace?", opts=[
    C("Ignorarlo", "c4_06"),
    M("Analizarlo en silencio", "c4_06", set={"analizo_x": True}),
    M("Preguntarle su nombre", "c4_06", set={"hablo_x": True}),
])

ch.scene("c4_06", bg="c4_torneo18", text="""
[hablo_x] El hombre solo responde: 'Da igual'.
Queen y Bowa pelean juntas en la ronda final, contra él.
Queen: Lo terminaremos rápido.
""", ask="¿Cuál es la estrategia de Queen?", opts=[
    C("Atrapar al desconocido dentro de su área", "c4_f1"),
    M("Dejar que Bowa ataque primero", "c4_f1", add={"rel_bowa": -1}),
])

ch.fight("c4_f1", "Queen y Bowa contra el desconocido", a="Queen", b="X", bg="c4_torneo18", winner="b", beats=[
    "Queen despliega su área. Dentro, ella dicta las reglas.",
    "El desconocido mira a su alrededor... y el área simplemente deja de existir.",
    "Bowa ataca con todo. El hombre no se mueve; el espacio se pliega y ella sale despedida.",
    "Un instante. Las dos están en el suelo. Ni siquiera lo vieron moverse.",
    "El ranking se actualiza: un nuevo número 1. El mundo lo llamará X.",
], next="c4_07")

ch.scene("c4_07", bg="c4_cuarto_oscuro", text="""
Queen se encierra en su habitación durante semanas. Por primera vez en su vida, perdió sin entender cómo.
Su confianza baja. Ya no quiere salir.
""", ask="¿Qué hace Queen en su encierro?", opts=[
    C("Revisar la pelea mil veces", "c4_08"),
    M("Dormir y no hablar con nadie", "c4_08"),
    M("Llamar a su padre, aunque cuelga antes de que conteste", "c4_08", add={"rel_zhen": 1}),
])

ch.scene("c4_08", bg="c4_dos_pasillo", text="""
Bowa también cae. Descubre un secreto: Queen es hija de Liu Zhen, un hombre con mucha influencia en la sombra.
Bowa: Así que todo te lo regalaron.
[rel_bowa>0] A pesar de todo, Bowa le deja un mensaje: 'Dime que no es verdad'.
""", ask="Bowa la confronta por mensaje. ¿Qué responde Queen?", opts=[
    C("No responde", "c4_09", add={"rel_bowa": -1}),
    M("'Lo que tengo lo gané yo'", "c4_09"),
    M("'Mi padre y yo no nos hablamos. Créeme'", "c4_09", add={"rel_bowa": 1}),
])

# ---------------- EPISODIO 12: LA CAÍDA DE LA ESTRELLA ----------------
ch.scene("c4_09", bg="c4_entrenamiento", text="""
Queen sale de la oscuridad. Vuelve a entrenar y retoma un plan que había abandonado: encontrar la caja negra del avión que cayó años atrás.
""", ask="¿Por qué quiere esa caja negra?", opts=[
    C("Por justicia: nadie salvó a esos pasajeros", "c4_10"),
    M("Para ganarle a X algo que él no pueda quitarle", "c4_10"),
    X("Porque sospecha que su padre y DOS ocultan algo", "c4_bA1", flag="queen_expone", ending="E07"),
])

ch.scene("c4_10", bg="c4_noticias", text="""
Bowa reaparece consumida por el miedo. Está convencida de que todo el éxito de Queen viene de los contactos de Zhen.
Su confianza se ha convertido en pura oscuridad.
""", ask="Queen ve las noticias. ¿Qué hace?", opts=[
    C("Prepararse para el enfrentamiento", "c4_11"),
    M("Intentar contactar a Bowa", "c4_11", add={"rel_bowa": 1}),
    M("Pedirle a Mickey que la contenga", "c4_11"),
])

ch.scene("c4_11", bg="c4_calle_noche", text="""
La víspera del 19.º Torneo. Queen regresa sola a casa.
Bowa cae del cielo como una tormenta negra.
Bowa: ¡Esta noche no hay padre que te salve!
""", ask="¿Qué le dice Queen antes de pelear?", opts=[
    C("'Entonces lucha'", "c4_f2"),
    M("'Bowa, no tienes que hacer esto'", "c4_f2", add={"rel_bowa": 1}),
])

ch.fight("c4_f2", "Queen contra Bowa", a="Queen", b="Bowa", bg="c4_calle_noche", beats=[
    "Bowa golpea con una fuerza aumentada por el miedo. El asfalto se agrieta.",
    "Queen extiende su área: dentro, nadie puede volar. Bowa cae.",
    "Bowa rompe las reglas a base de odio. La lanza de Queen se dobla.",
    "Herida, Queen redefine el área una última vez: 'Aquí, el miedo no pesa'.",
    "Bowa se desploma. Queen también, cubierta de sangre.",
], next="c4_12")

ch.scene("c4_12", bg="c4_calle_noche", text="""
Bowa está en el suelo, vencida. Llegan las sirenas.
[rel_bowa>0] Bowa: Yo... solo quería que me miraras como a una igual.
[rel_bowa<=0] Bowa: Algún día perderás todo, como yo.
""", ask="¿Qué hace Queen con Bowa?", opts=[
    C("Dejar que la arresten", "c4_13"),
    M("Decirle algo amable mientras se la llevan", "c4_13", add={"rel_bowa": 1}),
    X("Tocar el miedo de Bowa para recuperar fuerzas", "c4_bB1", flag="queen_miedo", ending="E06"),
])

ch.scene("c4_13", bg="c4_hospital", text="""
Queen despierta en un hospital. Se perdió el 19.º Torneo.
En la televisión, X gana otra vez sin despeinarse.
""", ask="¿Cómo reacciona?", opts=[
    C("Apagar la televisión", "c4_14"),
    M("Mirar la pelea entera, analizándolo", "c4_14"),
    M("Reírse de sí misma por primera vez", "c4_14", add={"humildad": 1}),
])

ch.scene("c4_14", bg="c4_hospital", text="""
Mickey la visita con flores y una propuesta.
Mickey: Necesitas descansar. Unas vacaciones. Te acompañará Lucky Cyan.
[cyan_libre] Mickey: Bueno... iba a acompañarte una nueva cantante, pero nunca firmó con nosotros. Irás sola.
[cyan_diosa] Mickey: Y de paso, si encuentras rastros de esa 'diosa' que se le escapó a DOS, avísame.
""", ask="¿Acepta las vacaciones?", opts=[
    C("Aceptar sin sospechar nada", "c4_15"),
    M("Aceptar, aunque nota algo raro en Mickey", "c4_15", set={"sospecha_mickey": True}),
])

ch.scene("c4_15", bg="c4_carretera", text="""
[!cyan_libre&!cyan_diosa] Un viaje en coche por la montaña. Cyan canta y Queen, por fin, se relaja un poco.
[!cyan_libre&!cyan_diosa] Cyan: Gracias por encontrar la caja negra. Me devolviste mi historia.
[cyan_libre|cyan_diosa] Queen conduce sola por la montaña. El silencio le pesa más de lo que esperaba.
""", ask="¿De qué habla Queen durante el viaje?", opts=[
    C("De X y de cómo la venció", "c4_16"),
    M("De su padre", "c4_16", add={"rel_zhen": 1}),
    M("De nada; solo escucha", "c4_16"),
])

ch.scene("c4_16", bg="c4_carretera_noche", text="""
Al caer la noche, algo enorme se mueve entre los árboles. Ojos que brillan. Un rugido.
[!cyan_libre&!cyan_diosa] Cyan: ¿Eso es... un monstruo?
[cyan_libre|cyan_diosa] Queen está sola frente a la criatura.
""", ask="Un monstruo bloquea el camino. ¿Qué hace Queen?", opts=[
    C("Sacar la lanza y ponerse delante", "c4_fin"),
    M("Analizar al monstruo antes de atacar", "c4_fin"),
])

ch.end("c4_fin", "Fin del capítulo 4", """
La lanza de Queen brilla en la oscuridad. El monstruo ruge.
En la ciudad, Mickey cuelga el teléfono con una sonrisa: el viaje no era casual.
Voz: La reina sigue en el tablero. Pero alguien mueve sus pasos sin que ella lo sepa.
""", bg="c4_carretera_noche")

# ================= RAMA A: Queen investiga a su padre =================
ch.scene("c4_bA1", bg="c4_archivo", text="""
Queen entra de noche en los archivos de DOS. Busca cualquier cosa sobre el accidente aéreo.
Encuentra una carpeta con el nombre de su padre y otro nombre: 'Spotlight'.
""", ask="¿Qué hace con la carpeta?", opts=[
    M("Fotografiarla y salir", "c4_bA2"),
    M("Llevársela entera", "c4_bA2", set={"robo_carpeta": True}),
])

ch.scene("c4_bA2", bg="c4_archivo", text="""
La Organización Spotlight, los villanos de la ciudad, recibe dinero de DOS. Los 'enemigos' están en la nómina.
Queen siente que el suelo se abre bajo sus pies.
""", ask="¿A quién confronta primero?", opts=[
    M("A su padre", "c4_bA3", add={"rel_zhen": 1}),
    M("A Mickey", "c4_bA3"),
])

ch.scene("c4_bA3", bg="c4_casa_zhen", text="""
Liu Zhen la recibe en su casa. No niega nada.
Liu Zhen: Los héroes no salvaron a esa gente en el avión. Quería que el mundo viera lo que pasa cuando nadie cree. A veces hay que fabricar la oscuridad para que la gente busque la luz.
""", ask="¿Qué siente Queen?", opts=[
    M("Asco", "c4_bA4", add={"rel_zhen": -2}),
    M("Tristeza, porque una parte de ella lo entiende", "c4_bA4"),
])

ch.scene("c4_bA4", bg="c4_dos_oficina", text="""
Mickey se entera. La llama a su despacho.
Mickey: Si sale esto, DOS cae. Y tú caes con DOS, Queen. Piénsalo.
""", ask="¿Cómo responde Queen a la amenaza?", opts=[
    M("Fingir que obedece", "c4_bA5"),
    M("Romper su contrato delante de él", "c4_bA5", add={"humildad": -1}),
])

ch.scene("c4_bA5", bg="c4_estudio_tv", text="""
Queen consigue una transmisión en directo. Tiene las pruebas en la mano.
Antes de hablar, ve a Bowa en las noticias: arrestada por un ataque lleno de miedo, gritando el nombre de Zhen.
""", ask="¿Qué incluye en su declaración?", opts=[
    M("Todo, incluido el papel de su padre", "c4_bA6"),
    M("Todo, y una disculpa pública a Bowa", "c4_bA6", add={"rel_bowa": 2}),
])

ch.scene("c4_bA6", bg="c4_estudio_tv", text="""
La verdad estalla. Millones de pulseras tiemblan. La confianza en DOS se hunde. La de Queen, extrañamente, sube.
La Comisión de Asuntos de Héroes anuncia una investigación.
""", ask="Le preguntan si seguirá siendo heroína. ¿Qué responde?", opts=[
    M("'Una reina sin corona sigue teniendo lanza'", "c4_bA7"),
    M("'Seré lo que la gente necesite'", "c4_bA7", add={"humildad": 1}),
])

ch.scene("c4_bA7", bg="c4_carcel", text="""
Liu Zhen es detenido. Antes de entrar en el furgón, mira a su hija.
Liu Zhen: Al menos esta vez alguien dijo la verdad a tiempo.
""", ask="¿Qué le responde Queen?", opts=[
    M("Nada", "c4_bA_fin"),
    M("'Papá... gracias por salvar a esa niña'", "c4_bA_fin", add={"rel_zhen": 1}),
])

ch.end("c4_bA_fin", "Fin del capítulo 4 (hilo alterado)", """
DOS es intervenida. Mickey huye. La Organización Spotlight se queda sin financiación.
Queen no gana el torneo, pero gana algo más difícil: credibilidad.
Voz: La reina tiró del hilo que la ataba. Ahora el resto del tablero sabe que los hilos existen.
""", bg="c4_estudio_tv", alt=True, set={"dos_expuesto": True})

# ================= RAMA B: Queen toca el miedo =================
ch.scene("c4_bB1", bg="c4_calle_noche", text="""
Queen pone la mano sobre el pecho de Bowa. El miedo, espeso y frío, le sube por el brazo.
Su dolor desaparece. En su lugar queda una fuerza terrible.
""", ask="¿Qué siente Queen?", opts=[
    M("Poder, por fin", "c4_bB2"),
    M("Miedo... y le gusta", "c4_bB2"),
])

ch.scene("c4_bB2", bg="c4_hospital", text="""
Despierta en el hospital, curada en horas. Los médicos no lo entienden.
Su área ha cambiado: ahora es oscura, y dentro de ella la gente siente terror.
""", ask="¿Le cuenta a alguien lo que le pasó?", opts=[
    M("No. Es su secreto", "c4_bB3"),
    M("Se lo cuenta a Mickey", "c4_bB3", set={"mickey_sabe": True}),
])

ch.scene("c4_bB3", bg="c4_torneo19", text="""
[mickey_sabe] Mickey sonríe: 'Esto es justo lo que necesitábamos'.
Queen se presenta al 19.º Torneo. Sus rivales salen de su área temblando, incapaces de pelear.
Locutor: ¡Queen llega a la final! ¡Contra X!
""", ask="Frente a X, ¿qué hace Queen?", opts=[
    M("Encerrarlo en su área de miedo", "c4_bB4"),
    M("Preguntarle si él también tiene miedo", "c4_bB4"),
])

ch.scene("c4_bB4", bg="c4_torneo19", text="""
X entra en el área. La mira sin miedo, con algo parecido a la lástima.
X: No eres tú la que habla.
Un segundo y ella está en el suelo. Otra vez.
""", ask="Derrotada, ¿qué hace Queen?", opts=[
    M("Gritar de rabia", "c4_bB5"),
    M("Dejar que el miedo la cubra por completo", "c4_bB5"),
])

ch.scene("c4_bB5", bg="c4_ciudad_oscura", text="""
El miedo ya no le obedece: la domina. Su área se expande por la ciudad. Las pulseras marcan números negativos.
[!cyan_libre&!cyan_diosa] Lucky Cyan intenta alcanzarla con su voz, pero la canción no atraviesa la oscuridad.
""", ask="¿Queda algo de Liu Yuwei dentro de Queen?", opts=[
    M("Un recuerdo de su graduación", "c4_bB6"),
    M("La voz de su padre", "c4_bB6", add={"rel_zhen": 1}),
])

ch.scene("c4_bB6", bg="c4_ciudad_oscura", text="""
Queen se aleja de la ciudad antes de destruirla del todo. Una última decisión propia.
Se instala en las ruinas de un estadio abandonado. Su área llega a varios kilómetros.
""", ask="¿Qué hace con quienes se acercan?", opts=[
    M("Expulsarlos con terror", "c4_bB7"),
    M("Dejarlos pasar si no tienen miedo", "c4_bB7"),
])

ch.scene("c4_bB7", bg="c4_ciudad_oscura", text="""
La llaman 'La Reina del Miedo'. La Comisión la clasifica como amenaza de nivel máximo.
En su trono de escombros, Queen mira el cielo sin estrellas.
""", ask="¿Qué piensa?", opts=[
    M("Que por fin nadie le regala nada", "c4_bB_fin"),
    M("Que ojalá alguien viniera a detenerla", "c4_bB_fin"),
])

ch.end("c4_bB_fin", "Fin del capítulo 4 (hilo alterado)", """
Queen ya no es la número 2. Es una zona del mapa a la que nadie quiere ir.
Voz: Cuando la heroína más fuerte después de mí cae en el miedo, nadie va a detener lo que viene.
""", bg="c4_ciudad_oscura", alt=True, set={"queen_caida": True})
