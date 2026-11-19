"""Videos y música OFICIALES de To Be Hero X en YouTube.

Los IDs vienen de la página oficial del anime: https://tbhx.net/en/movie/
Si pones un archivo local con el mismo nombre en assets/videos o assets/musica, el juego
usa ese archivo en lugar de YouTube (y funciona sin internet).
"""

# Opening que suena al abrir el juego (OP sin créditos, "INERTIA").
OPENING = "8QJ8KNdhkiA"
OPENING_X = "G66mjVMVp0w"       # Opening ver.X: se usa en el final canónico
ENDING = "gQ940ZInrTY"          # ED sin créditos ("KONTINUUM"): finales alternativos

# Soundtrack por capítulo: el tema oficial de cada héroe.
MUSICA = {
    "titulo": ("UfvehG03ZLk", "Main Theme · JEOPARDY"),
    "cap01": ("kfA1Nt-UCkk", "Tema de Nice · PARAGON"),
    "cap02": ("QBbBYA4_UP4", "Tema de E-Soul · NEON RAIN"),
    "cap03": ("-wfEaOBVEG0", "Tema de Lucky Cyan · Take Off"),
    "cap04": ("wK50680h7ko", "Tema de Queen · Queen of the stars"),
    "cap05": ("gNJDelCC1iA", "Tema de Loli · Candy Mountain"),
    "cap06": ("z5b9wOi5MZY", "Tema de Ghostblade · Because of you"),
    "cap07": ("Zd2w32HX-Hs", "Tema de los Johnnies · growL"),
    "cap08": ("UfvehG03ZLk", "Main Theme · JEOPARDY"),
    "cap09": ("hE8Xu9gQtcQ", "Tema de Dragon Boy · Scar"),
    "cap10": ("MWlOPz-uF-g", "Tema de Ahu · SPARX"),
    "cap11": ("2uuPU2K_w9c", "Tema de X · New Type of Hero"),
    "fin": ("gQ940ZInrTY", "Ending · KONTINUUM"),
    "fin_x": ("G66mjVMVp0w", "Opening ver.X · INERTIA"),
}

# Videos de las peleas (solo en la línea canónica): "HERO's Highlight" oficial del episodio
# (canal de Aniplex) o clips oficiales de Crunchyroll.
PELEAS = {
    "c1_f1": ("s_7HfuPSeiE", "HERO's Highlight #1"),
    "c1_f2": ("y-BlaBclLHk", "HERO's Highlight #2"),
    "c1_f3": ("7a5qHbzENqg", "HERO's Highlight #3"),
    "c1_f4": ("TSGQOInkSMo", "HERO's Highlight #4"),
    "c2_f1": ("7sQqZZ9NhNU", "HERO's Highlight #5"),
    "c2_f2": ("1PE8S1IiTzE", "HERO's Highlight #7"),
    "c3_f1": ("nTt4B0SZE9M", "HERO's Highlight #10"),
    "c4_f2": ("Zc9wiLMXwUk", "HERO's Highlight #12"),
    "c5_f1": ("P8AuSRsIoEQ", "HERO's Highlight #14"),
    "c6_f1": ("iPFqvRACJh0", "HERO's Highlight #16"),
    "c7_f1": ("i59dBkWI1vA", "HERO's Highlight #17"),
    "c8_f1": ("iyHElqN8Lx4", "HERO's Highlight #19"),
    "c8_f4": ("PnngXEfHiyo", "HERO's Highlight #20"),
    "c9_f1": ("rpzCjpmEYIA", "HERO's Highlight #21"),
    "c9_f2": ("GjxwD3Xwh7M", "HERO's Highlight #22"),
    "c9_f4": ("y13w5eXXmYs", "X Throws Away the Final Boss (Crunchyroll)"),
    "c10_f1": ("xpUwhaokFd8", "What X's Powers Look Like to Other People (Crunchyroll)"),
    "c10_f2": ("IWMTusm6bJk", "HERO's Highlight #23"),
    "c11_f1": ("VnIHLa-GSF8", "X vs Everyone (Crunchyroll)"),
}

# Videos que se reproducen al ENTRAR en una escena de la línea canónica.
ESCENAS = {
    "c5_05": ("WxZJ2EMtyTU", "HERO's Highlight #13 · Loli contra el acosador"),
    "c6_08": ("_QCfZZ6tSf0", "HERO's Highlight #15 · Ghostblade contra Loli"),
    "c7_09": ("hp6fa8Hx3Ys", "HERO's Highlight #18 · Vortex contra Big Johnny"),
    "c10_16": ("dnd0hZsy0aY", "Why Nice Jumped (Crunchyroll)"),
    "c11_09": ("44X4woNpEys", "The Heroes Tournament Starts (Crunchyroll)"),
}

# Tráiler oficial de cada capítulo ("Character Story Movie"), se ve desde el menú de capítulos.
TRAILERS = {
    1: "qrifmR4czdA", 2: "uv83dVEZc3c", 3: "ZjRNh1OJrbU", 4: "-wl-B3tODOo",
    5: "kldQhkRg0-o", 6: "lvLehc9O730", 7: "P-cLBvQsWsI", 8: "aRIMpR8YJ90",
    9: "mL7jsdI2f6E", 10: "5dl_2BgSCww", 11: "JsY9KSzRknE",
}

# Personaje que representa cada capítulo en el menú de selección.
REPRESENTANTE = {
    1: "Lin Ling", 2: "E-Soul", 3: "Cyan", 4: "Queen", 5: "Loli", 6: "Ghostblade",
    7: "Little Johnny", 8: "Big Johnny", 9: "Dragon Boy", 10: "Ahu", 11: "X",
}
