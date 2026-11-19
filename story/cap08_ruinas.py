"""Capítulo 8: El Incidente de las Ruinas (episodios 19-20)."""
from engine.model import Chapter, C, M, X

# Si alguno de estos hilos se rompió antes, las Ruinas no pueden ocurrir como en el anime.
ALTERADO = ("ghost_retirado|ghost_berserk|johnnies_retirados|johnny_oscuro|loli_retirada|"
            "queen_caida|cyan_libre|cyan_diosa|rock_expuesto|esoul_original_vivo|ovni_publico|"
            "dos_expuesto")

ch = Chapter(8, "El Incidente de las Ruinas", "Episodios 19-20", start="c8_00", color=(90, 60, 110), intro="""
Una nave estrellada. Cinco agencias. Una docena de órdenes secretas. Nadie sale de allí igual que entró.
""")

ch.scene("c8_00", bg="fuera_del_tiempo", text="""
Voz: Todos los hilos que has visto se anudan aquí.
[!ghost_retirado&!ghost_berserk&!johnnies_retirados&!johnny_oscuro&!loli_retirada&!queen_caida&!cyan_libre&!cyan_diosa&!rock_expuesto&!esoul_original_vivo&!ovni_publico&!dos_expuesto] Voz: Esto es lo que la historia recuerda como 'el Incidente de las Ruinas'.
""", next="c8_01", redirect=[(ALTERADO, "c8_bC0")])

# ---------------- EPISODIO 19: ROMPER EL EQUILIBRIO ----------------
ch.scene("c8_01", bg="c8_ovni_exterior", text="""
Little Johnny camina junto a Ghostblade hacia los restos del ovni. No puede dejar de mirar la espada del hombre callado.
Big Johnny: Hermano... huele raro.
""", ask="¿Qué hace Little Johnny con su sospecha?", opts=[
    C("Descartarla: no tiene pruebas", "c8_02"),
    M("Mantener a Big Johnny entre él y Ghostblade", "c8_02", add={"rel_big": 1}),
    M("Preguntarle a Ghostblade de dónde viene", "c8_02"),
])

ch.scene("c8_02", bg="c8_ovni_entrada", text="""
De pronto, Big Johnny echa a correr hacia el interior del ovni, como si algo lo llamara.
Little Johnny: ¡Big Johnny, espera!
""", ask="¿Qué hace Little Johnny?", opts=[
    C("Correr tras él", "c8_03"),
    M("Gritarle a Ghostblade que lo ayude", "c8_03"),
])

ch.scene("c8_03", bg="c8_ovni_pasillo", text="""
Ghostblade corre detrás del niño. En su bolsillo lleva una orden de Rock: matar a Little Johnny y llevarse a Big Johnny, la criatura inmune a la fe.
El niño corre delante de él, de espaldas, indefenso.
""", ask="Ghostblade tiene al niño a su alcance. ¿Qué hace?", opts=[
    C("Dudar, y seguir corriendo", "c8_04"),
    M("Llevar la mano a la espada... y apartarla", "c8_04", add={"conciencia": 1}),
])

ch.scene("c8_04", bg="c8_ovni_hangar", text="""
Un relámpago parte el hangar en dos. Es E-Soul.
[cheng_oscuro] Su mirada es la de un perro de presa. Lleva años haciendo el trabajo sucio de Rock.
E-Soul: Rock sabe que has estado visitando a tu hija, Ghostblade. Te han cambiado la misión.
""", ask="E-Soul los ataca. ¿Qué hace Little Johnny?", opts=[
    C("Pelear al lado de Ghostblade", "c8_f1"),
    M("Buscar a Big Johnny mientras ellos pelean", "c8_f1"),
])

ch.fight("c8_f1", "E-Soul contra Ghostblade y Little Johnny", a="Ghostblade", b="E-Soul", bg="c8_ovni_hangar", winner="b", beats=[
    "El relámpago contra la espada. El hangar se ilumina a cada choque.",
    "Ghostblade es más hábil, pero E-Soul está lleno de confianza fresca.",
    "Little Johnny llama a los animales del bosque; nadie responde dentro de la nave.",
    "E-Soul atrapa a Ghostblade en una jaula eléctrica. El niño cae inconsciente.",
], next="c8_05")

