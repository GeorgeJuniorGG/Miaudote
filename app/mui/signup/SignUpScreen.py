from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

class SignUpScreen(MDFloatLayout, MDScreen):
    controller = ObjectProperty()
    dialog = None

    def show_protectors_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Protetores",
                text="Protetores são pessoas com bom coração que cuidam de animais até eles encotrarem uma lar.\n\nMarque essa opção se você tem interesse em divulgar animais para serem adotados.",
            )
        self.dialog.open()
    
    # def createProtectorUser(self,name,birthDate,CPF,email,password1,password2):
    #     currentUser = self.authService.signUp(email,password1,password2)
    #     if(currentUser):
    #         createProtector(currentUser,name, birthDate, CPF)

    def go_forwardA(self):
        self.manager.go_forward_signup("SignUpScreen")
    
    def go_forwardB(self):
        self.manager.go_forward_protector_signup("SignUpScreen")

    def go_backward(self):
        self.manager.go_backward_signup("SignUpScreen")