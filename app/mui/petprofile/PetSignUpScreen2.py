from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu

class PetSignUpScreen2(MDFloatLayout, MDScreen):
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        menu_items1 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Aberto",
                "on_release": lambda x=f"Aberto": self.set_item1(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Fechado",
                "on_release": lambda x=f"Fechado": self.set_item1(x),
            }]

        self.menu1 = MDDropdownMenu(
            caller=self.ids.ambient,
            items=menu_items1,
            position="center",
            width_mult=2,
        )

    def set_item1(self, text__item):
        self.ids.ambient.text = text__item
        self.menu1.dismiss()


    def go_backward(self):
        # self.manager.go_backward_pet_signup("PetSignUpScreen")
        self.controller.backward(self.name)
    def go_forward(self):
        self.manager.go_forward_pet_signup("PetSignUpScreen")