ch.scene("c8_05", bg="c8_ovni_laboratorio", text="""
En otra zona de la nave, Nuonuo trabaja sola. Una figura perfecta, sonriente, aterriza frente a ella: Nice.
Shand lo envió a eliminar al equipo. Sus descubrimientos sobre la confianza y el material que suprime el miedo podrían acabar con la industria de los héroes.
Nice se arregla los guantes tres veces. Una, dos, tres. Siempre tres.
""", ask="Nice tiene delante a Nuonuo, aterrorizada. ¿Qué hace?", opts=[
    C("Avanzar hacia ella, siguiendo la orden", "c8_06"),
    M("Avanzar despacio, odiándose", "c8_06", add={"culpa_nice": 1}),
    X("Desobedecer a Shand y decirle que huya", "c8_bA1", flag="nice_deserta", ending="E02"),
])

ch.scene("c8_06", bg="c8_ovni_laboratorio", text="""
Un puño de metal rosa atraviesa la pared. Es Loli.
Loli: ¡Ni se te ocurra tocarla!
""", ask="¿Qué hace Loli?", opts=[
    C("Lanzarse contra Nice", "c8_f2"),
    M("Gritarle a Nuonuo que corra con su padre", "c8_f2", add={"rel_nuonuo": 1}),
])

ch.fight("c8_f2", "Loli contra Nice", a="Loli", b="Nice", bg="c8_ovni_laboratorio", winner="none", beats=[
    "Nice vuela con una elegancia perfecta. Cada golpe, impecable.",
    "El traje de Loli no depende de la fe; no le importa lo famoso que sea Nice.",
    "Chocan contra los paneles de la nave, que se encienden con luces extrañas.",
    "Ninguno cede. Loli lo inmoviliza un instante.",
], next="c8_07")

# ---------------- EPISODIO 20: EL INCIDENTE DE LAS RUINAS ----------------
ch.scene("c8_07", bg="c8_ovni_pasillo", text="""
El padre de Loli y Nuonuo corren por los pasillos. Loli los oye por la radio.
Padre de Loli: ¡Estamos bien, hija! ¡Vamos hacia la salida!
""", ask="¿Qué hace Loli?", opts=[
    C("Dejar a Nice y correr tras ellos", "c8_08"),
    M("Decirles que no se detengan pase lo que pase", "c8_08", add={"rel_padre": 1}),
])

ch.scene("c8_08", bg="c8_ovni_salida", text="""
Llega tarde. Unos agentes vestidos de negro, idénticos entre sí, los han emboscado: clones de un experimento con miedo.
Nuonuo está en el suelo, en coma. El padre de Loli y el equipo científico están muertos.
""", ask="Loli ve el cuerpo de su padre. ¿Qué hace?", opts=[
    C("Gritar y atacar a los clones", "c8_f3"),
    M("Proteger primero a Nuonuo y luego atacar", "c8_f3", add={"rel_nuonuo": 1}),
])

ch.fight("c8_f3", "Loli contra los clones del miedo", a="Loli", b="Clones", bg="c8_ovni_salida", beats=[
    "Los clones se mueven como uno solo. El miedo gotea de sus armas.",
    "Loli no siente miedo. Solo siente rabia.",
    "El traje se sobrecalienta. Ella no se detiene.",
    "El último clon cae. El silencio es peor que la pelea.",
], next="c8_09")

ch.scene("c8_09", bg="c8_ovni_laboratorio", text="""
Loli vuelve a donde dejó a Nice. Él sigue ahí, de pie, arreglándose los guantes. Una, dos, tres.
Loli: ¿Fue tu agencia? ¿Fuiste TÚ?
""", ask="¿Qué hace Loli?", opts=[
    C("Lanzarse otra vez contra él, ciega de rabia", "c8_10"),
    M("Exigirle el nombre de quien dio la orden", "c8_10"),
])

ch.scene("c8_10", bg="c8_ovni_hangar", text="""
En el hangar, Little Johnny despierta. Ve a Ghostblade herido y a E-Soul de pie sobre ellos.
Big Johnny aparece y, al ver a su hermano en el suelo, enloquece. Crece y crece. La nave entera empieza a romperse.
""", ask="Big Johnny se descontrola. ¿Qué hace Little Johnny?", opts=[
    C("Llamarlo una y otra vez, sin conseguir calmarlo", "c8_11"),
    M("Arrastrarse hacia él, llamándolo", "c8_11", add={"rel_big": 1}),
    X("Dejar de llamarlo: que lo destruya todo", "c8_bB1", flag="ruinas_catastrofe", ending="E06"),
])

