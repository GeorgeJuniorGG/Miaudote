from mui.welcome.WelcomeScreen import WelcomeScreen
from mem.screenmanager.screens import screens

class WelcomeManager:

    def __init__(self):
        self.screen = WelcomeScreen(name=screens['welcome'])
        self.screen.controller = self

    def welcomeToLogin(self):
        self.screen.manager.changeScreen('left', screens['login'])

    def welcomeToSignUp(self):
        self.screen.manager.changeScreen('left', screens['signUp'])