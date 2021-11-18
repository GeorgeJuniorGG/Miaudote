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
                "text": f"Cachorro(s)",
                "on_release": lambda x=f"Cachorro(s)": self.set_item1(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Gato(s)",
                "on_release": lambda x=f"Gato(s)": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Cachorros(s) e Gato(s)",
                "on_release": lambda x=f"Cachorros(s) e Gato(s)": self.set_item1(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Outros",
                "on_release": lambda x=f"Outros": self.set_item1(x),
            }]
        
        menu_items2 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Cachorro(s)",
                "on_release": lambda x=f"Cachorro(s)": self.set_item2(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Gato(s)",
                "on_release": lambda x=f"Gato(s)": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Cachorros(s) e Gato(s)",
                "on_release": lambda x=f"Cachorros(s) e Gato(s)": self.set_item2(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Outros",
                "on_release": lambda x=f"Outros": self.set_item2(x),
            }]
        
        menu_items3 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Pequeno",
                "on_release": lambda x=f"Pequeno": self.set_item3(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Médio",
                "on_release": lambda x=f"Médio": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Grande",
                "on_release": lambda x=f"Grande": self.set_item3(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Não tenho uma preferência",
                "on_release": lambda x=f"Não tenho uma preferencia": self.set_item3(x),
            }]
        
        menu_items4 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Dócil",
                "on_release": lambda x=f"Dócil": self.set_item4(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Tímido",
                "on_release": lambda x=f"Tímido": self.set_item4(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Bravo",
                "on_release": lambda x=f"Bravo": self.set_item4(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Agitado",
                "on_release": lambda x=f"Agitado": self.set_item4(x),
            }]
        
        menu_items5 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Brincalhão",
                "on_release": lambda x=f"Brincalhão": self.set_item5(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Quieto",
                "on_release": lambda x=f"Quieto": self.set_item5(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Dorminhoco",
                "on_release": lambda x=f"Dorminhoco": self.set_item5(x),
            }]

        menu_items6 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Filhote",
                "on_release": lambda x=f"Filhote": self.set_item6(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Jovem",
                "on_release": lambda x=f"Jovem": self.set_item6(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Adulto",
                "on_release": lambda x=f"Adulto": self.set_item6(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Mais velho",
                "on_release": lambda x=f"Mais velho": self.set_item6(x),
            }]
        
        menu_items7 = [
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Menos de 30 min por dia",
                "on_release": lambda x=f"Menos de 30 min/dia": self.set_item7(x),
            }, 
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"De 30 min a 1 hora por dia",
                "on_release": lambda x=f"De 30 min a 1 hora por dia": self.set_item7(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"De 1 a 2 horas por dia",
                "on_release": lambda x=f"De 1 a 2 horas por dia": self.set_item7(x),
            },
            {
                "viewclass": "OneLineListItem",
                "height": dp(56),
                "text": f"Mais de 2 horas por dia",
                "on_release": lambda x=f"Mais de 2 horas por dia": self.set_item7(x),
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
            width_mult=4,
        )

        self.menu3 = MDDropdownMenu(
            caller=self.ids._thirdField,
            items=menu_items3,
            position="center",
            width_mult=4,
        )

        self.menu4 = MDDropdownMenu(
            caller=self.ids._fourthField,
            items=menu_items4,
            position="center",
            width_mult=4,
        )

        self.menu5 = MDDropdownMenu(
            caller=self.ids._fifthField,
            items=menu_items5,
            position="center",
            width_mult=4,
        )

        self.menu6 = MDDropdownMenu(
            caller=self.ids._sixthField,
            items=menu_items6,
            position="center",
            width_mult=4,
        )
        self.menu7 = MDDropdownMenu(
            caller=self.ids._seventhField,
            items=menu_items7,
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
    
    def set_item4(self, text__item):
        self.ids._fourthField.text = text__item
        self.menu4.dismiss()
    
    def set_item5(self, text__item):
        self.ids._fifthField.text = text__item
        self.menu5.dismiss()

    def set_item6(self, text__item):
        self.ids._sixthField.text = text__item
        self.menu6.dismiss()

    def set_item7(self, text__item):
        self.ids._seventhField.text = text__item
        self.menu7.dismiss()
    
    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen3")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen3")