from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.utils.fitimage import FitImage
from kivymd.toast import toast

from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

from mui.ColorTheme import Color

class PetSignUpScreen4(MDFloatLayout, MDScreen):
    cor = Color()
    controller = ObjectProperty()
    files:list = list()

    def addPetImage(self, image):
        self.files.append(image)
        currentImage = FitImage(source = image)
        self.ids.container.add_widget(currentImage)

    def go_backward(self):
        self.controller.backward(self.name)

    def go_forward(self):
        self.controller.petSignUpScreen4Manager()
    
    def showToast(self, msg:str):
        toast(msg, get_color_from_hex(self.cor.azulCinzaClaro()+'F0'))