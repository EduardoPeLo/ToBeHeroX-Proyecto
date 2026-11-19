"""Capítulo 7: Los Johnnies (episodios 17-18)."""
from engine.model import Chapter, C, M, X

ch = Chapter(7, "Los Johnnies", "Episodios 17-18", start="c7_00", color=(160, 100, 30), intro="""
Un niño que habla con los animales. Un monstruo del espacio que lo quiere como a un hermano. Y un padre que nunca volvió a casa.
""")

ch.scene("c7_00", bg="fuera_del_tiempo", text="""
Voz: Este es el hilo más antiguo del tablero. Empieza antes que todos los demás.
Voz: Aquí ocurrió el primer crimen de esta historia.
""", next="c7_01")

# ---------------- EPISODIO 17: FLOR SUSURRANTE ----------------
ch.scene("c7_01", bg="c7_casa_ciudad", text="""
Ah Sheng, el héroe número 1 de su época, llega a casa con una jaula. Dentro hay una criatura pequeña, peluda, de ojos enormes.
Ah Sheng: La atrapé en una misión. Ahora es tuya, hijo.
El pequeño Johnny se acerca. La criatura le habla... y él la entiende.
""", ask="¿Qué hace Little Johnny?", opts=[
    C("Abrir la jaula", "c7_02"),
    M("Meter la mano para acariciarla", "c7_02", add={"rel_big": 1}),
    M("Preguntarle si tiene hambre", "c7_02", add={"rel_big": 1}),
])

ch.scene("c7_02", bg="c7_casa_ciudad", text="""
La criatura salta a sus brazos. Necesita un nombre.
Ah Sheng: Tú eres 'Johnny'. Él será... ¿cómo lo llamamos?
""", ask="¿Qué nombre elige?", opts=[
    C("'Big Johnny', como su hermano mayor", "c7_03"),
    M("'Big Johnny'... después de pensarlo mucho", "c7_03"),
])

ch.scene("c7_03", bg="c7_hospital", text="""
La madre de Johnny enferma. Una noche, ya no despierta.
Ah Sheng aprieta los puños. Big Johnny se acurruca en el regazo del niño.
""", ask="¿Cómo afronta Little Johnny la pérdida?", opts=[
    C("Abrazar a Big Johnny toda la noche", "c7_04", add={"rel_big": 1}),
    M("Abrazar a su padre", "c7_04", add={"rel_padre_j": 1}),
    M("No llorar delante de nadie", "c7_04"),
])

ch.scene("c7_04", bg="c7_campo", text="""
Padre e hijo dejan la ciudad. Se mudan al campo, lejos del ranking, de las cámaras y de los recuerdos.
Little Johnny aprende a hablar con los pájaros, las vacas y los perros del pueblo.
""", ask="¿Qué es lo que más le gusta del campo?", opts=[
    C("Correr por los campos con Big Johnny", "c7_05", add={"rel_big": 1}),
    M("Escuchar las historias de los animales", "c7_05"),
    M("Que su padre por fin está en casa", "c7_05", add={"rel_padre_j": 1}),
])

ch.scene("c7_05", bg="c7_campo_casa", text="""
Un día llega Vortex, el héroe que heredó el número 1. Necesita la ayuda de Ah Sheng contra un rival peligroso.
Ah Sheng: Ya no soy héroe, Vortex. Ahora soy padre.
Vortex se va, serio. Little Johnny lo ve todo desde la ventana.
""", ask="¿Qué piensa Little Johnny de Vortex?", opts=[
    C("Que es un hombre peligroso", "c7_06", add={"odio_vortex": 1}),
    M("Que parecía preocupado", "c7_06"),
    M("Que su padre hizo bien en negarse", "c7_06", add={"rel_padre_j": 1}),
])

ch.scene("c7_06", bg="c7_campo_noche", text="""
Esa noche, Ah Sheng no vuelve. Lo encuentran muerto frente a su propia casa.
Hay cortes limpios en la tierra y en los árboles. Cortes de espada.
""", ask="Little Johnny ve el cuerpo de su padre. ¿Qué hace?", opts=[
    C("Gritar el nombre de Vortex", "c7_07", add={"odio_vortex": 1}),
    M("Arrodillarse junto a él sin poder hablar", "c7_07"),
    M("Fijarse en los cortes de los árboles", "c7_07", set={"vio_cortes": True}),
])

ch.scene("c7_07", bg="c7_campo_noche", text="""
Para el niño, solo hay una explicación: Vortex vino, su padre lo rechazó y ahora está muerto.
El dolor y la rabia de Little Johnny fluyen hacia Big Johnny. La criatura empieza a crecer.
""", ask="Big Johnny se transforma. ¿Qué hace Little Johnny?", opts=[
    C("Dejar que su rabia lo alimente", "c7_08", add={"odio_vortex": 1}),
    M("Intentar calmarlo, sin conseguirlo", "c7_08", add={"rel_big": 1}),
])

