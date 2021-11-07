from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

class PetSignUpScreen(MDFloatLayout, MDScreen):
    def go_backward(self):
        self.manager.go_backward_pet_signup("PetSignUpScreen")
    def go_forward(self):
        self.manager.go_forward_pet_signup("PetSignUpScreen")