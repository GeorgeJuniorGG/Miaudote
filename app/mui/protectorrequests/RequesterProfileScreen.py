from functools import partial
from kivy.utils import get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from mui.ColorTheme import Color
from kivy.clock import Clock

class RequesterProfileScreen(MDFloatLayout, MDScreen):
    
    controller = None
    cor = Color()
    arStatus = None

    def insertAdopterData(self):
        data = self.controller.adopterProfileData()
        self.arStatus = data['arStatus']
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

    def approveRequest(self):
        self.controller.approveRequest()
        #Clock.schedule_once(lambda x: partial(self.manager.goBackward,'right'), 5)

    def declineRequest(self):
        self.controller.declineRequest()
        #self.manager.goBackward('right')
        #Clock.schedule_once(lambda x: partial(self.manager.goBackward,'right'), 5)

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))

    def hideButtons(self):
        if self.arStatus != None:
            self.remove_widget(self.ids.acceptButton)
            self.remove_widget(self.ids.rejectButton)