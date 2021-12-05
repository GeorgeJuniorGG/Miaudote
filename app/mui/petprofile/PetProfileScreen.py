from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.fitimage import FitImage
from kivymd.toast import toast

from kivy.utils import get_color_from_hex

from mui.ColorTheme import Color

class PetProfileScreen(MDScreen):
    def __init__(self, petData:dict, **kw):
        super().__init__(**kw)

        self.cor = Color()
        self.controller = None

        self.petName = petData['name']
        self.petSex = petData['sex']
        self.petAge = petData['Age']
        self.petAddr = str(petData['city']+", "+petData['state'])
        self.petDscp = petData['details']
        self.petImages = petData['images']
        self.petID = petData['pid']
        self.addPetImages()
    
    def addPetImages(self):
        for image in self.petImages:
            currentImage = FitImage(source = image)
            self.ids.carousel.add_widget(currentImage)

    def start_favorite_state(self, status):
        if status == False:
            self.petFav = "heart-outline"
        else:
            self.petFav = "heart-remove-outline"

    def change_favorite_state(self):
        if self.petFav == "heart-outline":
            self.petFav = "heart-remove-outline"
            self.controller.addFavorite(self.petID)
        else:
            self.petFav= "heart-outline"
            self.controller.removeFavorite(self.petID)

    def alert(self):
        print("DENÚNCIA!")

    def adopt_dialog(self):
        sim_btn = MDFillRoundFlatButton(text="SIM", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.azulEscuro()),
                                        on_release=self.go_forward)

        nao_btn = MDFillRoundFlatButton(text="NÃO", theme_text_color="Custom",
                                        text_color=get_color_from_hex(self.cor.branco()),
                                        md_bg_color=get_color_from_hex(self.cor.vermelho()),
                                        on_release=self.close_dialog)

        msg = "Você tem certeza que deseja enviar a solicitação de adoção?"

        self.dialog = MDDialog(text="[color=#ffffff]" + str(msg) + "[/color]",
                               md_bg_color=get_color_from_hex(self.cor.azulClaro()),
                               size_hint=(0.7, 1), radius=[20,20,20,20],
                               buttons=[sim_btn, nao_btn])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()        

    def go_forward(self, obj):
        self.dialog.dismiss()
        self.controller.addRequest(self.petID)

    def go_backwards(self):
        pass

    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))

    def screenToProtector(self):
        self.ids.pet_bar.remove_widget(self.ids.pet_fav)   
        self.ids.body.remove_widget(self.ids.pet_adopt)
