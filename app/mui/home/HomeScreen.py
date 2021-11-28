from kivymd.uix.screen import MDScreen

from .components.PetItem import PetItem
from .components.Separator import Separator

class HomeScreen(MDScreen):

    controller = None

    def __init__(self, **kw):
        super().__init__(**kw)
        # Apenas para ilustrar
        # os itens verdadeiros seram pegos do firebase
        # item = {
        #          'imageSource': 'dog.jpg',
        #          'petName': 'Willian',
        #          'petDecription': "Willian vivia em um lar em Jardins, São Paulo, até que seus donos tiveram que sair do país e resoveram não levá-lo...",
        #          'petChars': ['Pintado', 'Macho', 'Campinas']
        #        }

        # items = []
        # for i in range(9):
        #     items.append(item)

        # Clock.schedule_once(lambda x: self.insert_items(items))
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = PetItem(items[i])
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def addViewPets(self):
        # Pega todos os Pets no Firebase
        pets = self.controller.getAllPets()

        petItemData = list()
        for pet in pets:
            pData = {
                'imageSource': 'sem_imagem.png',
                'name': pet['name'],
                'details': pet['details'][:65] + '...',
                'petChars': [pet['sex'],
                             pet['size'],
                             pet['color']]                
            }

            petItemData.append(pData)
        
        self.insert_items(petItemData)

    def search(self, search_text):
        print("BUSCAR --> " + search_text)

    def on_touch(self, id):
        print("ID " + id)
