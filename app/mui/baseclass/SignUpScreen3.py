from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

class SignUpScreen3(MDFloatLayout, MDScreen):
    
    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen3")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen3")