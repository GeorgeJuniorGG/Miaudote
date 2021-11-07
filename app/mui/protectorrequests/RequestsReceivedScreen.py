from logging import root
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list.list import IconLeftWidget, OneLineAvatarListItem
from kivy.clock import Clock

from mui.ColorTheme import Color

class RequestsReceivedScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.on_start)
    
    def on_start(self, interval):
        cor = Color()

        for i in range(9):
            item = OneLineAvatarListItem(text=f"Usuário {i}", 
                   theme_text_color="Custom", text_color=cor.rgbVermelho(),
                   divider_color=cor.rgbVermelho())
            icon = IconLeftWidget(icon = "account-circle")
            
            item.add_widget(icon)
            self.ids.container.add_widget(item)

