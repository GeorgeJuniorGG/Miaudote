from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.properties import ObjectProperty

class SignUpScreen2b(MDFloatLayout, MDScreen):
    ToS_dialog = None
    controller = ObjectProperty()

    def show_terms_of_service_dialog(self):
        if not self.ToS_dialog:
            self.ToS_dialog = MDDialog(
                title="Termos de Uso",
                type="custom",
                text="Lorem ipsum dolor sit amet. Qui illo illum qui quia ullam est mollitia illum est totam laudantium ab quia quia sed enim atque ut ratione explicabo. Sit galisum dicta qui possimus assumenda rem aspernatur explicabo.",
            )
        self.ToS_dialog.open()
    
    def go_forward(self):
        self.manager.go_forward_protector_signup("SignUpScreen2b")

    def go_backward(self):
        #self.manager.go_backward_protector_signup("SignUpScreen2b")
        self.controller.backward(self.name, fHint='protc')