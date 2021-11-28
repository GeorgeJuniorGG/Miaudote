from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.clock import Clock
from kivy.utils import get_color_from_hex

from mui.adopterrequests.components.PetItem2 import PetItem2
from mui.home.components.Separator import Separator
from mui.ColorTheme import Color

class FavoritesScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.cor = Color()

        # Apenas para ilustrar
        # os itens verdadeiros seram pegos do firebase
        item = {
                 'imageSource': 'mrbubbles.png',
                 'petName': 'Mr. Bubbles',
                 'petDecription': "Bubbles vivia em um lar em Jardins, São Paulo, até que seus donos...",
                 'petChars': ['Branco', 'Macho', 'Campinas']
               }

        items = []
        for i in range(9):
            items.append(item)

        Clock.schedule_once(lambda x: self.insert_items(items))
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = PetItem2(items[i])
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def remove_favorite_dialog(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.azulEscuro()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.go_forward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.vermelho()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja remover o animal da sua lista de favoritos?"

        self.dialog = MDDialog(text="[color=get_color_from_hex(self.cor.branco())]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def go_forward(self, obj):
        self.dialog.dismiss()
        pass