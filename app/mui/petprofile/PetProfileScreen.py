from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.utils.fitimage import FitImage

from mui.ColorTheme import Color

class PetProfileScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.cor = Color()

        self.petName = "nome"
        self.petSex = "sexo"
        self.petAge = "0"
        self.petAddr = "Campinas/SP"
        self.petDscp = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        self.petImages = ['https://firebasestorage.googleapis.com/v0/b/miaudote-b4e55.appspot.com/o/petImages%2F4prTZhzu71iQaGpCo1bE%2Fgarfield1.jpeg?alt=media&token=c4c4c354-5200-43fe-a8da-5811c8e79f07','https://firebasestorage.googleapis.com/v0/b/miaudote-b4e55.appspot.com/o/petImages%2F4prTZhzu71iQaGpCo1bE%2Fgarfield2.jpg?alt=media&token=000bfeb7-64ab-49b4-8c51-e0ffc6ab9d57','https://firebasestorage.googleapis.com/v0/b/miaudote-b4e55.appspot.com/o/petImages%2F4prTZhzu71iQaGpCo1bE%2Fgarfield3.jpg?alt=media&token=661aa04f-266f-4af9-bc7c-d6348c222ff5']

        fav = 1
        self.addPetImagens()
        if(fav == 0):
            self.petFav = "heart-outline"
        else:
            self.petFav = "heart-remove-outline"

    def favourite(self):
        print("FAVORITO " + str(self.petFav))

    def alert(self):
        print("DENÚNCIA!")

    def adopt_popup(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=self.cor.textoL(),
                                        md_bg_color="#ffffff",
                                        on_release=self.go_foward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=self.cor.rgaVermelho(),
                                        md_bg_color="#ffffff",
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja enviar a solicitação?"

        self.dialog = MDDialog(text="[color=#ffffff]" + str(msg) + "[/color]",
                               md_bg_color=self.cor.fundoB(),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()        

    def go_foward(self, obj):
        self.dialog.dismiss()
        pass

    def go_backwards(self):
        pass

    def addPetImagens(self):
        for image in self.petImages:
            currentImage = FitImage(source = image)
            self.ids.carousel.add_widget(currentImage)
