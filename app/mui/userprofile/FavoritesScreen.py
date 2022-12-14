from kivymd import toast
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from functools import partial
from kivy.utils import get_color_from_hex

from mui.userprofile.components.PetItem2 import PetItem2
from mui.home.components.Separator import Separator
from mui.ColorTheme import Color
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

class FavoritesScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = None
        self.cor = Color()
    
    def addViewPets(self):
        # Pega todos os Pets dos favoritos do usuario
        pets = self.controller.getFavorites()

        if(len(pets) == 0):
            self.showMessage()
            
        else:
            petItemData = list()

            for pet in pets:
                pData = {
                    'imageSource': pet['images'][0],
                    'petName': pet['name'],
                        'petDecription': pet['details'][:65] + '...',
                    'pid': pet['pid'],
                    'petChars': [pet['sex'],
                                pet['size'],
                                pet['color']]                
                }

                petItemData.append(pData)
                    
            self.insert_items(petItemData)
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = PetItem2(items[i], self)
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def showMessage(self):
        self.ids.container.clear_widgets()

        label = Label()
        label.text = "Você não possui nenhum favorito"
        label.color = get_color_from_hex(self.cor.vermelhoEscuro())
        label.font_size = dp(18)
        label.bold = True
        label.padding_y = 30
        label.padding_x = 10
        label.valign = "center"
        label.halign = "center"
        
        self.ids.container.add_widget(label)
    
    def removeItem(self, petID:str):
        self.controller.removeFavorite(petID)
        self.updateItems()
    
    def updateItems(self):
        self.ids.container.clear_widgets()
        self.addViewPets()

    def remove_item_dialog(self, petID:str, obj):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.azulEscuro()),
                                        on_release=partial(self.go_forward, petID))

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.vermelho()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza de que deseja remover o animal dos seus favoritos?"

        self.dialog = MDDialog(text="[color=#ffffff]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def go_forward(self, petID:str, obj):
        self.dialog.dismiss()
        self.removeItem(petID)

    def openPetProfile(self, petID:str):
        self.controller.openPetProfile(petID)

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))