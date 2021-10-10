from services.firebaseAuth import login
from kivymd.uix.screen import MDScreen

class LoginScreen(MDScreen):
   def login(self, email, password):
      if(login(self, email, password)):
         print("Entrando...")
      else:
         print("E-mail ou senha incorreto")