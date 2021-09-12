from kivy.uix.relativelayout import RelativeLayout
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
from kivy.resources import resource_add_path
from kivy.core.window import Window

import os
from pathlib import Path

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"
KV_DIR = f"{os.environ['MIAUDOTE_ROOT']}/libs/kvfiles"

# Permitir que o Kivy procure arquivos nestes diretórios
resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class MainApp(App, MDApp):

    # Modo de Debug
    DEBUG = 1

    KV_FILES = {
        f'{KV_DIR}/ScreenManager.kv',
        f'{KV_DIR}/RootScreen.kv',
        f'{KV_DIR}/WelcomeScreen.kv',
        f'{KV_DIR}/LoginScreen.kv',
        f'{KV_DIR}/MyScreen.kv',
        f'{KV_DIR}/CadScreen.kv', 
    }

    CLASSES = {
        'RootScreen': 'libs.baseclass.RootScreen',
        'MainScreenManager' : 'libs.baseclass.ScreenManager',
        'WelcomeScreen': 'libs.baseclass.WelcomeScreen',
        'MyScreen' : 'libs.baseclass.MyScreen',
        'CadScreen' : 'libs.baseclass.CadScreen',
    }

    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]

    def build_app(self,*args):
        return Factory.MainScreenManager()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()

    def change_screen(self, screen):
        if isinstance(self.root, RelativeLayout):
            self.root.children[0].current = screen
            print(self.root.children[0].current)
        else:
            self.root.current = screen
            print(self.root.current)
            

MainApp().run()