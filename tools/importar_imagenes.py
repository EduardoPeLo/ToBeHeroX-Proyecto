"""Importa las imágenes oficiales descargadas (tbhx.net y miniaturas de YouTube oficiales)
y las coloca en assets/ con los nombres que usa el juego.

Uso:  python tools/importar_imagenes.py <carpeta_descargas>
      (la carpeta debe tener las subcarpetas main/, other/ y yt/)
"""
import json
import os
import sys

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pygame  # noqa: E402

from engine.assets import ASSETS, slug  # noqa: E402

# --- Retratos recortados de las ilustraciones oficiales (fondo transparente) ---
CUTOUTS = {
    "X": "chara1_2", "Queen": "chara2_2", "Liu Yuwei": "chara2_2", "Dragon Boy": "chara3_2",
    "Ghostblade": "chara4_2", "Wang Yi": "chara4_2", "Little Johnny": "chara5_2",
    "Loli": "chara6_2", "Luo Li": "chara6_2", "Cyan": "chara7_2", "Ahu": "chara8_2",
    "E-Soul": "chara9_2", "Yang Cheng": "chara9_2", "Lin Ling": "chara10_2",
}
# --- Retratos enmarcados desde capturas oficiales: (archivo, centro x de la cara 0-1) ---
FRAMES = {
    "Nice": ("ep21-3", .50), "Moon": ("ep1-3", .55), "Miss J": ("ep1-4", .60), "Ex-jefe": ("ep1-5", .50),
    "Enlighter": ("ep1-6", .50), "God Eye": ("ep1-6", .50), "Wreck": ("ep1-7", .45),
    "Firm-Man": ("ep1-8", .50), "Wolf Girl": ("ep1-9", .30), "Shand": ("ep4-1", .65),
    "Xia Qing": ("ep5-2", .50), "Shang Chao": ("ep5-3", .45), "Pomelo": ("ep5-5", .40),
    "E-Soul original": ("ep5-6", .55), "Rock": ("ep7-1", .35), "Liu Zhen": ("ep8-2", .50),
    "Director": ("ep8-3", .60), "Luo": ("ep8-5", .55), "Mickey": ("ep9-6", .60), "Bowa": ("ep11-2", .55),
    "Big Johnny": ("ep17-2", .50), "Padre de Loli": ("ep13-2", .50), "Nuonuo": ("ep13-3", .45),
    "DJ Shindig": ("ep13-5", .40), "Zhang Lan": ("ep15-2", .55), "Vortex": ("ep17-4", .50),
    "Smile": ("ep21-2", .55), "Xin Ya": ("ep23-2", .55),
}
# --- Cartas del menú de capítulos (arte oficial de cada héroe) ---
CARDS = {1: "chara11", 2: "chara9", 3: "chara7", 4: "chara2", 5: "chara6", 6: "chara4",
         7: "chara5", 8: "yt:aRIMpR8YJ90", 9: "chara3", 10: "chara8", 11: "chara1"}
# Portada de cada capítulo: miniatura del "Character Story Movie" oficial (sin recortar: trae el nombre).
TITLES = {1: "qrifmR4czdA", 2: "uv83dVEZc3c", 3: "ZjRNh1OJrbU", 4: "-wl-B3tODOo", 5: "kldQhkRg0-o",
          6: "lvLehc9O730", 7: "P-cLBvQsWsI", 8: "aRIMpR8YJ90", 9: "mL7jsdI2f6E", 10: "5dl_2BgSCww",
          11: "JsY9KSzRknE"}

