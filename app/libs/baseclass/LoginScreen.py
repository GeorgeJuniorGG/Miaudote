from services.firebase import loginUser, registerUser
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout

Window.size= (375,667)

class LoginScreen(MDFloatLayout):
   
   def login(self, email, password):
      if(loginUser(self, email, password)):
         print("Entrando...")
      else:
         print("E-mail ou senha incorreto")

