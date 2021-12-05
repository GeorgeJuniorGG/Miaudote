import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mem.filechooser.FMClient import FMClient
from mem.filechooser.FileManager import FileManager
from mui.filechooser.FileChooserScreen import FileChooserScreen

from mem.screenmanager.MainScreenManager import MainScreenManager
from orchestrator import Orchestrator
from mem.screenmanager.screens import screens

from mui.protectorrequests.RequesterProfileScreen import RequesterProfileScreen

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)

# Permitir que o Kivy procure arquivos nestes diretórios
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"

resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class CustomApp( MDApp):
    KV_FILES = [ 
                #  'mui/userprofile/FavoritesScreen.kv',
                #  'mui/adopterrequests/components/PetItem2.kv',
                #  'mui/logo/components/Logo.kv',
                #  'mui/filechooser/FileChooserScreen.kv',
                #  'mui/petprofile/PetSignUpScreen.kv',
                #  'mui/petprofile/PetSignUpScreen2.kv',
                #  'mui/petprofile/PetSignUpScreen3.kv',
                #  'mui/petprofile/PetSignUpScreen4.kv',
                # 'mui/protectorrequests/RequesterProfileScreen.kv',
                # 'mui/userprofile/components/UserInfo.kv',
                'mui/logo/components/Logo.kv',
                'mui/protectorrequests/RequestsReceivedScreen.kv',
                'mui/protectorrequests/components/ARItem.kv'

               ]
    DEBUG = True

    CLASSES = {
        # 'FavoritesScreen': 'mui.userprofile.FavoritesScreen',
        # 'PetItem2': 'mui.adopterrequests.components.PetItem2',
        # 'MiauLogo': 'mui.logo.components.MiauLogo',
        # 'FileChooserScreen': 'mui.filechooser.FileChooserScreen',
        # 'FileManager': 'mem.filechooser.FileManager',
        # 'PetSignUpManager': 'mem.petSignUp.petSignUpManager',
        # 'UserInfo': 'mui.userprofile.components.UserInfo',
        'MiauLogo': 'mui.logo.components.MiauLogo'
    }

    def build_app(self):
        manager = MainScreenManager()
        orchestrator = Orchestrator(manager)
        controller = orchestrator.buildComponent(screens['recRequests'])
        #controller.manager = manager
        #controller.addScreens()
        screen = controller.screen
        manager.add_widget(screen)
        manager.changeScreen('left', screen.name)


        return manager


CustomApp().run()