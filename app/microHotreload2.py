import os
from pathlib import Path
from kivy.resources import resource_add_path
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from mem.user.FavoriteManager import FavoriteManager
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mlo.database.firebaseUserDB import FUserDB
from mlo.database.firebasePetDB import FPetDB

from mem.filechooser.FMClient import FMClient
from mem.filechooser.FileManager import FileManager
from mui.filechooser.FileChooserScreen import FileChooserScreen

from mem.screenmanager.MainScreenManager import MainScreenManager
from orchestrator import Orchestrator
from mem.screenmanager.screens import screens

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
                 'mui/filechooser/FileChooserScreen.kv',
                 'mui/petprofile/PetSignUpScreen.kv',
                 'mui/petprofile/PetSignUpScreen2.kv',
                 'mui/petprofile/PetSignUpScreen3.kv',
                 'mui/petprofile/PetSignUpScreen4.kv',

               ]
    DEBUG = True

    CLASSES = {
        # 'FavoritesScreen': 'mui.userprofile.FavoritesScreen',
        # 'PetItem2': 'mui.adopterrequests.components.PetItem2',
        # 'MiauLogo': 'mui.logo.components.MiauLogo',
        'FileChooserScreen': 'mui.filechooser.FileChooserScreen',
        'FileManager': 'mem.filechooser.FileManager',
        'PetSignUpManager': 'mem.petSignUp.petSignUpManager'
    }

    def build_app(self):
        global manager
        manager = MainScreenManager()
        orchestrator = Orchestrator(manager)
        # uDB = FUserDB('1KNReiiLyeguu1FZVtM926FPAHa2')
        # pDB = FPetDB()
        # uS = UserService(uDB)
        # pS = PetService(pDB)
        # controller = FavoriteManager(uS, pS)
        # screen = controller.screen
        
        controller = orchestrator.buildComponent(screens['petSignUp'])
        controller.manager = manager
        controller.addScreens()
        
        manager.changeScreen('left', controller.petSignUpScreen4.name)

        return manager


CustomApp().run()