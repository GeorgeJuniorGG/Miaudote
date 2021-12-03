from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

class RequesterProfileScreen(MDFloatLayout, MDScreen):
    
    controller = None

    def insertAdopterData(self):
        data = self.controller.adopterProfileData()
        for itemName in self.ids:
            item = self.ids[itemName]
            if itemName == 'adopterImage':
                item.source = data[itemName]

            elif itemName == 'city':
                value = f'{data[itemName]} / {data["state"]}'
                item.fieldValue = value
            elif itemName in data.keys():
                item.fieldValue = data[itemName]        

        for itemName in data['homeCharacteristics']:
            if itemName in self.ids:
                item = self.ids[itemName]
                value = data['homeCharacteristics'][itemName]

                if itemName == 'availableSpace':
                    area = 'Área Fechada'
                    if data['homeCharacteristics']['openArea']:
                        area = 'Área Aberta'

                    value = f"{data['homeCharacteristics']['houseType']} / {area} / {value}"

                elif type(value) == bool:
                    value = 'Sim' if value else 'Não'

                item.fieldValue = value
