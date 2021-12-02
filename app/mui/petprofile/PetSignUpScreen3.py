from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty

class PetSignUpScreen3(MDFloatLayout, MDScreen):
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        menu_items1 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Dócil",
                "on_release": lambda x=f"Dócil": self.set_item1(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Tímido",
                "on_release": lambda x=f"Tímido": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Bravo",
                "on_release": lambda x=f"Bravo": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Agitado",
                "on_release": lambda x=f"Agitado": self.set_item1(x),
            }]
        
        menu_items2 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Brincalhão",
                "on_release": lambda x=f"Brincalhão": self.set_item2(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Quieto",
                "on_release": lambda x=f"Quieto": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Dorminhoco",
                "on_release": lambda x=f"Dorminhoco": self.set_item2(x),
            }]

        menu_items3 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Filhote",
                "on_release": lambda x=f"Filhote": self.set_item3(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Jovem",
                "on_release": lambda x=f"Jovem": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Adulto",
                "on_release": lambda x=f"Adulto": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Mais velho",
                "on_release": lambda x=f"Mais velho": self.set_item3(x),
            }]
        self.menu1 = MDDropdownMenu(
            caller=self.ids._firstField,
            items=menu_items1,
            position="center",
            width_mult=4,
        )

        self.menu2 = MDDropdownMenu(
            caller=self.ids._secondField,
            items=menu_items2,
            position="center",
            width_mult=3,
        )

        self.menu3 = MDDropdownMenu(
            caller=self.ids._thirdField,
            items=menu_items3,
            position="center",
            width_mult=4,
        )
    
    def set_item1(self, text__item):
        self.ids._firstField.text = text__item
        self.menu1.dismiss()

    def set_item2(self, text__item):
        self.ids._secondField.text = text__item
        self.menu2.dismiss()
    
    def set_item3(self, text__item):
        self.ids._thirdField.text = text__item
        self.menu3.dismiss()

    def go_backward(self):
        # self.manager.go_backward_pet_signup("PetSignUpScreen3")
        self.controller.backward(self.name)
    def go_forward(self):
        self.manager.go_forward_pet_signup("PetSignUpScreen3")