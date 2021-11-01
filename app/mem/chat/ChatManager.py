from kivy.uix.screenmanager import ScreenManager
from mui.chat.ChatScreen import (ChatScreen, 
                         MenssageReceived, MenssageSent)
from kivy.clock import Clock

class ChatManager:

    def __init__(self, chatScreen:ChatScreen, manager:ScreenManager):
        self.chatScreen = chatScreen
        self.chatScreen.controller = self
        self.manager = manager

    def response(self, *args):
        if value == "Olá" or value == "ola":
            response = "Olá Jhonatan, Tudo Bem?\n"+\
                       "Vi que teve interesse em um dos animais que estou doando, "+\
                        "gostaria de conversar mais sobre a possível adoção."

        elif value == "Estou Bem! E Você?":
            response = "Estou bem também, obrigado!"
        
        else:
            response = ""

        self.chatScreen.add_widget(MenssageReceived(text=response, size_hint_x=.72, halign="left"))

    def send(self):
        global size, halign, value
        chat_screen = self.chatScreen
        if chat_screen.text_input != "":
            value = chat_screen.text_input.text
            len_v = len(value) 
            if(len_v < 6):
                size = .22
                halign = "center"

            elif(len_v < 11):
                size = .32
                halign = "center"

            elif(len_v < 16):
                size = .45
                halign = "center"

            elif(len_v < 21):
                size = .58
                halign = "center"

            elif(len_v < 26):
                size = .71
                halign = "left"
            
            else:
                size = .77
                halign = "left"

            chat_screen.chat_list.add_widget(MenssageSent(text=value, size_hint_x=size, halign=halign))
            Clock.schedule_once(self.response, 1)
            chat_screen.text_input.text = ""    