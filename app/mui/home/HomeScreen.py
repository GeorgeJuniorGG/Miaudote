from logging import root
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list.list import IRightBody, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.clock import Clock

from mui.ColorTheme import Color

class HomeScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.on_start)
    
    def on_start(self, interval):
        cor = Color()

        for i in range(9):
            item = ThreeLineAvatarListItem(text=f"Mr. Bubbles {i}", 
                   theme_text_color="Custom", text_color=cor.rgbVermelho(),
                   secondary_text="Características", tertiary_text = "Bubbles...",
                   tertiary_theme_text_color="Custom", tertiary_text_color=cor.textoL(), 
                   divider_color=cor.rgbVermelho())
            image = ImageLeftWidget(source = "mrbubbles.png")

            item.add_widget(image)
            self.ids.container.add_widget(item)
    
    def search(self, search_text):
        print("BUSCAR --> " + search_text)

    def on_touch(self, id):
        print("ID " + id)
