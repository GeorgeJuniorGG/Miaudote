from logging import root
from typing import List
from kivymd.uix.screen import MDScreen

from .components.PetItem import PetItem
from .components.Separator import Separator
from kivy.uix.label import Label
from mui.ColorTheme import Color
from kivy.utils import get_color_from_hex
from kivy.metrics import dp

class HomeScreen(MDScreen):

    controller = None

    def __init__(self, **kw):
        super().__init__(**kw)
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = PetItem(items[i])
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def addViewPets(self):
        # Pega todos os Pets dos recomendados
        pets = self.controller.getRecommended()

        petItemData = list()
        for pet in pets:
            pData = {
                'imageSource': pet['images'][0],
                'name': pet['name'],
                'details': pet['details'][:65] + '...',
                'petChars': [pet['sex'],
                             pet['size'],
                             pet['color']]                
            }

            petItemData.append(pData)
        
        self.insert_items(petItemData)

    def search(self, search_text):
        results = self.controller.getSearchResults(search_text)
        if (type(results) == str):
            self.showError(results)
        else:
            self.updateItems(results)

    def updateItems(self, newItems: List):
        self.ids.container.clear_widgets()

        petItemData = list()

        for pet in newItems:
            pData = {
                'imageSource': pet['images'][0],
                'name': pet['name'],
                'details': pet['details'][:65] + '...',
                'petChars': [pet['sex'],
                             pet['size'],
                             pet['color']]                
            }

            petItemData.append(pData)

        self.insert_items(petItemData)
    
    def showError(self, error: str):
        self.ids.container.clear_widgets()

        cor = Color()

        label = Label()
        label.text = error
        label.color = get_color_from_hex(cor.vermelhoEscuro())
        label.font_size = dp(18)
        label.bold = True
        label.padding_x = 10
        label.valign = "center"
        label.halign = "center"
        label.text_size = self.size
        

        self.ids.container.add_widget(label)


    def on_touch(self, id):
        print("ID " + id)
