"""Visor de videos de YouTube (oficiales) en una ventana propia, usando pywebview.

Se ejecuta como proceso aparte desde el juego:
    python -m engine.visor_web <id> video  "<título>" <vol>                  -> ventana propia
    python -m engine.visor_web <id> widget "<título>" <vol> <hwnd> x y w h   -> incrustado en el juego
    python -m engine.visor_web <id> audio  "<título>" <vol>                  -> soundtrack en bucle

En modo widget, x y w h son fracciones (0-1) del área lógica del juego (1280x720). El visor
se pega encima de ese rectángulo de la ventana del juego y la sigue si se mueve o cambia de tamaño.
"""
import ctypes
import os
import sys
import tempfile
import time

os.environ.setdefault("WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS",
                      "--autoplay-policy=no-user-gesture-required")

import webview  # noqa: E402

PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<style>html,body{{margin:0;height:100%;background:#000;overflow:hidden}}
#p{{position:fixed;inset:0;width:100vw;height:100vh}}
#skip{{position:fixed;right:18px;bottom:18px;z-index:9;font:600 15px Segoe UI,Arial;color:#fff;
background:rgba(0,0,0,.6);border:2px solid #ffc440;padding:8px 16px;cursor:pointer;transform:skewX(-12deg)}}</style>
</head><body><div id="p"></div>{skip}
<script>
var LOOP={loop}, VOL={vol};
function api(n,a){{ if(window.pywebview && window.pywebview.api) window.pywebview.api[n](a); }}
var tag=document.createElement('script'); tag.src="https://www.youtube.com/iframe_api"; document.head.appendChild(tag);
var player;
function onYouTubeIframeAPIReady(){{
  player=new YT.Player('p',{{videoId:'{vid}',
    playerVars:{{autoplay:1,controls:LOOP?0:1,rel:0,playsinline:1,loop:LOOP,playlist:'{vid}',origin:location.origin}},
    events:{{
      onReady:function(e){{e.target.setVolume(VOL);e.target.playVideo();}},
      onStateChange:function(e){{ if(e.data===0 && !LOOP) api('cerrar'); }},
      onError:function(e){{ api('error', e.data); }}
    }}}});
}}
document.addEventListener('keydown',function(e){{ if(e.key==='Escape') api('cerrar'); }});
</script></body></html>"""


class Api:
    def __init__(self):
        self._window = None

    def cerrar(self, *_):
        self._window.destroy()

    def error(self, code=None):
        print("ERROR_YOUTUBE", code, flush=True)
        self._window.destroy()


class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long), ("right", ctypes.c_long), ("bottom", ctypes.c_long)]


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def _follow(win, uid, game, frac):
    """Mantiene la ventana del video encima del área reservada en la ventana del juego."""
    u = ctypes.windll.user32
    u.FindWindowW.restype = ctypes.c_void_p
    hwnd = None
    for _ in range(300):
        hwnd = u.FindWindowW(None, uid)
        if hwnd:
            break
        time.sleep(.05)
    if not hwnd:
        return
    # La ventana del juego pasa a ser la 'dueña': el video queda siempre encima de ella
    # (y solo de ella), y se minimiza junto con el juego.
    u.SetWindowLongPtrW(ctypes.c_void_p(hwnd), -8, ctypes.c_void_p(game))
    last = None
    while True:
        if not u.IsWindow(ctypes.c_void_p(game)):
            win.destroy()
            return
        if not u.IsWindow(ctypes.c_void_p(hwnd)):
            return
        if u.IsIconic(ctypes.c_void_p(game)):
            time.sleep(.1)
            continue
        rc, pt = RECT(), POINT(0, 0)
        u.GetClientRect(ctypes.c_void_p(game), ctypes.byref(rc))
        u.ClientToScreen(ctypes.c_void_p(game), ctypes.byref(pt))
        cw, ch = rc.right - rc.left, rc.bottom - rc.top
        sc = min(cw / 1280, ch / 720) if cw and ch else 1
        ox, oy = pt.x + (cw - 1280 * sc) / 2, pt.y + (ch - 720 * sc) / 2
        geo = (int(ox + frac[0] * 1280 * sc), int(oy + frac[1] * 720 * sc),
               int(frac[2] * 1280 * sc), int(frac[3] * 720 * sc))
        if geo != last:
            # SWP_NOZORDER | SWP_NOACTIVATE | SWP_SHOWWINDOW
            u.SetWindowPos(ctypes.c_void_p(hwnd), None, *geo, 0x0004 | 0x0010 | 0x0040)
            last = geo
        time.sleep(.04)


def main():
    if sys.platform == "win32":
        try:  # coordenadas en píxeles reales, aunque Windows use escalado (125 %, 150 %...)
            ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
        except (AttributeError, OSError):
            pass
    vid = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else "video"
    title = sys.argv[3] if len(sys.argv) > 3 else "To Be Hero X"
    vol = sys.argv[4] if len(sys.argv) > 4 else "70"
    audio = mode == "audio"
    widget = mode == "widget"
    folder = tempfile.mkdtemp(prefix="tbhx_")
    path = os.path.join(folder, "index.html")
    skip = "" if (audio or widget) else '<div id="skip" onclick="api(\'cerrar\')">SALTAR ▶▶ (ESC)</div>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(PAGE.format(vid=vid, title=title, loop=1 if audio else 0, vol=vol, skip=skip))
    api = Api()
    follow = None
    if audio:
        win = webview.create_window(title, url=path, js_api=api, width=320, height=200,
                                    minimized=True, focus=False)
    elif widget:
        game = int(sys.argv[5])
        frac = [float(v) for v in sys.argv[6:10]]
        uid = f"tbhx_widget_{os.getpid()}"
        win = webview.create_window(uid, url=path, js_api=api, width=640, height=360, x=-4000, y=-4000,
                                    frameless=True, easy_drag=False, focus=False, background_color="#000000")
        follow = lambda: _follow(win, uid, game, frac)  # noqa: E731
    else:
        win = webview.create_window(title, url=path, js_api=api, width=1280, height=720,
                                    on_top=True, background_color="#000000")
    api._window = win

    def debug():
        import time
        for _ in range(12):
            time.sleep(1.5)
            try:
                st = win.evaluate_js("player && player.getPlayerState ? player.getPlayerState() : 'sin-player'")
                print("ESTADO", st, flush=True)
                if st == 1:
                    break
            except Exception as e:  # noqa: BLE001
                print("ESTADO err", e, flush=True)
        win.destroy()

    webview.start(debug if os.environ.get("TBHX_DEBUG") else follow, http_server=True,
                  private_mode=False, storage_path=os.path.join(folder, "wv"))


if __name__ == "__main__":
    main()
