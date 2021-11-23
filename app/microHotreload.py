import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from mui.root.RootScreen import RootScreen


os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class CustomApp( MDApp):
    manager: ScreenManager
    KV_FILES = [ 
                 'mui/root/RootScreen.kv',
                 'mui/menu/MiaudoteMenuScreen.kv',
                 'mui/menu/components/menuItem.kv',
                 'mui/home/HomeScreen.kv',
                 'mui/home/components/PetItem.kv',
                 'mui/home/components/Separator.kv',
                 'mui/userprofile/ProfileScreen.kv',
                 'mui/userprofile/components/UserInfo.kv',
                 'mui/userprofile/FavoritesScreen.kv',
                 'mui/adopterrequests/components/PetItem2.kv'
               ]
    DEBUG = True

    CLASSES = {
        'HomeScreen': 'mui.home.HomeScreen',
        'PetItem': 'mui.home.components.PetItem',
        'MiaudoteMenuScreen': 'mui.menu.MiaudoteMenuScreen',
        'MenuItem': 'mui.menu.components.MenuItem',
        'ProfileScreen': 'mui.userprofile.ProfileScreen',
        'UserInfo': 'mui.userprofile.components.UserInfo',
        'FavoritesScreen' : 'mui.userprofile.FavoritesScreen',
        'PetItem2': 'mui.adoptationrequests.components.PetItem2'
    }

    def build_app(self):
        #global manager
        self.manager = ScreenManager()
        self.manager.add_widget(RootScreen(name='Root'))
        return self.manager

    def change_screen(self, screen):
        print(self.manager.current)
        self.manager.transition = SlideTransition()
        self.manager.transition.direction = 'up'
        self.manager.add_widget(screen)
        self.manager.current = screen.name
        print(self.manager.current)


CustomApp().run()