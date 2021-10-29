from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
class SignUpScreen4(MDFloatLayout, MDScreen):
    escape_route_dialog = None
    ToS_dialog = None

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
                buttons=[
                    MDFillRoundFlatButton(
                        text="Aceitar", md_bg_color=[0.592, 0.725, 0.752, 1], font_size="20sp",
                    ),
                ],
            )
        self.ToS_dialog.open()
    
    def go_forward(self):
        self.manager.go_forward_signup("SignUpScreen4")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen4")