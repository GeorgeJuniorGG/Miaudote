from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.utils.fitimage import FitImage

class PetSignUpScreen4(MDFloatLayout, MDScreen):
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