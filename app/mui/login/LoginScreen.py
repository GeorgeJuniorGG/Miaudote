from mlo.services.firebaseAuth import FireBaseAuthService
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty

class LoginScreen(MDScreen):

   authService = ObjectProperty()

   def __init__(self, **kw):
      super().__init__(**kw)
      self.authService = FireBaseAuthService()

   def login(self, email, password):

      if(self.authService.login(email, password)):
         print("Entrando...")
      else:
         print("E-mail ou senha incorreto")
   
   def go_forward(self):
        self.manager.go_forward_login("LoginScreen")

   def go_backward(self):
        self.manager.go_backward_login("LoginScreen")