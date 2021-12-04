from functools import partial
from kivy.metrics import dp
from kivymd.uix.button.button import MDFillRoundFlatButton
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.label.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.utils import get_color_from_hex

from .components.ARItem import ARItem
from mui.home.components.Separator import Separator

from mui.ColorTheme import Color

class RequestsReceivedScreen(MDScreen, MDFloatLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.cor = Color()
        self.controller = None

    def addRequestsViews(self):
        # Pega todas as requisições de adoção
        requests = self.controller.getRequests()

        try:
            if(len(requests) == 0):
                self.showMessage()
            
            else:                    
                self.insert_items(requests)
        
        except:
            self.showMessage()

    def showMessage(self):
        self.ids.container.clear_widgets()

        label = MDLabel()
        label.text = "Seus Pets não possuem solicitações de adoção."
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
        self.addRequestsViews()

    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = ARItem(items[i], self)
            self.ids.container.add_widget(petItem)
            self.ids.container.add_widget(Separator())
            self.ids.container.ids[f'item{i}'] = petItem

    def remove_item_dialog(self, arID:str, obj):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.azulEscuro()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=partial(self.go_forward, arID))

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.vermelho()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja recusar a solicitação de adoção?"

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