ch.scene("c8_11", bg="c8_ovni_ruinas", text="""
La nave se derrumba. Entre el polvo aparecen dos figuras: Queen, con su lanza, y Lucky Cyan.
El 'monstruo' que vieron en la carretera durante sus vacaciones era Big Johnny. Mickey las envió aquí a propósito.
Queen: Todos. Quietos.
""", ask="Queen llega al caos. ¿Qué hace?", opts=[
    C("Desplegar su área sobre todas las ruinas", "c8_f4"),
    M("Pedirle a Cyan que cante para calmar a Big Johnny y luego desplegar el área", "c8_f4"),
])

ch.fight("c8_f4", "Queen contra todos", a="Queen", b="Todos", bg="c8_ovni_ruinas", beats=[
    "El área de Queen cubre las ruinas. Dentro, ella pone las reglas.",
    "'Aquí no hay relámpagos.' E-Soul se apaga.",
    "'Aquí nadie vuela.' Nice cae al suelo.",
    "'Aquí, los monstruos duermen.' Big Johnny se encoge hasta su tamaño normal.",
    "Todos quedan inmóviles. La reina ha hablado.",
], next="c8_12")

ch.scene("c8_12", bg="c8_ovni_ruinas", text="""
El polvo se asienta. Loli se arrodilla junto al cuerpo de su padre. Nuonuo respira, pero no despierta.
Ghostblade mira a su hija en coma y no puede decir nada. Nunca ha podido.
""", ask="¿Qué hace Loli?", opts=[
    C("Abrazar a su padre en silencio", "c8_13"),
    M("Tomar la mano de Nuonuo", "c8_13", add={"rel_nuonuo": 1}),
    M("Mirar a Nice con odio mientras se lo llevan", "c8_13"),
])

ch.scene("c8_13", bg="c8_noticias", text="""
Mickey y Shand se adelantan a las investigaciones: hacen que todas las pruebas apunten a Rock y a Mighty Glory.
Un año después, el 20.º Torneo de Héroes se cancela. X sigue siendo el número 1. Queen, la número 2.
""", ask="Nuonuo sigue en coma. Ghostblade la visita en el hospital. ¿Qué hace?", opts=[
    C("Sentarse junto a ella cada día, en silencio", "c8_14"),
    M("Leerle su viejo cuaderno, sin voz, solo moviendo los labios", "c8_14", add={"rel_nuonuo": 1}),
])

ch.scene("c8_14", bg="c8_mighty_glory", text="""
Ghostblade, ahora número 4, se presenta en Mighty Glory con una carta de renuncia.
Rock: Si te vas, perderás todo.
""", ask="¿Qué hace Ghostblade?", opts=[
    C("Dejar la carta sobre la mesa e irse", "c8_15"),
    M("Clavar la carta en la mesa con un cuchillo", "c8_15"),
])

ch.scene("c8_15", bg="c8_fomo", text="""
Los Johnnies pasan a DOS como número 5. Loli entra en FOMO como número 6.
Zac: Bienvenida a FOMO. Aquí tenemos gente... peculiar.
En un escritorio del fondo, un oficinista de corbata levanta la vista un segundo y vuelve a su trabajo.
""", ask="¿Por qué Loli eligió FOMO?", opts=[
    C("Porque es la agencia más lejos de TREEMAN", "c8_16"),
    M("Porque así puede seguir investigando el ovni", "c8_16"),
    M("Porque su padre le habría dicho que sí", "c8_16", add={"rel_padre": 1}),
])

ch.scene("c8_16", bg="c8_rock_oficina", text="""
En su oficina, Rock no parece preocupado. Frente a él, un joven con la mirada llena de odio: Dragon Boy.
Rock: Cero cayó porque estaba solo. Tú no lo estarás.
""", ask="¿Qué responde Dragon Boy?", opts=[
    C("'Quiero toda la fe del mundo'", "c8_fin"),
    M("'Quiero que el mundo pague'", "c8_fin"),
])

ch.end("c8_fin", "Fin del capítulo 8", """
El Incidente de las Ruinas termina. La verdad queda enterrada bajo los escombros.
Rock sigue adelante con su plan. Ahora tiene a un dragón.
Voz: Has visto el nudo. Ahora verás cómo alguien intenta convertirse en un dios.
""", bg="c8_rock_oficina")

