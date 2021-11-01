from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

class MenssageSent(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17

class MenssageReceived(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_size = 17


class ChatScreen(MDScreen, MDFloatLayout):
    controller = ObjectProperty()