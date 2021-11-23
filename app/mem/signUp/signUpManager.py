from mlo.auth.Address import Address
from mlo.auth.HomeCharacteristics import HomeCharacteristics
from mlo.auth.Preferences import UserPreferences
from mlo.auth.basicUserdata import BasicUSerData
from mui.signup.SignUpScreen import SignUpScreen
from mui.signup.SignUpScreen2a import SignUpScreen2a
from mui.signup.SignUpScreen2b import SignUpScreen2b
from mui.signup.SignUpScreen3 import SignUpScreen3
from mui.signup.SignUpScreen4 import SignUpScreen4
from kivy.properties import ObjectProperty

from mem.screenmanager.screens import (screens, 
                                       usualProtectorSignUpFlow as upf, 
                                       usualSignUpFlow as usf)

from mlo.auth.dataModelService import DataModelService
from mlo.auth.authService import AuthService
from mlo.storage.storageService import StoregeService
from typing import Type

class SignUpManager:
    authService = Type[AuthService]
    dataModelService = Type[DataModelService]
    storegeService = Type[StoregeService]
    currentUser: str
    manager = None

    def __init__(self, auth:AuthService,
                       dataModel:DataModelService,
                       storage:StoregeService) -> None:
        # Serviços
        self.authService = auth
        self.dataModelService = dataModel
        self.storegeService = storage

        # Screens
        self.signUpScreen=SignUpScreen(name=screens['signUp'])
        self.signUpScreen.controller = self
        self.signUpScreen2a=SignUpScreen2a(name=f"{screens['signUp']}2a")
        self.signUpScreen2a.controller = self
        self.signUpScreen2b=SignUpScreen2b(name=f"{screens['signUp']}2b")
        self.signUpScreen2b.controller = self
        self.signUpScreen3=SignUpScreen3(name=f"{screens['signUp']}3")
        self.signUpScreen3.controller = self
        self.signUpScreen4=SignUpScreen4(name=f"{screens['signUp']}4")
        self.signUpScreen4.controller = self

    def addScreens(self):
        self.manager.add_widget(self.signUpScreen)
        self.manager.add_widget(self.signUpScreen2a)
        self.manager.add_widget(self.signUpScreen2b)
        self.manager.add_widget(self.signUpScreen3)
        self.manager.add_widget(self.signUpScreen4)

    def changeScreen(self, flow:list, sName:str, dir:int=1):
        direction = 'left'
        if dir == -1:
            direction = 'right'

        index = flow.index(sName)
        nextScreen = flow[index+dir]
        self.manager.changeScreen(direction, nextScreen)

    def backward(self, sName, fHint:str='adopt'):
        flow = usf
        if fHint != 'adopt':
            flow = upf
        
        self.changeScreen(flow, sName, dir=-1)

    def singUpScreenManager(self):
        sUData = {
            'name': self.signUpScreen.ids.name.text,
            'cpf': self.signUpScreen.ids.cpf.text,
            'email': self.signUpScreen.ids.email.text
        }

        userData = self.dataModelService.createUserData(**sUData)
        
        if(type(userData)==BasicUSerData):
            authData = {
                'password1': self.signUpScreen.ids.password1.text,
                'password2': self.signUpScreen.ids.password2.text,
                'minimumAge': self.signUpScreen.ids.minimumAge.active,
                'isProtector': self.signUpScreen.ids._check.active,
            }
            signUp = self.authService.signUp(**authData, userData=userData)
            if(signUp==True):
                self.currentUser = self.authService.getUserID()
                if(self.signUpScreen.ids._check.active):
                    #self.signUpScreen.go_forwardB()
                    self.changeScreen(upf, self.signUpScreen.name)
                elif(not self.signUpScreen.ids._check.active):
                    #self.signUpScreen.go_forwardA()
                    self.changeScreen(usf, self.signUpScreen.name)
            else:
                print(signUp)
        else:
            print(userData)

        
    def singUpScreen2aManager(self):
        addressData = (
            self.signUpScreen2a.ids.state.text,
            self.signUpScreen2a.ids.city.text,
            self.signUpScreen2a.ids.CEP.text,
            self.signUpScreen2a.ids.neighborhood.text,
            self.signUpScreen2a.ids.address.text,
            self.signUpScreen2a.ids.number.text
        )
        userAddress = self.dataModelService.createAddressData(*addressData)
        if(type(userAddress)==Address):
            if(self.storegeService.storeAddress('adopters',self.currentUser, userAddress)):
                #self.signUpScreen2a.go_forward()
                self.changeScreen(usf, self.signUpScreen2a.name)
            else:
                print('Erro ao armazenar dados')
        else:
            print(userAddress)

    def singUpScreen2bManager(self):
        addressData = (
            self.signUpScreen2b.ids.state.text,
            self.signUpScreen2b.ids.city.text,
            self.signUpScreen2b.ids.CEP.text,
            self.signUpScreen2b.ids.neighborhood.text,
            self.signUpScreen2b.ids.address.text,
            self.signUpScreen2b.ids.number.text
        )
        userAddress = self.dataModelService.createAddressData(*addressData)
        if(type(userAddress)==Address):
            if(self.storegeService.storeAddress('protectors', self.currentUser, userAddress)):
                if(self.signUpScreen2b.ids._ToSCheck.active):
                    #self.signUpScreen2b.go_forward()
                    self.changeScreen(upf, self.signUpScreen2b.name)
                else:
                    self.signUpScreen2b.show_terms_of_service_dialog()
            else:
                print('Erro ao armazenar dados')
        else:
            print(userAddress)

    def singUpScreen3Manager(self):
        prefData = (
            self.signUpScreen3.ids._firstField.text,
            self.signUpScreen3.ids._secondField.text,
            self.signUpScreen3.ids._thirdField.text,
            self.signUpScreen3.ids._fourthField.text,
            self.signUpScreen3.ids._fifthField.text,
            self.signUpScreen3.ids._sixthField.text,
            self.signUpScreen3.ids._seventhField.text
        )
        userPreferences =  self.dataModelService.createUserPreferencesData(*prefData)
        if(type(userPreferences)==UserPreferences):
            if(self.storegeService.storePreferences(self.currentUser, userPreferences)):
                #self.signUpScreen3.go_forward()
                self.changeScreen(usf, self.signUpScreen3.name)
            else:
                print('Erro ao armazenar dados')
        else:
            print(userPreferences)

    def singUpScreen4Manager(self):
        homeData = (
            self.signUpScreen4.ids._firstField.text,
            self.signUpScreen4.ids._secondField.text,
            self.signUpScreen4.ids.ambiente.active,
            self.signUpScreen4.ids.rotas.active,
            self.signUpScreen4.ids.criancas.active
        )
        userHomeCharacteristics = self.dataModelService.createHomeCharacteristicsData(*homeData)
        if(type(userHomeCharacteristics)==HomeCharacteristics): 
            if(self.storegeService.storeHomeCharacteristics(self.currentUser, userHomeCharacteristics)):
                if(self.signUpScreen4.ids._ToSCheck.active):
                    #self.signUpScreen4.go_forward()
                    self.changeScreen(usf, self.signUpScreen4.name)
                else:
                    self.signUpScreen4.show_terms_of_service_dialog()
            else:
                print('Erro ao armazenar dados')
        else:
            print(userHomeCharacteristics)    