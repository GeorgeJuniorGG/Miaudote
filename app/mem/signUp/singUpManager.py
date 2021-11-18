from mui.signup.SignUpScreen import SignUpScreen
from mui.signup.SignUpScreen2a import SignUpScreen2a
from mui.signup.SignUpScreen2b import SignUpScreen2b
from mui.signup.SignUpScreen3 import SignUpScreen3
from mui.signup.SignUpScreen4 import SignUpScreen4
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.storage.firebaseDB import FirebaseDB
from mlo.auth.dataModel import DataModel
from mlo.auth.dataModelService import DataModelService
from mlo.auth.authService import AuthService
from mlo.storage.storageService import StoregeService
from typing import Type

class SignUpManager:
    authService = Type[AuthService]
    dataModelService = Type[DataModelService]
    storegeService = Type[StoregeService]
    controller = ObjectProperty()
    currentUser: str

    def __init__(self, signUpScreen:SignUpScreen, signUpScreen2a:SignUpScreen2a, signUpScreen2b:SignUpScreen2b, signUpScreen3:SignUpScreen3, signUpScreen4:SignUpScreen4, manage:ScreenManager):
        self.signUpScreen=signUpScreen
        self.signUpScreen.controller = self
        self.signUpScreen2a=signUpScreen2a
        self.signUpScreen2a.controller = self
        self.signUpScreen2b=signUpScreen2b
        self.signUpScreen2b.controller = self
        self.signUpScreen3=signUpScreen3
        self.signUpScreen3.controller = self
        self.signUpScreen4=signUpScreen4
        self.signUpScreen4.controller = self
        self.manager = manage

        self.dataModelService = DataModel()
        self.authService = FireBaseAuthService()
        self.storegeService =FirebaseDB()

        
    def singUpScreenManager(self):
        userData = self.dataModelService.createUserData(self.signUpScreen.ids.name.text,self.signUpScreen.ids.cpf.text,self.signUpScreen.ids.email.text)
        if(userData):
            self.currentUser = self.authService.signUp(self.signUpScreen.ids.password1.text,self.signUpScreen.ids.password2.text, self.signUpScreen.ids.minimumAge.active,self.signUpScreen.ids._check.active, userData)
            if(self.signUpScreen.ids._check.active and  self.currentUser):
                self.signUpScreen.go_forwardB()
            elif(not self.signUpScreen.ids._check.active and self.currentUser):
                self.signUpScreen.go_forwardA()
            else:
                print("Algo deu errado durante o cadastro")
        else:
            print("Preencha os campos corretamente")

        
    def singUpScreen2aManager(self):
        userAddress = self.dataModelService.createAddressData(self.signUpScreen2a.ids.state.text, self.signUpScreen2a.ids.city.text, self.signUpScreen2a.ids.CEP.text, self.signUpScreen2a.ids.neighborhood.text, self.signUpScreen2a.ids.address.text, self.signUpScreen2a.ids.number.text)
        if(userAddress and self.storegeService.storeAddress('adopters',self.currentUser, userAddress)):
            self.signUpScreen2a.go_forward()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen2bManager(self):
        userAddress = self.dataModelService.createAddressData(self.signUpScreen2b.ids.state.text, self.signUpScreen2b.ids.city.text, self.signUpScreen2b.ids.CEP.text, self.signUpScreen2b.ids.neighborhood.text, self.signUpScreen2b.ids.address.text, self.signUpScreen2b.ids.number.text)
        if(userAddress and self.storegeService.storeAddress('protectors', self.currentUser, userAddress)):
            if(self.signUpScreen2b.ids._ToSCheck.active):
                self.signUpScreen2b.go_forward()
            else:
                self.signUpScreen2b.show_terms_of_service_dialog()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen3Manager(self):
        userPreferences =  self.dataModelService.createUserPreferencesData(self.signUpScreen3.ids._firstField.text, self.signUpScreen3.ids._secondField.text, self.signUpScreen3.ids._thirdField.text, self.signUpScreen3.ids._fourthField.text, self.signUpScreen3.ids._fifthField.text)
        if(userPreferences and self.storegeService.storePreferences(self.currentUser, userPreferences)):
            self.signUpScreen3.go_forward()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen4Manager(self):
        userHomeCharacteristics = self.dataModelService.createHomeCharacteristicsData(self.signUpScreen4.ids._firstField.text, self.signUpScreen4.ids._secondField.text, self.signUpScreen4.ids.ambiente.active, self.signUpScreen4.ids.rotas.active, self.signUpScreen4.ids.criancas.active)
        if(userHomeCharacteristics and self.storegeService.storeHomeCharacteristics(self.currentUser, userHomeCharacteristics)):
            if(self.signUpScreen4.ids._ToSCheck.active):
                self.signUpScreen4.go_forward()
            else:
                self.signUpScreen4.show_terms_of_service_dialog()
        else:
            print("Preencha os campos corretamente")