from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

from functools import partial

from mui.adopterrequests.components.PetItem2 import PetItem2
from mui.home.components.Separator import Separator
from mui.ColorTheme import Color

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
                reqItemData = list()

                for req in requests:
                    reqData = {
                        'imageSource': req['images'][0],
                        'petName': req['name'],
                        'petDecription': req['details'][:65] + '...',
                        'pid': req['pid'],
                        'petChars': [req['sex'],
                                    req['size'],
                                    req['color']]                
                    }

                    reqItemData.append(reqData)
                    
                self.insert_items(reqItemData)

        except:
            self.showMessage()
    
    def insert_items(self, items:list):
        for i in range(len(items)):
            petItem = PetItem2(items[i])
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

    def removeItem(self, petID:str):
        self.controller.removeRequest(petID)
        self.updateItems()
    
    def updateItems(self):
        self.ids.container.clear_widgets()
        self.addViewRequests()

    def remove_item_dialog(self, petID:str):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.azulEscuro()),
                                        on_release=partial(self.go_forward, petID))

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.vermelho()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja remover essa solicitação?"

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