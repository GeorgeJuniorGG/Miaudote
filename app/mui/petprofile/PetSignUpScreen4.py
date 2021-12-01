from logging import addLevelName
from re import A
from typing import List
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.utils.fitimage import FitImage

class PetSignUpScreen4(MDFloatLayout, MDScreen):
    controller = ObjectProperty()
    files = []

    def __init__(self, **kw):
        super().__init__(**kw)
        self.imgTypes = ('png', 'jpg', 'jpeg')
        self.fileManager = MDFileManager(
            exit_manager=self.exitManager,
            select_path=self.selectPath,
            preview=True,    
            selector="multi" 
        )

    def fileManagerOpen(self):
        self.fileManager.show('/')
        self.manager_open = True

    def selectPath(self, paths):
        self.fileManager.select_path
        for path in paths:
            valid = False  
            for type in self.imgTypes:
                if type in path:
                    valid = True
            if not valid:
                toast("Arquivo não suportado")
                self.exitManager()
                return
        self.addPetImagens(paths)
        self.exitManager()

    def addPetImagens(self, paths):
        self.files = paths
        for image in paths:
            currentImage = FitImage(source = image)
            self.ids.container.add_widget(currentImage)

    def exitManager(self, *args):
        self.manager_open = False
        self.fileManager.close()

    def go_backward(self):
        self.manager.go_backward_pet_signup("PetSignUpScreen3")
        self.controller.backward(self.name)

    def go_forward(self):
        self.manager.go_forward_pet_signup("PetSignUpScreen4")