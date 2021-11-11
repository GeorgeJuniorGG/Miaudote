from logging import root
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.clock import Clock

from mui.adopterrequests.components.PetItem2 import PetItem2
from mui.home.components.Separator import Separator

class RequestsScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)

        # Apenas para ilustrar
        # os itens verdadeiros seram pegos do firebase
        item = {
                 'imageSource': 'mrbubbles.png',
                 'petName': 'Mr. Bubbles',
                 'petDecription': "Bubbles vivia em um lar em Jardins, São Paulo, até que seus donos tiveram que sair do país e resoveram não levá-lo...",
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

