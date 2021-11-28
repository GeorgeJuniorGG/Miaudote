from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

class LoginScreen(MDScreen):

   controller = ObjectProperty()

   def __init__(self, **kw):
      super().__init__(**kw)
      self.controller = None

   def go_forward(self):
      self.manager.go_forward_login("LoginScreen")

   def go_backward(self):
      self.manager.go_backward_login("LoginScreen")