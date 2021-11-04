from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty

class SignUpScreen3(MDScreen, MDFloatLayout):
    controller = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._late_init)

    def _late_init(self, interval):
        menu_items1 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 1",
                "on_release": lambda x=f"Opção 1": self.set_item1(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 2",
                "on_release": lambda x=f"Opção 2": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 3",
                "on_release": lambda x=f"Opção 3": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 4",
                "on_release": lambda x=f"Opção 4": self.set_item1(x),
            }]
        
        menu_items2 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 1",
                "on_release": lambda x=f"Opção 1": self.set_item2(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 2",
                "on_release": lambda x=f"Opção 2": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 3",
                "on_release": lambda x=f"Opção 3": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 4",
                "on_release": lambda x=f"Opção 4": self.set_item2(x),
            }]
        
        menu_items3 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 1",
                "on_release": lambda x=f"Opção 1": self.set_item3(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 2",
                "on_release": lambda x=f"Opção 2": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 3",
                "on_release": lambda x=f"Opção 3": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 4",
                "on_release": lambda x=f"Opção 4": self.set_item3(x),
            }]
        
        menu_items4 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 1",
                "on_release": lambda x=f"Opção 1": self.set_item4(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 2",
                "on_release": lambda x=f"Opção 2": self.set_item4(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 3",
                "on_release": lambda x=f"Opção 3": self.set_item4(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 4",
                "on_release": lambda x=f"Opção 4": self.set_item4(x),
            }]
        
        menu_items5 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 1",
                "on_release": lambda x=f"Opção 1": self.set_item5(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 2",
                "on_release": lambda x=f"Opção 2": self.set_item5(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 3",
                "on_release": lambda x=f"Opção 3": self.set_item5(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Opção 4",
                "on_release": lambda x=f"Opção 4": self.set_item5(x),
            }]

        self.menu1 = MDDropdownMenu(
            caller=self.ids._firstField,
            items=menu_items1,
            position="bottom",
            width_mult=4,
        )

        self.menu2 = MDDropdownMenu(
            caller=self.ids._secondField,
            items=menu_items2,
            position="bottom",
            width_mult=4,
        )

        self.menu3 = MDDropdownMenu(
            caller=self.ids._thirdField,
            items=menu_items3,
            position="bottom",
            width_mult=4,
        )

        self.menu4 = MDDropdownMenu(
            caller=self.ids._fourthField,
            items=menu_items4,
            position="bottom",
            width_mult=4,
        )

        self.menu5 = MDDropdownMenu(
            caller=self.ids._fifthField,
            items=menu_items5,
            position="bottom",
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
    
    def set_item4(self, text__item):
        self.ids._fourthField.text = text__item
        self.menu4.dismiss()
    
    def set_item5(self, text__item):
        self.ids._fifthField.text = text__item
        self.menu5.dismiss()
    
    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen3")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen3")