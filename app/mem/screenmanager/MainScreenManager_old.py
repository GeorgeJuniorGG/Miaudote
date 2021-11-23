from kivy.uix.screenmanager import ScreenManager
from mem.signUp.signUpManager import SignUpManager

class MainScreenManager(ScreenManager):
    usualLoginFlow = ["WelcomeScreen", "LoginScreen"]
    usualProtectorSignUpFlow = ["WelcomeScreen", "SignUpScreen", "SignUpScreen2b", "LoginScreen"]
    usualSignUpFlow = ["WelcomeScreen", "SignUpScreen", "SignUpScreen2a", "SignUpScreen3", "SignUpScreen4", "LoginScreen"]
    usualPetSignUpFlow = ["PetSignUpScreen", "PetSignUpScreen2"]

    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     signUpScreen = self.get_screen('SignUpScreen')
    #     signUpScreen2a = self.get_screen('SignUpScreen2a')
    #     signUpScreen2b = self.get_screen('SignUpScreen2b')
    #     signUpScreen3 = self.get_screen('SignUpScreen3')
    #     signUpScreen4 = self.get_screen('SignUpScreen4')

    #     signUpManager = SignUpManager(signUpScreen, signUpScreen2a, signUpScreen2b, signUpScreen3, signUpScreen4, ScreenManager)

    def change_screen(self, screen):
        self.current = screen
        print(self.current)

    def welcome_to_signup(self):
        self.transition.direction = 'left'
        self.change_screen(self.usualSignUpFlow[1])
    
    def welcome_to_login(self):
        self.transition.direction = 'left'
        self.change_screen(self.usualLoginFlow[1])

    def go_forward_login(self, screenId):
        self.transition.direction = 'left'
        position = self.usualLoginFlow.index(screenId)
        self.change_screen(self.usualLoginFlow[position + 1])
    
    def go_backward_login(self, screenId):
        self.transition.direction = 'right'
        position = self.usualLoginFlow.index(screenId)
        self.change_screen(self.usualLoginFlow[position - 1])

    def go_forward_protector_signup(self, screenId):
        self.transition.direction = 'left'
        position = self.usualProtectorSignUpFlow.index(screenId)
        self.change_screen(self.usualProtectorSignUpFlow[position + 1])

    def go_backward_protector_signup(self, screenId):
        self.transition.direction = 'right'
        position = self.usualProtectorSignUpFlow.index(screenId)
        self.change_screen(self.usualProtectorSignUpFlow[position - 1])

    def go_forward_signup(self, screenId):
        self.transition.direction = 'left'
        position = self.usualSignUpFlow.index(screenId)
        self.change_screen(self.usualSignUpFlow[position + 1])
    
    def go_backward_signup(self, screenId):
        self.transition.direction = 'right'
        position = self.usualSignUpFlow.index(screenId)
        self.change_screen(self.usualSignUpFlow[position - 1])
    
    def go_forward_pet_signup(self, screenId):
        self.transition.direction = 'left'
        position = self.usualPetSignUpFlow.index(screenId)
        self.change_screen(self.usualPetSignUpFlow[position + 1])

    def go_backward_pet_signup(self, screenId):
        self.transition.direction = 'right'
        position = self.usualPetSignUpFlow.index(screenId)
        self.change_screen(self.usualPetSignUpFlow[position - 1])