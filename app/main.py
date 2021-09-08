from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

from kaki.app import App
from kivy.factory import Factory
import os

class MainApp(App, MDApp):

    DEBUG = 1

    KV_FILES = {
        #os.path.join(os.getcwd(),'libs/kvfiles/MyScreen.kv')
        './libs/kvfiles/MyScreen.kv'
    }
    CLASSES = {
        'MyScreen': 'libs.baseclass.MyScreen'
    }
    AUTORELOADER_PATHS = [
        ('.',{'recursive':True})
    ]

    def build_app(self,*args):
        return Factory.MyScreen()


MainApp().run()