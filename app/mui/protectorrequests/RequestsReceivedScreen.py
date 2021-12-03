from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list.list import ImageLeftWidget, OneLineAvatarListItem

from kivy.clock import Clock
from kivy.utils import get_color_from_hex

from mui.ColorTheme import Color

class RequestsReceivedScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cor = Color()
        self.controller = None
        Clock.schedule_once(self.on_start)
    
    def on_start(self, interval):
        for i in range(9):
            item = OneLineAvatarListItem(text=f"Usuário {i}", 
                   theme_text_color="Custom", text_color=get_color_from_hex(self.cor.vermelho()),
                   divider_color=get_color_from_hex(self.cor.vermelho()))
            image = ImageLeftWidget(source = "mrbubbles.png")
            
            item.add_widget(image)
            self.ids.container.add_widget(item)