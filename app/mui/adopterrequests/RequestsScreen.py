from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from functools import partial
from kivy.utils import get_color_from_hex

from mui.protectorrequests.components.ARItem import ARItem
from mui.home.components.Separator import Separator
from mui.ColorTheme import Color
from kivy.uix.label import Label
from kivy.metrics import dp

class RequestsScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.controller = None
        self.cor = Color()
    
    def addViewRequests(self):
        requests = self.controller.getRequests()

        try:
            if(len(requests) == 0):
                self.showMessage()
    
            else:

                for req in requests:
                    msg = f'Aguardando a resposta do protetor de {req["petName"]}.'
                    if req['arStatus'] == True:
                        msg = f'O protetor de {req["petName"]} aprovou sua solicitação. Agora você pode conversar com o protetor!'
                    elif req['arStatus'] == False:
                        msg = f'O protetor de {req["petName"]} recusou sua solicitação de adoção.'
                        
                    req['description'] = msg

                self.insert_items(requests)

        except:
            self.showMessage()
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = ARItem(items[i], self)
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def showMessage(self):
        self.ids.container.clear_widgets()

        label = Label()
        label.text = "Você não tem nenhuma solicitação"
        label.color = get_color_from_hex(self.cor.vermelhoEscuro())
        label.font_size = dp(18)
        label.bold = True
        label.padding_y = 30
        label.padding_x = 10
        label.valign = "center"
        label.halign = "center"
        
        self.ids.container.add_widget(label)

    def removeItem(self, arID:str):
        self.controller.removeRequest(arID)
        self.updateItems()
    
    def updateItems(self):
        self.ids.container.clear_widgets()
        self.addViewRequests()

    def remove_item_dialog(self, arID:str, obj):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.azulEscuro()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=partial(self.go_forward, arID))

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.vermelho()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja remover essa solicitação?"

        self.dialog = MDDialog(text="[color=get_color_from_hex(self.cor.branco())]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def go_forward(self, arID:str, obj):
        self.dialog.dismiss()
        self.removeItem(arID)

    def openRequest(self, arID:str):
        self.controller.openRequest(arID)

    def openChat(self, arID:str, obj):
        self.controller.openChat(arID)