# ================= RAMA A: Nice desobedece =================
ch.scene("c8_bA1", bg="c8_ovni_laboratorio", text="""
Nice baja el puño. Le tiembla la mano.
Nice: Corre. Hacia la salida norte, no la sur. En la sur te esperan.
Nuonuo no entiende nada, pero corre.
""", ask="¿Qué hace Nice ahora?", opts=[
    M("Seguirla para protegerla", "c8_bA2"),
    M("Arreglarse los guantes tres veces para calmarse", "c8_bA2", add={"culpa_nice": 1}),
])

ch.scene("c8_bA2", bg="c8_ovni_pasillo", text="""
Loli atraviesa la pared y se le echa encima.
Loli: ¡Aléjate de ella!
Nice: ¡Escúchame! ¡Hay otros! ¡Shand envió a otros!
""", ask="¿Qué hace Nice?", opts=[
    M("No defenderse para que ella le crea", "c8_bA3"),
    M("Señalar la radio: el padre de Loli está en peligro", "c8_bA3"),
])

ch.scene("c8_bA3", bg="c8_ovni_salida", text="""
Llegan a la salida sur justo cuando los clones del miedo rodean al padre de Loli y al equipo científico.
Nice: Yo me encargo de la izquierda.
""", ask="¿Cómo pelean juntos?", opts=[
    M("Nice distrae y Loli golpea", "c8_bA4"),
    M("Nice se pone delante de los científicos como escudo", "c8_bA4", add={"culpa_nice": -1}),
])

ch.scene("c8_bA4", bg="c8_ovni_salida", text="""
Los clones caen. El padre de Loli está herido, pero vivo. Nuonuo también.
Loli mira a Nice con desconfianza.
Loli: ¿Por qué?
""", ask="¿Qué responde Nice?", opts=[
    M("'Porque estoy cansado de ser perfecto'", "c8_bA5"),
    M("'Porque nadie me lo había preguntado antes'", "c8_bA5"),
])

ch.scene("c8_bA5", bg="c8_ovni_hangar", text="""
En el hangar, Big Johnny se descontrola. Queen y Cyan llegan y calman la situación.
Nice se acerca a Queen con un pendrive.
Nice: Aquí están las órdenes de Shand. Todas.
""", ask="¿Entrega Nice las pruebas?", opts=[
    M("Sí, a Queen", "c8_bA6"),
    M("Sí, en directo, ante la prensa", "c8_bA6", add={"culpa_nice": -1}),
])

ch.scene("c8_bA6", bg="c8_noticias", text="""
TREEMAN se hunde. Shand es arrestado. Las 'pruebas' contra Rock no aparecen, porque nadie tiene que fabricarlas.
Nice pierde el contrato, la agencia y la mitad de su confianza.
""", ask="¿Cómo se siente Nice?", opts=[
    M("Libre", "c8_bA7"),
    M("Asustado, pero vivo", "c8_bA7"),
])

ch.scene("c8_bA7", bg="c8_azotea", text="""
Una noche, Nice sube a una azotea. La misma donde, en otra versión de la historia, habría saltado.
Mira hacia abajo un buen rato.
""", ask="¿Qué hace?", opts=[
    M("Dar media vuelta y bajar por las escaleras", "c8_bA_fin"),
    M("Sentarse y mirar la ciudad hasta que amanece", "c8_bA_fin"),
])

ch.end("c8_bA_fin", "Fin del capítulo 8 (hilo alterado)", """
El padre de Loli sobrevive. Nuonuo nunca entra en coma. TREEMAN deja de existir.
Y Nice, el héroe perfecto, no saltará de ninguna azotea.
Voz: Has salvado a un hombre que tenía que morir para que otro naciera. ¿Quién ocupará ahora su lugar?
""", bg="c8_azotea", alt=True, set={"nuonuo_salvada": True, "padre_loli_vivo": True, "nice_rebelde": True})

# ================= RAMA B: La catástrofe =================
ch.scene("c8_bB1", bg="c8_ovni_hangar", text="""
Little Johnny se calla. Su silencio deja crecer a Big Johnny sin límite.
El techo de la nave se abre. Las paredes se derriten. En el núcleo del ovni, algo brilla: un depósito de miedo antiguo.
""", ask="¿Qué hace Little Johnny?", opts=[
    M("Mirar cómo todo se derrumba", "c8_bB2"),
    M("Arrepentirse demasiado tarde", "c8_bB2", add={"rel_big": 1}),
])

