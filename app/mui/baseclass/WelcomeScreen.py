from kivymd.uix.floatlayout import MDFloatLayout

class WelcomeScreen(MDFloatLayout):
    
    def welcome_to_signup(self):
        self.parent.manager.welcome_to_signup()
    
    def welcome_to_login(self):
        self.parent.manager.welcome_to_login()