ch.scene("c7_08", bg="c7_aldea_destruida", text="""
Big Johnny es ya un monstruo gigantesco. Ataca la aldea cercana sin control.
Vortex aparece para proteger a los aldeanos. Entre los árboles, una sombra silenciosa observa con una espada en la mano. Nadie la ve.
[vio_cortes] Esos cortes... Little Johnny no lo sabe todavía, pero ya los vio.
""", ask="Vortex se enfrenta a Big Johnny. ¿Qué hace Little Johnny?", opts=[
    C("Gritarle a Big Johnny que no se detenga", "c7_f1", add={"odio_vortex": 1}),
    M("Mirar paralizado", "c7_f1"),
])

ch.fight("c7_f1", "Big Johnny contra Vortex", a="Big Johnny", b="Vortex", bg="c7_aldea_destruida", beats=[
    "Vortex crea un remolino que levanta tejados enteros.",
    "Big Johnny ruge y atraviesa el viento a zarpazos.",
    "Vortex se interpone entre el monstruo y una familia. Recibe el golpe de lleno.",
    "El héroe número 1 cae de rodillas. Big Johnny alza la garra para el golpe final.",
], next="c7_09")

# ---------------- EPISODIO 18: LLAMA EXTINGUIDA ----------------
ch.scene("c7_09", bg="c7_aldea_destruida", text="""
Vortex está derrotado. Big Johnny ruge, esperando una orden.
Vortex: Niño... yo no maté a tu padre.
""", ask="¿Qué hace Little Johnny?", opts=[
    C("Correr hacia Big Johnny y abrazarlo para calmarlo", "c7_10", add={"rel_big": 1}),
    M("Gritarle '¡basta!' a Big Johnny", "c7_10"),
    X("Dejar que Big Johnny destroce a Vortex", "c7_bA1", flag="johnny_venganza", ending="E14"),
])

ch.scene("c7_10", bg="c7_noticias", text="""
La noticia corre como la pólvora: 'Un niño domestica a un monstruo y salva una aldea'.
La confianza fluye hacia los Johnnies. FOMO, una agencia, los recluta.
Zac: Juntos llegarán muy lejos, chicos.
""", ask="¿Acepta Little Johnny unirse a FOMO?", opts=[
    C("Aceptar", "c7_11"),
    M("Aceptar si Big Johnny puede vivir con él", "c7_11", add={"rel_big": 1}),
    M("Aceptar solo para acercarse a Vortex", "c7_11", add={"odio_vortex": 1}),
])

ch.scene("c7_11", bg="c7_fomo", text="""
Little Johnny se hace una promesa frente al espejo.
Little Johnny: Voy a ser el número 1. Y cuando lo sea, Vortex tendrá que decirme la verdad.
""", ask="¿Cómo entrena Little Johnny?", opts=[
    C("Sin descanso, día y noche", "c7_12"),
    M("Aprendiendo a controlar a Big Johnny", "c7_12", add={"rel_big": 1}),
    M("Estudiando todas las peleas de Vortex", "c7_12", add={"odio_vortex": 1}),
])

ch.scene("c7_12", bg="c7_noticias", text="""
Noticia urgente: un avión cayó en la montaña. Entre los pasajeros iba Vortex. Solo hay una superviviente, una niña.
[cyan_libre|cyan_diosa] Esa niña, años después, tomará un camino muy distinto al que todos esperaban.
Little Johnny se queda mirando la pantalla.
""", ask="Vortex ha muerto. ¿Qué siente Little Johnny?", opts=[
    C("Rabia: ya nunca sabrá la verdad", "c7_13"),
    M("Un vacío extraño", "c7_13"),
    M("Culpa, por haberlo odiado tanto", "c7_13", add={"odio_vortex": -1}),
])

ch.scene("c7_13", bg="c7_fomo", text="""
Años después, en el presente. Los Johnnies son héroes reconocidos.
FOMO les asigna una misión: explorar por delante del equipo que investiga el ovni estrellado.
[ovni_publico] Desde la filtración, cada paso de la expedición se transmite en vivo.
""", ask="¿Cómo prepara Little Johnny la misión?", opts=[
    C("Estudiando el mapa con Big Johnny", "c7_14"),
    M("Pidiéndoles a los pájaros que vigilen el bosque", "c7_14"),
    M("Sin prepararse: confía en su instinto", "c7_14"),
])

