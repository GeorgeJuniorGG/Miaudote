from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.utils import get_color_from_hex

from mui.ColorTheme import Color

class PetProfileScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.cor = Color()

        self.petName = "nome"
        self.petSex = "sexo"
        self.petAge = "0"
        self.petAddr = "Campinas/SP"
        self.petDscp = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce non semper lacus, quis dapibus eros."

        fav = 1

        if(fav == 0):
            self.petFav = "heart-outline"
        else:
            self.petFav = "heart-remove-outline"

    def change_favorite_state(self):
        self.petFav = "heart-remove-outline" if self.petFav == "heart-outline" else "heart-outline"

        print("FAVORITO " + str(self.petFav))

    def alert(self):
        print("DENÚNCIA!")

    def adopt_dialog(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.azulEscuro()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.go_forward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.vermelho()),
                                        md_bg_color=get_color_from_hex(self.cor.branco()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja enviar a solicitação de adoção?"

        self.dialog = MDDialog(text="[color=get_color_from_hex(self.cor.branco())]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()        

    def go_forward(self, obj):
        self.dialog.dismiss()
        pass

    def go_backwards(self):
        pass