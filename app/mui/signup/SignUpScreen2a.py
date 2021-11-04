from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

class SignUpScreen2a(MDFloatLayout, MDScreen):
    
    controller = ObjectProperty()

    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen2a")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen2a")