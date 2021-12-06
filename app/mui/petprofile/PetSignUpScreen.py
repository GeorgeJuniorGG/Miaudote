from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.toast import toast

from kivy.metrics import dp
from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

from mui.ColorTheme import Color

class PetSignUpScreen(MDFloatLayout, MDScreen):
    cor = Color()
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        menu_items1 = [
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Fêmea",
                    "on_release": lambda x=f"Fêmea": self.set_item1(x),
                }, 
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Macho",
                    "on_release": lambda x=f"Macho": self.set_item1(x),
                }]
        
        menu_items2 = [
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Pequeno",
                    "on_release": lambda x=f"Pequeno": self.set_item2(x),
                }, 
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Médio",
                    "on_release": lambda x=f"Médio": self.set_item2(x),
                },
                {
                    "viewclass": "OneLineListItem",
                    "height": dp(56),
                    "text": f"Grande",
                    "on_release": lambda x=f"Grande": self.set_item2(x),
                }]

        self.menu1 = MDDropdownMenu(
                caller=self.ids.sex,
                items=menu_items1,
                position="center",
                width_mult=2,
            )

        self.menu2 = MDDropdownMenu(
                caller=self.ids.size,
                items=menu_items2,
                position="center",
                width_mult=3,
            )

    def set_item1(self, text__item):
        self.ids.sex.text = text__item
        self.menu1.dismiss()

    def set_item2(self, text__item):
        self.ids.size.text = text__item
        self.menu2.dismiss()

    def go_backward(self):
        # self.manager.go_backward_pet_signup("PetSignUpScreen")
        self.controller.backward(self.name)
    
    def go_forward(self):
        self.manager.go_forward_pet_signup("PetSignUpScreen")

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))