ch.scene("c8_bB2", bg="c8_ovni_ruinas", text="""
Big Johnny rompe el núcleo. Una ola de miedo sale disparada hacia el cielo.
E-Soul, Nice y Ghostblade quedan atrapados en ella. Sus ojos se vuelven negros.
""", ask="¿Qué hace Loli, inmune al miedo gracias a su traje?", opts=[
    M("Sacar a Nuonuo y a su padre de allí", "c8_bB3", add={"rel_nuonuo": 1}),
    M("Intentar cerrar el núcleo", "c8_bB3"),
])

ch.scene("c8_bB3", bg="c8_ovni_ruinas", text="""
Queen llega y despliega su área, pero el miedo es demasiado grande. Las reglas se le escapan.
[!cyan_libre&!cyan_diosa] Cyan canta con todas sus fuerzas. Su voz apenas se oye.
Queen: ¡No puedo contenerlo!
""", ask="¿Qué hace Queen?", opts=[
    M("Concentrar su área para salvar solo a los civiles", "c8_bB4"),
    M("Resistir hasta caer", "c8_bB4"),
])

ch.scene("c8_bB4", bg="c8_ciudad_miedo", text="""
La ola llega a la ciudad más cercana. Las pulseras marcan negativo. La gente se encierra en sus casas.
Los héroes que estuvieron en las Ruinas vuelven... distintos.
""", ask="¿A quién sigue la historia ahora?", opts=[
    M("A Loli, la única que sigue en pie", "c8_bB5"),
    M("A Little Johnny, que lo provocó todo", "c8_bB5"),
])

ch.scene("c8_bB5", bg="c8_ciudad_miedo", text="""
Loli fabrica placas con restos del ovni para proteger a la gente. Pero no hay suficientes.
Little Johnny camina entre las ruinas, con Big Johnny dormido, enorme, detrás de él como una montaña.
""", ask="¿Qué hace Little Johnny?", opts=[
    M("Pedir perdón en público", "c8_bB6"),
    M("Desaparecer", "c8_bB6"),
])

ch.scene("c8_bB6", bg="c8_rock_oficina", text="""
Rock observa todo desde su torre. Sonríe.
Rock: El miedo es solo fe al revés. Y yo sé darle la vuelta.
""", ask="¿Quién se opone a Rock?", opts=[
    M("Queen, herida pero en pie", "c8_bB7"),
    M("Nadie, por ahora", "c8_bB7"),
])

ch.scene("c8_bB7", bg="c8_ciudad_miedo", text="""
El ranking deja de publicarse. Nadie sabe quién es el número 1. Solo se sabe que X no ha aparecido.
""", ask="¿Qué espera la gente?", opts=[
    M("Que X venga a salvarlos", "c8_bB_fin"),
    M("Ya nada", "c8_bB_fin"),
])

ch.end("c8_bB_fin", "Fin del capítulo 8 (hilo alterado)", """
El Incidente de las Ruinas se convierte en 'La Ola'. El miedo ya no es un experimento: es el clima.
Voz: Un monstruo sin freno y un núcleo roto. El tablero está ardiendo.
""", bg="c8_ciudad_miedo", alt=True, set={"miedo_liberado": True})

# ================= RUTA C: Las Ruinas con el hilo ya alterado =================
ch.scene("c8_bC0", bg="fuera_del_tiempo", text="""
Voz: Pero tú ya has tirado de otros hilos. El nudo no puede formarse igual.
""", next="c8_bC1")

ch.scene("c8_bC1", bg="c8_ovni_exterior", text="""
La expedición llega al ovni.
[ovni_publico] Hay drones de prensa por todas partes. Ninguna agencia se atreve a atacar delante de las cámaras.
[loli_retirada] Loli no está. Su padre tampoco: en su lugar hay un equipo de científicos de la Comisión.
[!loli_retirada] Loli y su padre encabezan el grupo científico.
[ghost_retirado] No hay ningún asesino silencioso en el equipo de seguridad. Mighty Glory envió a otro guardia, mucho menos hábil.
[ghost_berserk] De las profundidades de la nave sale un rastro de barro negro: allí dentro se esconde lo que queda de Ghostblade.
[johnnies_retirados] Los Johnnies no vinieron. Están en el campo, lejos de todo esto.
[johnny_oscuro] En el horizonte, una montaña respira: Big Johnny, gigante, y un niño que busca al hombre que huele a acero.
""", ask="Al llegar al ovni, ¿en quién se centra la historia?", opts=[
    M("En Nuonuo", "c8_bC2", add={"rel_nuonuo": 1}),
    M("En el equipo científico", "c8_bC2"),
])

