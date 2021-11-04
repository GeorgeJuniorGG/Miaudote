from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty

class SignUpScreen4(MDFloatLayout, MDScreen):
    controller = ObjectProperty()
    escape_route_dialog = None
    ToS_dialog = None

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
    
    def set_item1(self, text__item):
        self.ids._firstField.text = text__item
        self.menu1.dismiss()
    
    def set_item2(self, text__item):
        self.ids._secondField.text = text__item
        self.menu2.dismiss()

    def show_escape_routes_dialog(self):
        if not self.escape_route_dialog:
            self.escape_route_dialog = MDDialog(
                title="Rotas de Fuga",
                text="Marque essa opção se o espaço reservado para o seu futuro pet possui brechas que facilitem a sua fuga.\n(Melhorar texto)",
            )
        self.escape_route_dialog.open()
    
    def show_terms_of_service_dialog(self):
        if not self.ToS_dialog:
            self.ToS_dialog = MDDialog(
                title="Termos de Uso",
                type="custom",
                text="Lorem ipsum dolor sit amet. Qui illo illum qui quia ullam est mollitia illum est totam laudantium ab quia quia sed enim atque ut ratione explicabo. Sit galisum dicta qui possimus assumenda rem aspernatur explicabo.",
            )
        self.ToS_dialog.open()
    
    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen4")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen4")