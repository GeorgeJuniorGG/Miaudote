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
KV_DIR = f"{os.environ['MIAUDOTE_ROOT']}/mui/kvfiles"

# Permitir que o Kivy procure arquivos nestes diretórios
resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class MainApp(App, MDApp):

    # Modo de Debug
    DEBUG = 1

    KV_FILES = {
        f'{KV_DIR}/ScreenManager.kv',
        f'{KV_DIR}/WelcomeScreen.kv',
        f'{KV_DIR}/LoginScreen.kv',
        f'{KV_DIR}/SignUpScreen.kv',
        f'{KV_DIR}/SignUpScreen2a.kv',
        f'{KV_DIR}/SignUpScreen2b.kv',
        f'{KV_DIR}/SignUpScreen3.kv',
        f'{KV_DIR}/SignUpScreen4.kv',
    }

    CLASSES = {
        'MainScreenManager' : 'mui.baseclass.ScreenManager',
        'WelcomeScreen': 'mui.baseclass.WelcomeScreen',
        'SignUpScreen' : 'mui.baseclass.SignUpScreen',
        'SignUpScreen2a' : 'mui.baseclass.SignUpScreen2a',
        'SignUpScreen2b' : 'mui.baseclass.SignUpScreen2b',
        'SignUpScreen3' : 'mui.baseclass.SignUpScreen3',
        'SignUpScreen4' : 'mui.baseclass.SignUpScreen4',
    }

    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]

    def build_app(self,*args):
        return Factory.MainScreenManager()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()            

MainApp().run()