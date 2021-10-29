from services.authService import AuthService
from services.firebaseAuth import FireBaseAuthService
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