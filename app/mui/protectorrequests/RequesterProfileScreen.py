from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast

from kivy.utils import get_color_from_hex

from mui.ColorTheme import Color

class RequesterProfileScreen(MDFloatLayout, MDScreen):
    
    controller = None
    cor = Color()

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

    def approveRequest(self):
        self.controller.approveRequest()
        #Clock.schedule_once(lambda x: partial(self.manager.goBackward,'right'), 5)

    def declineRequest(self):
        self.controller.declineRequest()
        #self.manager.goBackward('right')
        #Clock.schedule_once(lambda x: partial(self.manager.goBackward,'right'), 5)

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))

    def decline_dialog(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.azulEscuro()),
                                        on_release=self.go_forward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.vermelho()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza de que deseja recusar essa solicitação?"

        self.dialog = MDDialog(text="[color=#ffffff]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()        

    def go_forward(self, obj):
        self.dialog.dismiss()
        self.declineRequest()