from mlo.auth.Address import Address
from mlo.auth.basicUserdata import BasicUSerData
from mlo.auth.dataModelService import DataModelService
from mlo.auth.authService import AuthService
from mlo.storage.storageService import StoregeService
from typing import Type

class FakeSignUpManager:
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

    def singUpScreenManager(self, name:str, cpf:int, email:str, password1:str, password2:str, minimumAge:bool, check:bool):
        sUData = {
            'name': name,
            'cpf': cpf,
            'email': email
        }

        userData = self.dataModelService.createUserData(**sUData)
        
        if(type(userData)==BasicUSerData):
            authData = {
                'password1': password1,
                'password2': password2,
                'minimumAge': minimumAge,
                'isProtector': check
            }
            signUp = self.authService.signUp(**authData, userData=userData)
            if(signUp==True): 
                self.currentUser = self.authService.getUserID()
                if(check):
                    #self.signUpScreen.go_forwardB()
                    # self.changeScreen(upf, self.signUpScreen.name)
                    return "changeScreen"
                elif(check):
                    #self.signUpScreen.go_forwardA()
                    # self.changeScreen(usf, self.signUpScreen.name)
                    return 'changeScreen'
            else:
                return signUp
        else:
            return userData

    def singUpScreen2bManager(self, state, city, CEP, neighborhood, address,  number):
        addressData = (
            state,
            city,
            CEP,
            neighborhood,
            address,
            number
        )
        userAddress = self.dataModelService.createAddressData(*addressData)
        if(type(userAddress)==Address):
            if(self.storegeService.storeAddress('protectors',self.currentUser, userAddress)):
                #self.signUpScreen2b.go_forward()
                #self.changeScreen(upf, self.signUpScreen2b.name)
                return "Cadastro realizado com sucesso"
            else:
                return "Erro ao armazenar dados"
        else:
            return userAddress