ch.scene("c7_14", bg="c7_bosque_ovni", text="""
Cerca del ovni, Big Johnny se pone nervioso. Mira la nave como si la reconociera.
Big Johnny: Casa... ¿casa?
""", ask="¿Qué hace Little Johnny?", opts=[
    C("Tranquilizarlo y seguir con la misión", "c7_15"),
    M("Preguntarle qué siente", "c7_15", add={"rel_big": 1}),
    X("Dejarlo volver a su origen, aunque abandonen FOMO", "c7_bB1", flag="johnny_paz", ending="E09"),
])

ch.scene("c7_15", bg="c7_bosque_ovni", text="""
En el bosque encuentran restos de una pelea reciente: árboles cortados con una precisión imposible.
[ghost_berserk] Los cortes están cubiertos de un barro negro que huele a miedo.
[ghost_retirado] Son cortes viejos, de hace años... pero idénticos.
Little Johnny se queda helado. Son los mismos cortes que vio el día en que murió su padre.
""", ask="¿Qué hace Little Johnny?", opts=[
    C("Tocar los cortes con la mano", "c7_16"),
    M("Pedirle a Big Johnny que olfatee el rastro", "c7_16"),
    M("Tomar fotos para compararlas después", "c7_16"),
])

ch.scene("c7_16", bg="c7_bosque_ovni", text="""
El asesino de su padre está cerca. Quizá en el mismo equipo de la expedición.
[!ghost_retirado&!ghost_berserk] Little Johnny piensa en el hombre callado de la espada que viaja con ellos.
""", ask="¿Qué decide hacer con su sospecha?", opts=[
    C("Guardársela por ahora", "c7_fin"),
    M("Contársela solo a Big Johnny", "c7_fin", add={"rel_big": 1}),
])

ch.end("c7_fin", "Fin del capítulo 7", """
Los Johnnies siguen hacia el ovni con una sospecha que les pesa en el pecho.
Lejos de allí, Mickey le confiesa a Liu Zhen que la Organización Spotlight trabaja para DOS. Y envía a Queen a la zona con unas 'vacaciones' falsas.
Voz: Todos los hilos se dirigen al mismo punto: una nave que cayó del cielo.
""", bg="c7_bosque_ovni")

# ================= RAMA A: La venganza =================
ch.scene("c7_bA1", bg="c7_aldea_destruida", text="""
Little Johnny no dice nada. Su silencio es la orden.
La garra de Big Johnny cae. Vortex no se levanta.
Los aldeanos miran al niño con terror.
""", ask="¿Qué siente Little Johnny?", opts=[
    M("Nada", "c7_bA2"),
    M("Algo que se rompe dentro de él", "c7_bA2"),
])

ch.scene("c7_bA2", bg="c7_noticias", text="""
'Un niño y su monstruo matan al héroe número 1.' La confianza no llega: llega el miedo. Y el miedo hace crecer a Big Johnny todavía más.
""", ask="Los héroes vienen a por ellos. ¿Qué hace?", opts=[
    M("Huir a las montañas", "c7_bA3"),
    M("Enfrentarlos", "c7_bA3", add={"odio_vortex": 1}),
])

ch.scene("c7_bA3", bg="c7_montana", text="""
Años de huida. Big Johnny ya no cabe en ninguna cueva. Little Johnny habla cada vez menos con los humanos y más con los lobos.
Un día, un animal le cuenta algo: 'Vortex olía a viento. El hombre que mató a tu padre olía a acero y no hacía ningún ruido'.
""", ask="¿Qué hace con esa información?", opts=[
    M("Buscar al hombre que huele a acero", "c7_bA4"),
    M("Negarse a creerla", "c7_bA4"),
])

ch.scene("c7_bA4", bg="c7_montana", text="""
La verdad lo encuentra igual: el asesino trabajaba para Mighty Glory. Un hombre sin voz.
Little Johnny: Entonces Vortex era inocente...
Big Johnny gruñe, confundido por el dolor de su hermano.
""", ask="¿Qué siente Little Johnny?", opts=[
    M("Que ya no puede volver atrás", "c7_bA5"),
    M("Que necesita terminar lo que empezó", "c7_bA5", add={"odio_vortex": 1}),
])

ch.scene("c7_bA5", bg="c7_bosque_ovni", text="""
Siguiendo el rastro, llegan a la zona del ovni. Big Johnny se queda mirando la nave.
Big Johnny: Casa...
""", ask="¿Qué hace Little Johnny?", opts=[
    M("Ignorarlo: primero la venganza", "c7_bA6"),
    M("Prometerle que después irán a 'casa'", "c7_bA6", add={"rel_big": 1}),
])

