from kivy.uix.screenmanager import ScreenManager
from kivy.uix.relativelayout import RelativeLayout

class MainScreenManager(ScreenManager):
    usualLoginFlow = ["RootScreen", "LoginScreen"]
    usualProtectorSignUpFlow = ["RootScreen", "SignUpScreen", "SignUpScreen2b", "LoginScreen"]
    usualSignUpFlow = ["RootScreen", "SignUpScreen", "SignUpScreen2a", "SignUpScreen3", "SignUpScreen4", "LoginScreen"]

    def change_screen(self, screen):
        if isinstance(self, RelativeLayout):
            self.children[0].current = screen
            print(self.children[0].current)
        else:
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