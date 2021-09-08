from kivy.core.window import Window

from kivymd.uix.floatlayout import MDFloatLayout


Window.size= (375,667)

class LoginScreen(MDFloatLayout):
     def login(self):
        print('logando...')