ch.scene("c7_bA6", bg="c7_bosque_ovni", text="""
Encuentran los mismos cortes de espada. El asesino está cerca. Big Johnny ya es más grande que los árboles.
""", ask="¿Qué hace Little Johnny?", opts=[
    M("Rugir con Big Johnny para que el asesino los oiga", "c7_bA7"),
    M("Esperar en silencio, como él", "c7_bA7"),
])

ch.scene("c7_bA7", bg="c7_bosque_ovni", text="""
La noche cae. El niño que hablaba con los pájaros ya no recuerda cómo se reía.
""", ask="¿Qué le dice a Big Johnny antes de dormir?", opts=[
    M("'Mañana acaba todo'", "c7_bA_fin"),
    M("'Perdóname'", "c7_bA_fin", add={"rel_big": 1}),
])

ch.end("c7_bA_fin", "Fin del capítulo 7 (hilo alterado)", """
Vortex murió en una aldea, no en un avión. Los Johnnies no son héroes: son una amenaza en busca de su presa.
Voz: El hilo más antiguo se ha quemado. Todos los que vienen después cargarán con sus cenizas.
""", bg="c7_bosque_ovni", alt=True, set={"johnny_oscuro": True, "vortex_muerto": True})

# ================= RAMA B: Big Johnny vuelve a casa =================
ch.scene("c7_bB1", bg="c7_bosque_ovni", text="""
Little Johnny se arrodilla frente a su hermano.
Little Johnny: Si allí está tu casa, vamos. FOMO puede esperar.
Big Johnny lo mira con sus ojos enormes.
""", ask="¿Cómo se acercan al ovni?", opts=[
    M("De noche, en secreto", "c7_bB2"),
    M("Ahora mismo, sin esperar al equipo", "c7_bB2"),
])

ch.scene("c7_bB2", bg="c7_ovni_interior", text="""
Dentro de la nave, las luces se encienden con la presencia de Big Johnny. Hay jaulas vacías. Imágenes de criaturas como él.
Big Johnny: No casa. Jaula.
""", ask="¿Qué entiende Little Johnny?", opts=[
    M("Que Big Johnny fue un prisionero aquí también", "c7_bB3"),
    M("Que su casa de verdad es él", "c7_bB3", add={"rel_big": 1}),
])

ch.scene("c7_bB3", bg="c7_ovni_interior", text="""
En una pantalla de la nave aparecen datos que entiende a medias: la confianza, el miedo, esta especie... Big Johnny es inmune a los poderes basados en la fe.
Little Johnny: Por eso te quería la gente poderosa...
""", ask="¿Qué hace con esa información?", opts=[
    M("Destruir la pantalla para que nadie lo sepa", "c7_bB4"),
    M("Memorizarla", "c7_bB4"),
])

ch.scene("c7_bB4", bg="c7_bosque_ovni", text="""
Al salir, encuentran los cortes de espada en los árboles. Los mismos de aquella noche.
Big Johnny se pone delante de él, protector.
""", ask="¿Qué decide Little Johnny?", opts=[
    M("No buscar al asesino: ya no quiere más odio", "c7_bB5"),
    M("Recordarlo, pero no perseguirlo", "c7_bB5"),
])

ch.scene("c7_bB5", bg="c7_fomo", text="""
Little Johnny llama a FOMO y renuncia.
Zac: ¿Estás loco? ¡Estabas a punto de entrar en el top 5!
""", ask="¿Qué le responde?", opts=[
    M("'Mi hermano no es un arma'", "c7_bB6"),
    M("'El número 1 no me devolverá a mi padre'", "c7_bB6"),
])

ch.scene("c7_bB6", bg="c7_campo", text="""
Vuelven al campo, a la vieja casa. Arreglan el tejado. Los animales del pueblo vienen a saludarlos.
""", ask="¿Qué hace Little Johnny con la tumba de su padre?", opts=[
    M("Plantar flores", "c7_bB7"),
    M("Contarle todo lo que pasó", "c7_bB7", add={"rel_padre_j": 1}),
])

ch.scene("c7_bB7", bg="c7_campo_noche", text="""
Esa noche duermen en el campo, bajo las estrellas. Big Johnny ronca como un trueno pequeño.
""", ask="¿Qué piensa Little Johnny antes de dormir?", opts=[
    M("Que su padre estaría orgulloso", "c7_bB_fin"),
    M("Que algún día sabrá la verdad, pero sin odio", "c7_bB_fin"),
])

ch.end("c7_bB_fin", "Fin del capítulo 7 (hilo alterado)", """
Los Johnnies abandonan el ranking. Big Johnny nunca volverá a ser un arma.
Voz: Una criatura inmune a la fe, fuera del tablero. Hay quien la buscaba con muchas ganas.
""", bg="c7_campo_noche", alt=True, set={"johnnies_retirados": True})