ch.scene("c8_bC2", bg="c8_ovni_laboratorio", text="""
Dentro de la nave, Nuonuo encuentra paneles que reaccionan al miedo y a la confianza.
[rock_expuesto] Rock está en la cárcel; nadie ha dado la orden de robar a Big Johnny ni de traicionar a nadie.
[esoul_original_vivo] Ningún relámpago irrumpe en el hangar: los dos E-Soul están lejos de aquí, trabajando juntos.
[!rock_expuesto&!esoul_original_vivo] Un relámpago estalla en el hangar: E-Soul cumple órdenes de Rock, aunque su objetivo no está donde esperaba.
Nice aterriza frente a Nuonuo, enviado por Shand.
[ovni_publico] Nice: ...hay cámaras por todas partes. Shand, no puedo hacerlo.
""", ask="Nice está frente a Nuonuo. ¿Qué pasa?", opts=[
    M("Nice duda y se retira", "c8_bC3", add={"culpa_nice": 1}),
    M("Nice duda, pero alguien más actúa por él", "c8_bC3"),
])

ch.scene("c8_bC3", bg="c8_ovni_salida", text="""
En la salida aparecen los clones del miedo de Shand.
[!loli_retirada] Loli llega a tiempo de pelear, pero no de salvar a todos.
[!loli_retirada&!padre_loli_vivo] Su padre cae protegiendo a Nuonuo.
[loli_retirada] Sin Loli, los científicos de la Comisión huyen como pueden. Nuonuo se queda atrás.
[nuonuo_espada] Nuonuo saca la espada envuelta en un pañuelo que le dio su padre. Sabe usarla. Sobrevive.
""", ask="¿Qué hace Nuonuo?", opts=[
    M("Esconderse en el núcleo de la nave", "c8_bC4"),
    M("Enfrentarse a los clones con lo que tenga a mano", "c8_bC4", add={"rel_nuonuo": 1}),
])

ch.scene("c8_bC4", bg="c8_ovni_ruinas", text="""
La nave tiembla.
[queen_caida] Nadie viene a poner orden. La reina que debía llegar es ahora una zona prohibida del mapa.
[!queen_caida&dos_expuesto] Queen llega por su cuenta. Nadie la envió esta vez.
[!queen_caida&!dos_expuesto] Queen llega desde la carretera.
[cyan_libre] Viene sola: Lucky Cyan nunca existió.
[cyan_diosa] Viene sola: Cyan es ahora la diosa de un culto del miedo.
""", ask="¿Cómo termina el caos en las ruinas?", opts=[
    M("Con todos huyendo antes del derrumbe", "c8_bC5"),
    M("Con la nave hundiéndose en la tierra", "c8_bC5"),
])

ch.scene("c8_bC5", bg="c8_noticias", text="""
Las noticias cuentan una historia confusa. Cada agencia culpa a otra.
[dos_expuesto] Sin Mickey, Shand no tiene cómplice para inculpar a Rock. La investigación apunta directamente a TREEMAN.
[!dos_expuesto&!rock_expuesto] Mickey y Shand inculpan a Rock.
[rock_expuesto] Sin Rock al que culpar, Shand se queda solo frente a las preguntas.
""", ask="¿Qué siente Nice ante todo esto?", opts=[
    M("Que está perdiendo el control", "c8_bC6", add={"culpa_nice": 1}),
    M("Que Shand lo va a sacrificar", "c8_bC6", add={"culpa_nice": 1}),
])

ch.scene("c8_bC6", bg="c8_rock_oficina", text="""
[!rock_expuesto] Rock recibe a un joven lleno de odio: Dragon Boy.
[rock_expuesto] En la cárcel, Rock recibe una visita: un joven lleno de odio. Dragon Boy.
Rock: Cero cayó porque estaba solo. Tú no lo estarás.
""", ask="¿Qué responde Dragon Boy?", opts=[
    M("'Quiero toda la fe del mundo'", "c8_bC_fin"),
    M("'Quiero que el mundo pague'", "c8_bC_fin"),
])

ch.end("c8_bC_fin", "Fin del capítulo 8 (hilo alterado)", """
Las Ruinas no ocurrieron como las recuerda la historia. Algunos que debían morir siguen vivos. Otros que debían estar allí ya no existen en el tablero.
Voz: El nudo se deshizo de otra manera. El dragón, sin embargo, sigue despertando.
""", bg="c8_rock_oficina", alt=True)
