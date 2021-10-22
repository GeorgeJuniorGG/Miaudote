from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog

class SignUpScreen(MDFloatLayout, MDScreen):
    dialog = None

    def show_protectors_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Protetores",
                text="Protetores são pessoas com bom coração que cuidam de animais até eles encotrarem uma lar.\n\nMarque essa opção se você tem interesse em divulgar animais para serem adotados.",
            )
        self.dialog.open()