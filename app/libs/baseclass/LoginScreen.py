from services.firebase import loginUser, registerUser
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
   def login(self, email, password):
      if(loginUser(self, email, password)):
         print("Entrando...")
      else:
         print("E-mail ou senha incorreto")