# --- Fondos: clave de escena -> imagen ('other/ep..' captura limpia, 'yt:ID' miniatura recortada) ---
F = {
    "titulo": "yt:8QJ8KNdhkiA", "fuera_del_tiempo": "yt:G66mjVMVp0w",
    "c1_azotea": "ep1-1", "c1_treeman_oficina": "ep4-1", "c1_entrenamiento": "ep1-4",
    "c1_plaza_fans": "ep1-3", "c1_set_tv": "ep11-9", "c1_calle_caos": "ep1-5", "c1_noticias": "ep11-10",
    "c1_departamento_moon": "ep1-3", "c1_cuarto_cerrado": "ep1-2", "c1_cafe": "ep1-2",
    "c1_azotea_propuesta": "yt:y-BlaBclLHk", "c1_estatua": "ep1-9", "c1_estadio": "ep1-6",
    "c1_callejon_lluvia": "yt:TSGQOInkSMo", "c1_calle_noche": "yt:s_7HfuPSeiE", "c1_bosque": "yt:7a5qHbzENqg",
    "c1_pueblo_mar": "yt:qrifmR4czdA",
    "c2_teatro_infantil": "ep5-5", "c2_casa_qing": "ep5-2", "c2_camerino": "ep5-2", "c2_audicion": "ep5-3",
    "c2_calle": "yt:7sQqZZ9NhNU", "c2_autopista": "yt:7sQqZZ9NhNU", "c2_redes": "yt:1kGT14Q_mRg",
    "c2_noticias": "ep11-10", "c2_mighty_glory": "ep7-1", "c2_cuartel": "ep5-1", "c2_cuartel_noche": "ep5-1",
    "c2_funeral": "ep5-3", "c2_arena": "yt:1PE8S1IiTzE", "c2_almacen": "ep5-6", "c2_calle_noche": "ep5-6",
    "c3_avion_restos": "yt:ZjRNh1OJrbU", "c3_redaccion": "ep8-2", "c3_orfanato_culto": "ep8-3",
    "c3_patio": "ep8-5", "c3_orfanato_noche": "yt:2WGf_KMeZR8", "c3_orfanato_accidente": "yt:2WGf_KMeZR8",
    "c3_calles": "yt:sgrmYA2kYvk", "c3_dos_oficina": "ep9-6", "c3_concierto": "ep11-6", "c3_noticias": "ep11-10",
    "c3_orfanato_zombi": "yt:nTt4B0SZE9M", "c3_sotano": "yt:nTt4B0SZE9M", "c3_altar": "yt:nTt4B0SZE9M",
    "c3_pueblo": "ep8-1",
    "c4_graduacion": "ep8-4", "c4_dos_oficina": "ep9-6", "c4_ceremonia": "yt:_mmwZ5gQLWc",
    "c4_torneo16": "yt:_mmwZ5gQLWc", "c4_torneo18": "yt:_mmwZ5gQLWc", "c4_torneo19": "yt:Zc9wiLMXwUk",
    "c4_entrenamiento": "ep11-1", "c4_cuarto_oscuro": "ep11-1", "c4_dos_pasillo": "ep11-2",
    "c4_calle_noche": "yt:Zc9wiLMXwUk", "c4_hospital": "ep11-6", "c4_carretera": "ep11-7",
    "c4_carretera_noche": "ep11-7", "c4_archivo": "ep11-5", "c4_casa_zhen": "ep11-5", "c4_carcel": "ep11-5",
    "c4_estudio_tv": "ep11-9", "c4_noticias": "ep11-10", "c4_ciudad_oscura": "yt:Zc9wiLMXwUk",
    "c5_cuarto_loli": "ep13-1", "c5_audicion": "ep11-11", "c5_laboratorio_padre": "ep13-2",
    "c5_calle_noche": "yt:WxZJ2EMtyTU", "c5_glimmer_lab": "ep13-3", "c5_glimmer_lab_ataque": "ep13-5",
    "c5_glimmer_lab_miedo": "yt:P8AuSRsIoEQ", "c5_comision": "ep11-10", "c5_redes": "ep11-10",
    "c5_azotea_lab": "ep13-3",
    "c6_escuela": "ep15-1", "c6_ciudad": "ep15-1", "c6_mighty_glory": "ep7-1", "c6_noche_lluvia": "yt:_QCfZZ6tSf0",
    "c6_puente": "ep15-2", "c6_boda": "ep15-2", "c6_casa": "ep15-2", "c6_calle_noche": "ep15-3",
    "c6_campamento": "yt:iPFqvRACJh0", "c6_campamento_amanecer": "yt:iPFqvRACJh0",
    "c6_bosque_noche": "yt:iPFqvRACJh0", "c6_ovni_exterior": "yt:iPFqvRACJh0",
    "c7_casa_ciudad": "ep17-1", "c7_hospital": "ep17-6", "c7_campo": "ep17-2", "c7_campo_casa": "ep17-2",
    "c7_campo_noche": "yt:i59dBkWI1vA", "c7_aldea_destruida": "ep17-4", "c7_fomo": "ep11-3",
    "c7_noticias": "ep11-10", "c7_bosque_ovni": "yt:hp6fa8Hx3Ys", "c7_ovni_interior": "yt:hp6fa8Hx3Ys",
    "c7_montana": "yt:hp6fa8Hx3Ys",
    "c8_ovni_exterior": "yt:iyHElqN8Lx4", "c8_ovni_entrada": "yt:iyHElqN8Lx4", "c8_ovni_pasillo": "yt:iyHElqN8Lx4",
    "c8_ovni_hangar": "yt:PnngXEfHiyo", "c8_ovni_laboratorio": "yt:PnngXEfHiyo", "c8_ovni_salida": "yt:PnngXEfHiyo",
    "c8_ovni_ruinas": "yt:PnngXEfHiyo", "c8_fomo": "ep11-3", "c8_mighty_glory": "ep7-1",
    "c8_rock_oficina": "ep7-1", "c8_noticias": "ep11-10", "c8_azotea": "ep21-3", "c8_ciudad_miedo": "yt:PnngXEfHiyo",
    "c9_casa_dragon": "ep21-1", "c9_callejon": "ep21-1", "c9_rock_oficina": "ep7-1", "c9_treeman": "ep4-1",
    "c9_azotea_x": "ep21-8", "c9_puerto": "yt:rpzCjpmEYIA", "c9_puerto_noche": "yt:GjxwD3Xwh7M",
    "c9_oficina_fomo": "yt:JsY9KSzRknE", "c9_comision": "ep11-10", "c9_noticias": "ep11-10",
    "c9_ciudad_dragon": "yt:mL7jsdI2f6E",
    "c10_circo": "ep23-1", "c10_casa_xinya": "ep23-2", "c10_casa_nueva": "ep23-2", "c10_barrio": "yt:5dl_2BgSCww",
    "c10_plaza_barrio": "yt:5dl_2BgSCww", "c10_calle": "yt:5dl_2BgSCww", "c10_escondite": "yt:IWMTusm6bJk",
    "c10_treeman": "ep4-1", "c10_fomo": "ep11-3", "c10_noticias": "ep11-10", "c10_comision": "ep11-10",
    "c11_fomo_noche": "yt:JsY9KSzRknE", "c11_fomo_ataque": "yt:MAPIxJANBHU", "c11_tablero": "yt:G66mjVMVp0w",
    "c11_cero": "yt:G66mjVMVp0w", "c11_azotea_noche": "ep21-8", "c11_ceremonia": "yt:8QJ8KNdhkiA",
    "fin_x": "yt:G66mjVMVp0w", "fin_sin_mascara": "ep21-3", "fin_luna": "ep1-3", "fin_relampago": "ep5-1",
    "fin_cero": "ep7-1", "fin_miedo": "yt:PnngXEfHiyo", "fin_reina": "ep11-1", "fin_sin_confianza": "ep13-1",
    "fin_familia": "ep17-2", "fin_sonrisa": "ep21-2", "fin_perro": "ep23-2", "fin_caida_x": "yt:MAPIxJANBHU",
    "fin_oficinista": "yt:JsY9KSzRknE", "fin_llama": "yt:i59dBkWI1vA",
}


