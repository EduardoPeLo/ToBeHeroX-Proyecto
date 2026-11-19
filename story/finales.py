"""Los 14 finales del juego (E01 es el final canónico de la obra)."""
from engine.model import Ending

_E = [
    Ending("E01", "X", """
La ceremonia del 21.º Torneo de Héroes se queda en silencio. Los diez mejores ya están en el escenario: Nice, vivo, con grietas que le recorren la piel; un E-Soul que ya no figura entre los diez; Queen, Lucky Cyan, Loli, los Johnnies, Ghostblade, Dragon Boy, Ahu...
Entonces sube él. Sin traje, sin máscara, sin agencia. Un oficinista cualquiera de FOMO, de corbata y con cara de cansancio.
X se presenta ante el mundo con su forma civil. Al mostrarse, deja de ser una pieza que la Comisión de Asuntos de Héroes puede mover a su antojo.
Las pulseras de millones de personas parpadean. Nadie sabe si la confianza va a subir o a desplomarse.
Recorriste el hilo del destino tal como fue tejido. Lo que pase después ya no le toca escribirlo a nadie más que a él.
""", bg="fin_x", canon=True),
    Ending("E02", "Sin Máscara", """
Alguien con la máscara de Nice dijo que no. Su confesión, sus pruebas y la gente que le creyó acabaron con la reputación de TREEMAN.
Shand pierde la agencia y la Comisión tiene que abrir una investigación pública sobre los héroes fabricados.
Ya no hay un héroe perfecto en el ranking, pero en una pulsera brilla una cifra pequeña y honesta. Por primera vez en años, alguien que se arreglaba los guantes tres veces duerme tranquilo.
""", bg="fin_sin_mascara"),
    Ending("E03", "Claro de Luna", """
El relámpago que debía matar a Moon se estrelló contra la espalda de Lin Ling. Ella sobrevivió.
Los dos desaparecen de las pantallas. Sin agencia, sin contratos y sin ranking, la confianza que les queda es la de un pueblo pequeño junto al mar, donde nadie los reconoce.
A veces, por la noche, Moon se teletransporta a la azotea más alta que encuentra solo para ver la ciudad de lejos. Lin Ling siempre sube detrás de ella por las escaleras.
""", bg="fin_luna"),
    Ending("E04", "Relámpago sin Dueño", """
Yang Cheng no mató al E-Soul original. Siguió el rastro del asesinato de Shang Chao y llegó hasta la oficina de Rock.
Las pruebas salen a la luz: el secuestro de Pomelo y la muerte de Chao formaban parte del mismo plan. Mighty Glory se derrumba.
Dos E-Soul comparten ahora el mismo nombre y ninguno de los dos le pertenece a una agencia. Xia Qing, en primera fila, sonríe cuando el relámpago ilumina el escenario infantil.
""", bg="fin_relampago"),
    Ending("E05", "El Trono de Cero", """
Rock siempre quiso repetir la historia de Cero. Esta vez nadie lo detuvo.
Con su arma más fiel y un dios fabricado a base de fe monopolizada, el ranking deja de importar. Solo hay un nombre en todas las pulseras.
La Comisión se arrodilla. Los héroes que quedan se esconden. Alguien, en algún lugar fuera del tiempo, mira el tablero y suspira.
""", bg="fin_cero"),
    Ending("E06", "La Era del Miedo", """
El miedo no es solo la ausencia de confianza: también se contagia, se fabrica y se vende.
Lo que empezó como un experimento en un laboratorio terminó convertido en una ola. Los héroes se vuelven villanos, los villanos en monstruos, y las pulseras de la ciudad marcan números negativos.
Algunos siguen luchando entre las ruinas. Ninguno sabe ya si la gente cree en ellos o les tiene miedo.
""", bg="fin_miedo"),
    Ending("E07", "La Verdad de la Reina", """
Liu Yuwei investigó a su propio padre y lo que encontró hundió a DOS: la Organización Spotlight, los villanos fabricados, los accidentes provocados.
Mickey cae. Liu Zhen confiesa ante las cámaras. La Comisión de Asuntos de Héroes queda obligada a reformarse ante millones de pulseras furiosas.
Queen no ganó ningún torneo. Pero ahora, cuando dice la verdad, la gente le cree.
""", bg="fin_reina"),
    Ending("E08", "Un Mundo sin Confianza", """
Los datos del ovni se filtraron: existe un material capaz de suprimir el miedo y de alterar la confianza. El sistema que fabrica héroes nunca fue natural.
Las agencias se desploman en bolsa. Las pulseras se vuelven locas durante semanas, hasta que la gente empieza a quitárselas.
Loli mira su traje mecánico, una armadura que funciona sin que nadie crea en ella. Tal vez el futuro sea eso: héroes que no necesitan que los quieran.
""", bg="fin_sin_confianza"),
    Ending("E09", "Lo que de Verdad Importa", """
Uno por uno, los héroes eligieron a las personas que querían por encima del ranking.
Hay un padre mudo que aprende a escribirle cartas a su hija, dos huérfanos que comparten la suerte y la desgracia, un niño y su monstruo durmiendo bajo las estrellas.
El tablero del destino se quedó sin piezas importantes. El torneo se celebra igual, y casi nadie lo ve.
""", bg="fin_familia"),
    Ending("E10", "La Sonrisa que Siguió", """
Nice no inyectó el miedo. Smile sobrevivió a la noche en la que debía morir.
Con su ídolo vivo, Lin Ling encontró el valor para decirle que no a Shand. Smile volvió a sentarse junto a X en aquella azotea, dos amigos que no le deben nada a nadie.
La Comisión todavía quiere a X muerto. Pero ahora X tiene a alguien que le cuida la espalda.
""", bg="fin_sonrisa"),
    Ending("E11", "Solo un Perro", """
Ahu no se atribuyó lo que había hecho X. Les contó la verdad a todos: él solo era un perro que había mordido a un hombre malo.
La confianza que habría recibido se fue con el viento. Nunca aprendió a hablar.
Pero cada mañana, Xin Ya le rasca detrás de la oreja y le dice que es el mejor héroe del mundo. Y Ahu, que no entiende las palabras, entiende eso perfectamente.
""", bg="fin_perro"),
    Ending("E12", "La Caída de X", """
La Comisión consiguió lo que quería: el nombre, la dirección y el punto débil del héroe número uno.
X no se defendió como habría podido. Dejó que el mundo creyera que había caído. La silla del número uno queda vacía, y todas las agencias se lanzan a pelear por ella.
En la oficina de FOMO, un escritorio queda vacío. Nadie recuerda bien quién se sentaba ahí.
""", bg="fin_caida_x"),
    Ending("E13", "Un Oficinista Cualquiera", """
X se retira del 21.º Torneo de Héroes. No da explicaciones.
El torneo lo gana otro y el mundo sigue girando. La Comisión, satisfecha, archiva la orden de ejecución.
Cada mañana, un hombre de corbata toma el mismo tren, llega a la misma oficina y escribe los mismos informes. Ahu lo acompaña a veces hasta la puerta. Ninguno de los dos menciona lo que vieron fuera del tiempo.
""", bg="fin_oficinista"),
    Ending("E14", "Llama Apagada", """
Little Johnny buscó al asesino de su padre con un monstruo a su lado y odio en el pecho.
La confianza que la gente le tenía se convirtió en miedo, y ese miedo hizo crecer a Big Johnny hasta que ya no cupo en ninguna ciudad.
Al final encontró la verdad. No le devolvió a su padre. Solo le quitó lo último que le quedaba: el niño que había sido.
""", bg="fin_llama"),
]

ENDINGS = {e.key: e for e in _E}
