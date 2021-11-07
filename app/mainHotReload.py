from kivymd.tools.hotreload.app import MDApp
from kivy.factory import Factory
from kivy.resources import resource_add_path
from kivy.core.window import Window

import os
from pathlib import Path

os.environ["MIAUDOTE_ROOT"] = str(Path(__file__).parent)
FONT_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/fonts"
IMG_DIR = f"{os.environ['MIAUDOTE_ROOT']}/assets/images"
KV_DIR = f"{os.environ['MIAUDOTE_ROOT']}/mui"

# Permitir que o Kivy procure arquivos nestes diretórios
resource_add_path(FONT_DIR)
resource_add_path(IMG_DIR)

Window.size = (375,667)

class MainApp(MDApp):

    # Modo de Debug
    DEBUG = 1

    KV_FILES = [
        f'mem/screenmanager/MainScreenManager.kv',
        f'{KV_DIR}/welcome/WelcomeScreen.kv',
        f'{KV_DIR}/login/LoginScreen.kv',
        f'{KV_DIR}/signup/SignUpScreen.kv',
        f'{KV_DIR}/signup/SignUpScreen2a.kv',
        f'{KV_DIR}/signup/SignUpScreen2b.kv',
        f'{KV_DIR}/signup/SignUpScreen3.kv',
        f'{KV_DIR}/signup/SignUpScreen4.kv',
        f'{KV_DIR}/userprofile/ProfileScreen.kv',
        f'{KV_DIR}/chat/ChatScreen.kv',
        f'{KV_DIR}/adopterrequests/AdoptionRScreen.kv',
        f'{KV_DIR}/adopterrequests/RequestsScreen.kv',
        f'{KV_DIR}/protectorrequests/RequesterProfileScreen.kv',
        f'{KV_DIR}/protectorrequests/RequestsReceivedScreen.kv',
        f'{KV_DIR}/userprofile/FavoritesScreen.kv',
        f'{KV_DIR}/petprofile/PetSignUpScreen.kv',
        f'{KV_DIR}/petprofile/PetSignUpScreen2.kv',
        f'{KV_DIR}/home/HomeScreen.kv'
    ]

    CLASSES = {
        'MainScreenManager' : 'mem.screenmanager.MainScreenManager',
        'WelcomeScreen': 'mui.welcome.WelcomeScreen',
        'LoginScreen': 'mui.login.LoginScreen',
        'SignUpScreen' : 'mui.signup.SignUpScreen',
        'SignUpScreen2a' : 'mui.signup.SignUpScreen2a',
        'SignUpScreen2b' : 'mui.signup.SignUpScreen2b',
        'SignUpScreen3' : 'mui.signup.SignUpScreen3',
        'SignUpScreen4' : 'mui.signup.SignUpScreen4',
        'ProfileScreen' : 'mui.userprofile.ProfileScreen',
        'AdoptionRScreen' : 'mui.adopterrequests.AdoptionRScreen',
        'ChatScreen' : 'mui.chat.ChatScreen',
        'RequestsScreen' : 'mui.adopterrequests.RequestsScreen',
        'RequesterProfileScreen' : 'mui.protectorrequests.RequesterProfileScreen',
        'RequestsReceivedScreen' : 'mui.protectorrequests.RequestsReceivedScreen',
        'FavoritesScreen' : 'mui.userprofile.FavoritesScreen',
        'PetSignUpScreen' : 'mui.petprofile.PetSignUpScreen',
        'PetSignUpScreen2' : 'mui.petprofile.PetSignUpScreen2',
        'HomeScreen' : 'mui.home.HomeScreen',
    }

    def build_app(self,*args):
        return Factory.MainScreenManager()

    def _rebuild(self, *args):
        if args[1] == 32:
            self.rebuild()            

MainApp().run()