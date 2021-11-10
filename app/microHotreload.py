import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mui.home.HomeScreen import HomeScreen


os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class CustomApp( MDApp):
    KV_FILES = [ 
                 'mui/home/HomeScreen.kv',
                 'mui/home/components/PetItem.kv',
                 'mui/home/components/Separator.kv'
               ]
    DEBUG = True

    CLASSES = {
        'HomeScreen': 'mui.home.HomeScreen',
        'PetItem': 'mui.home.components.PetItem'
    }

    def build_app(self):
        global manager
        manager = ScreenManager()
        manager.add_widget(HomeScreen())
        return manager


CustomApp().run()