from mui.signup.SignUpScreen import SignUpScreen
from mui.signup.SignUpScreen2a import SignUpScreen2a
from mui.signup.SignUpScreen2b import SignUpScreen2b
from mui.signup.SignUpScreen3 import SignUpScreen3
from mui.signup.SignUpScreen4 import SignUpScreen4
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from mlo.services.firebaseAuth import FireBaseAuthService
from mlo.services.firebaseDB import (createProtector,createAdopter, storeAddress, storeHomeCharacteristics, storePreferences)

class SignUpManager:
    authService = FireBaseAuthService()
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
        
    def singUpScreenManager(self):
        if(not self.signUpScreen.ids.name.text or not self.signUpScreen.ids.birthDate.text or not self.signUpScreen.ids.CPF.text.isdigit() or not self.signUpScreen.ids.email.text or not self.signUpScreen.ids.password1.text or not self.signUpScreen.ids.password2.text):
            print("Preencha os campos corretamente")
        elif(self.signUpScreen.ids.password1.text != self.signUpScreen.ids.password2.text):
            print("As senhas inseridas são diferentes")
        elif(not "@" in self.signUpScreen.ids.email.text or not ".com" in self.signUpScreen.ids.email.text):
            print("Email inválido")
        else:
            self.currentUser = self.authService.signUp(self.signUpScreen.ids.email.text,self.signUpScreen.ids.password1.text,self.signUpScreen.ids.password2.text)
            if(self.signUpScreen.ids._check.active and self.currentUser):
                createProtector(self.currentUser,self.signUpScreen.ids.name.text, self.signUpScreen.ids.birthDate.text, self.signUpScreen.ids.CPF.text)
                self.signUpScreen.go_forwardB()
            elif(not self.signUpScreen.ids._check.active and self.currentUser):
                createAdopter(self.currentUser,self.signUpScreen.ids.name.text, self.signUpScreen.ids.birthDate.text, self.signUpScreen.ids.CPF.text)
                self.signUpScreen.go_forwardA()
            else:
                print("Algo deu errado durante o cadastro")
        
    def singUpScreen2aManager(self):
        if(storeAddress('adopters',self.currentUser, self.signUpScreen2a.ids.state.text, self.signUpScreen2a.ids.city.text, self.signUpScreen2a.ids.CEP.text, self.signUpScreen2a.ids.neighborhood.text, self.signUpScreen2a.ids.address.text, self.signUpScreen2a.ids.number.text)):
            self.signUpScreen2a.go_forward()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen2bManager(self):
        if(storeAddress('protectors', self.currentUser, self.signUpScreen2b.ids.state.text, self.signUpScreen2b.ids.city.text, self.signUpScreen2b.ids.CEP.text, self.signUpScreen2b.ids.neighborhood.text, self.signUpScreen2b.ids.address.text, self.signUpScreen2b.ids.number.text)):
            if(self.signUpScreen2b.ids._ToSCheck.active):
                self.signUpScreen2b.go_forward()
            else:
                self.signUpScreen2b.show_terms_of_service_dialog()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen3Manager(self):
        if(storePreferences(self.currentUser, self.signUpScreen3.ids._firstField.text, self.signUpScreen3.ids._secondField.text, self.signUpScreen3.ids._thirdField.text, self.signUpScreen3.ids._fourthField.text, self.signUpScreen3.ids._fifthField.text)):
            self.signUpScreen3.go_forward()
        else:
            print("Preencha os campos corretamente")

    def singUpScreen4Manager(self):
        if(storeHomeCharacteristics(self.currentUser, self.signUpScreen4.ids._firstField.text, self.signUpScreen4.ids._secondField.text, self.signUpScreen4.ids.ambiente.active, self.signUpScreen4.ids.rotas.active, self.signUpScreen4.ids.criancas.active)):
            if(self.signUpScreen4.ids._ToSCheck.active):
                self.signUpScreen4.go_forward()
            else:
                self.signUpScreen4.show_terms_of_service_dialog()
        else:
            print("Preencha os campos corretamente")