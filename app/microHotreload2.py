import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mui.userprofile.ProfileScreen import ProfileScreen


os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class CustomApp( MDApp):
    KV_FILES = [ 
                 'mui/userprofile/ProfileScreen.kv',
                 'mui/userprofile/components/UserInfo.kv'
               ]
    DEBUG = True

    CLASSES = {
        'ProfileScreen': 'mui.userprofile.ProfileScreen',
        'UserInfo': 'mui.userprofile.components.UserInfo'
    }

    def build_app(self):
        global manager
        manager = ScreenManager()
        manager.add_widget(ProfileScreen())
        return manager


CustomApp().run()