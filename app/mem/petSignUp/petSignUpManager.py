from kivy.properties import ObjectProperty

from mui.petprofile.PetSignUpScreen import PetSignUpScreen
from mui.petprofile.PetSignUpScreen2 import PetSignUpScreen2
from mui.petprofile.PetSignUpScreen3 import PetSignUpScreen3
from mui.petprofile.PetSignUpScreen4 import PetSignUpScreen4

from mem.filechooser.FMClient import FMClient
from mem.screenmanager.screens import (screens, 
                                       usualPetSignUpFlow as upsf)

from mlo.pets.PetModel import PetModel

from mlo.database.PetDB import PetDB
from mlo.pets.PetDataModelService import PetDataModelService
from mlo.user.UserService import UserService
from typing import Type

class PetSignUpManager(FMClient):

    petStoregeService = Type[PetDB]
    petDataModelService = Type[PetDataModelService]
    userService = Type[UserService]
    currentUser: str
    manager = None
    petID: str

    def __init__(self, storage:PetDB, petDataModel:PetDataModelService, user=UserService) -> None:
        # Serviços
        self.petStoregeService = storage
        self.petDataModelService = petDataModel
        self.userService = user

        # Screens
        self.petSignUpScreen=PetSignUpScreen(name=screens['petSignUp'])
        self.petSignUpScreen.controller = self
        self.petSignUpScreen2=PetSignUpScreen2(name=f"{screens['petSignUp']}2")
        self.petSignUpScreen2.controller = self
        self.petSignUpScreen3=PetSignUpScreen3(name=f"{screens['petSignUp']}3")
        self.petSignUpScreen3.controller = self
        self.petSignUpScreen4=PetSignUpScreen4(name=f"{screens['petSignUp']}4")
        self.petSignUpScreen4.controller = self

        # File Manager
        self.__FM = None
        self.__CP = "/"

    def addScreens(self):
        self.manager.add_widget(self.petSignUpScreen)
        self.manager.add_widget(self.petSignUpScreen2)
        self.manager.add_widget(self.petSignUpScreen3)
        self.manager.add_widget(self.petSignUpScreen4)


    def changeScreen(self, flow:list, sName:str, dir:int=1):
        direction = 'left'
        if dir == -1:
            direction = 'right'

        index = flow.index(sName)
        nextScreen = flow[index+dir]
        
        if dir == -1 and sName == self.petSignUpScreen.name:
            self.clearScreen()
        
        self.manager.changeScreen(direction, nextScreen)

    def backward(self, sName):
        flow = upsf
        self.changeScreen(flow, sName, dir=-1)

    def petSignUpScreenManager(self):
        petScreen1Data = {
            'name': self.petSignUpScreen.ids.name.text,
            'type': (self.petSignUpScreen.ids.type.text).lower(),
            'color': (self.petSignUpScreen.ids.color.text).lower(),
            'sex': (self.petSignUpScreen.ids.sex.text).lower(),
            'size': (self.petSignUpScreen.ids.size.text).lower(),
        }
        dataPetScreen1 = self.petDataModelService.createPetModelScreen1(**petScreen1Data)
        if(dataPetScreen1==True):
            self.changeScreen(upsf, self.petSignUpScreen.name)
        else:
            self.petSignUpScreen.showToast(dataPetScreen1)
        
    def petSignUpScreen2Manager(self):
        petScreen2Data = {
            'ambient': (self.petSignUpScreen2.ids.ambient.text).lower(),
            'origin': (self.petSignUpScreen2.ids.origin.text).lower(),
            'health': (self.petSignUpScreen2.ids.health.text).lower(),
        }
        dataPetScreen2 = self.petDataModelService.createPetModelScreen2(**petScreen2Data)
        if(dataPetScreen2==True):
            self.changeScreen(upsf, self.petSignUpScreen2.name)
        else:
            self.petSignUpScreen2.showToast(dataPetScreen2)

    def petSignUpScreen3Manager(self):
        petScreen3Data = {
            'details': self.petSignUpScreen3.ids.details.text,
            'Personality': self.petSignUpScreen3.ids._firstField.text,
            'Activities': self.petSignUpScreen3.ids._secondField.text,
            'Age': self.petSignUpScreen3.ids._thirdField.text,
        }
        dataPetScreen3 = self.petDataModelService.createPetModelScreen3(**petScreen3Data)
        if(dataPetScreen3==True):
            completeData = self.petDataModelService.createCompleteModel(self.userService.getUserData())
            if(type(completeData)==PetModel):
                self.petID = self.petStoregeService.addPet(completeData)
                self.userService.addPetId(self.petID)
                self.changeScreen(upsf, self.petSignUpScreen3.name)
            else:
                self.petSignUpScreen3.showToast(completeData)
        else:
            self.petSignUpScreen3.showToast(dataPetScreen3)
               

    def petSignUpScreen4Manager(self):
        pathImages = self.petSignUpScreen4.files
        if(self.petStoregeService.addPetImages(self.petID, pathImages)):
            self.changeScreen(upsf, self.petSignUpScreen4.name)
            self.clearScreen()
        else:
            self.petSignUpScreen4.showToast("Houve um erro ao adicionar as imagens")    

    def clearScreen(self):
        self.manager.remove_widget(self.petSignUpScreen)
        self.manager.remove_widget(self.petSignUpScreen2)
        self.manager.remove_widget(self.petSignUpScreen3)
        self.manager.remove_widget(self.petSignUpScreen4)

    # File Manager
    def registreFM(self, FM):
        self.__FM = FM

    def callFileManager(self):
        self.manager.orchestrator.openFileManager(self)

    def getCurrentPath(self) -> str:
        return self.__CP

    def receiveFile(self, file: str, path: str):
        self.__CP = path
        orchestrator = self.manager.orchestrator

        if file != None:
            self.petSignUpScreen4.addPetImage(file)

        orchestrator.callGoBackward(self.petSignUpScreen4.name)

