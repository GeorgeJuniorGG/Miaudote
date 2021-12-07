from kivymd.uix.screen import MDScreen
from kivymd.toast import toast

from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

from mui.ColorTheme import Color

class LoginScreen(MDScreen):
   cor = Color()
   controller = ObjectProperty()

   def __init__(self, **kw):
      super().__init__(**kw)
      self.controller = None

   def go_forward(self):
      self.manager.go_forward_login("LoginScreen")

   def go_backward(self):
      self.manager.go_backward_login("LoginScreen")

   def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))