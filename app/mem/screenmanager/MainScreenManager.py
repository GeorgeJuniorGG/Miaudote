from kivy.uix.screenmanager import ScreenManager

class MainScreenManager(ScreenManager):
    usualLoginFlow = ["WelcomeScreen", "LoginScreen"]
    usualProtectorSignUpFlow = ["WelcomeScreen", "SignUpScreen", "SignUpScreen2b", "LoginScreen"]
    usualSignUpFlow = ["WelcomeScreen", "SignUpScreen", "SignUpScreen2a", "SignUpScreen3", "SignUpScreen4", "LoginScreen"]

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