def load(src, ref):
    if ref.startswith("yt:"):
        return pygame.image.load(os.path.join(src, "yt", ref[3:] + ".jpg")).convert()
    if ref.startswith("chara"):
        return pygame.image.load(os.path.join(src, "main", ref + ".png")).convert_alpha()
    return pygame.image.load(os.path.join(src, "other", ref + ".jpg")).convert()


def scene_crop(img, ref):
    """Quita las franjas negras (capturas) o los textos/logos (miniaturas de YouTube)."""
    w, h = img.get_size()
    if ref.startswith("yt:"):
        r = pygame.Rect(0, int(h * .17), w, int(h * .66))
    else:
        r = pygame.Rect(0, int(h * .12), w, int(h * .76))
    return img.subsurface(r).copy()


def bust(img):
    """Recorta de cabeza a cintura una ilustración con fondo transparente."""
    box = img.get_bounding_rect(min_alpha=40)
    fig = img.subsurface(box).copy()
    fw, fh = fig.get_size()
    h = min(fh, int(fw / .72) if fh < fw * 1.2 else int(fh * .52))
    w = min(fw, int(h * .9))
    x = (fw - w) // 2
    return fig.subsurface(pygame.Rect(x, 0, w, h)).copy()


def frame(img, cx):
    w, h = img.get_size()
    top, bot = int(h * .12), int(h * .88)
    ch = bot - top
    cw = int(ch * .78)
    x = max(0, min(w - cw, int(w * cx - cw / 2)))
    return img.subsurface(pygame.Rect(x, top, cw, ch)).copy()


def main():
    src = sys.argv[1]
    pygame.init()
    pygame.display.set_mode((8, 8))
    for d in ("personajes", "cartas", "anime", "fondos"):
        os.makedirs(os.path.join(ASSETS, d), exist_ok=True)
    n = 0
    for name, ref in CUTOUTS.items():
        pygame.image.save(bust(load(src, ref)), os.path.join(ASSETS, "personajes", slug(name) + ".png"))
        n += 1
    for name, (ref, cx) in FRAMES.items():
        pygame.image.save(frame(load(src, ref), cx), os.path.join(ASSETS, "personajes", slug(name) + ".png"))
        n += 1
    for num, ref in CARDS.items():
        img = load(src, ref)
        if ref.startswith("yt:"):
            img = scene_crop(img, ref)
        else:
            img = img.subsurface(img.get_bounding_rect(min_alpha=40)).copy()
        pygame.image.save(img, os.path.join(ASSETS, "cartas", f"cap{num:02d}.png"))
        n += 1
    used = set(F.values()) | {f"yt:{v}" for v in TITLES.values()}
    for ref in used:
        if ref.startswith("yt:") and ref[3:] in TITLES.values() and ref not in F.values():
            continue
        name = ref.replace("yt:", "yt_")
        pygame.image.save(scene_crop(load(src, ref), ref), os.path.join(ASSETS, "anime", name + ".jpg"))
        n += 1
    for num, vid in TITLES.items():
        pygame.image.save(load(src, "yt:" + vid), os.path.join(ASSETS, "fondos", f"cap{num:02d}_titulo.jpg"))
        n += 1
    mapa = {k: v.replace("yt:", "yt_") + ".jpg" for k, v in F.items()}
    with open(os.path.join(ASSETS, "anime", "mapa_fondos.json"), "w", encoding="utf-8") as f:
        json.dump(mapa, f, indent=1, ensure_ascii=False)
    print(f"{n} imágenes colocadas en assets/")


if __name__ == "__main__":
    main()
