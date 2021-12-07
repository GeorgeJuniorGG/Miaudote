from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

from mui.ColorTheme import Color

class SignUpScreen2a(MDFloatLayout, MDScreen):
    cor = Color()
    controller = ObjectProperty()

    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen2a")

    def go_backward(self):
        #self.manager.go_backward_signup("SignUpScreen2a")
        self.controller.backward(self.name)

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))