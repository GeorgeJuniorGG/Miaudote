from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

class WelcomeScreen(MDScreen, MDFloatLayout):
    controller = ObjectProperty()

    def welcome_to_signup(self):
        self.manager.welcome_to_signup()
    
    def welcome_to_login(self):
        self.manager.welcome_to_login()