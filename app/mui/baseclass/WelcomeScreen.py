from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

class WelcomeScreen(MDScreen, MDFloatLayout):
    
    def welcome_to_signup(self):
        self.manager.welcome_to_signup()
    
    def welcome_to_login(self):
        self.manager.welcome_to_login()