from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.utils import get_color_from_hex

from mui.ColorTheme import Color

class ProfileScreen(MDScreen):
    cor = Color()
    controller = None

    # Adicionar as Informações do Usuário na tela de perfil
    def getUserData(self):
        userData = self.controller.getUserData()

        for itemName in self.ids:
            item = self.ids[itemName]
            if itemName == 'userImage':
                item.source = userData['userImage']
            elif itemName in userData.keys():
                item.fieldValue = userData[itemName]

    def changeUserImage(self, imagePath):
        oldImage = self.ids['userImage'].source
        self.ids['userImage'].source = imagePath
        return oldImage

    def logout_dialog(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.azulEscuro()),
                                        on_release=self.go_forward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.vermelho()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja deslogar?"

        self.dialog = MDDialog(text="[color=#ffffff]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()        

    def go_forward(self, obj):
        self.dialog.dismiss()
        self.controller.logout()