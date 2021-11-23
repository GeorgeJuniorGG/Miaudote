from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class MessageSent(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17

class MessageReceived(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17


class ChatScreen(MDScreen, MDFloatLayout):
    controller = ObjectProperty()
    text_input = ObjectProperty()
    chat_list = ObjectProperty()

    def send(self):
        msg_content = self.text_input.text

        if msg_content != "":
            self.controller.sendMessage(msg_content)
            self.createSentBalloon(msg_content)
            self.text_input.text = ""

    def ballonProps(self, msgLen:int) -> tuple:

        size: int = .22
        halign: str = 'center'

        if(msgLen < 6):
            size = .22
            halign = 'center'

        elif(msgLen < 11):
            size = .32
            halign = 'center'

        elif(msgLen < 16):
            size = .45
            halign = 'center'

        elif(msgLen < 21):
            size = .58
            halign = 'center'

        elif(msgLen < 26):
            size = .71
            halign = 'left'
        
        else:
            size = .77
            halign = 'left' 

        return size, halign

    def createReceivedBalloon(self, msg:str):
        size, halign = self.ballonProps(len(msg))
        received_balloon = MessageReceived(text=msg, size_hint_x=size, halign=halign)
        self.chat_list.add_widget(received_balloon)       

    def createSentBalloon(self, msg:str):
        size, halign = self.ballonProps(len(msg))
        sent_balloon = MessageSent(text=msg, size_hint_x=size, halign=halign)
        self.chat_list.add_widget(sent_balloon)           
