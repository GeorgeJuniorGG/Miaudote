import os
from pathlib import Path

from kivy.resources import resource_add_path
from kivy.core.window import Window

from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from mui.protectorrequests.RequesterProfileScreen import RequesterProfileScreen # Mudar para screen que querem trabalhar

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class RequestsApp(MDApp):
    KV_FILES = ['mui/protectorrequests/RequesterProfileScreen.kv']
    DEBUG = True

    def build_app(self):
        global manager
        manager = ScreenManager()
        manager.add_widget(RequesterProfileScreen()) # adicionar a screen que está trabalhandp
        return manager


RequestsApp().run()