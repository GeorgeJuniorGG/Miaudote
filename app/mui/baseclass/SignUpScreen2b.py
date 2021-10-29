from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
class SignUpScreen2b(MDFloatLayout, MDScreen):
    ToS_dialog = None

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