from __future__ import annotations
from abc import ABC, abstractmethod
from mlo.auth.Address import Address
from mlo.auth.HomeCharacteristics import HomeCharacteristics
from mlo.auth.Preferences import UserPreferences
from mlo.auth.basicUserdata import BasicUSerData

class DataModelService(ABC):

    @abstractmethod
    def createUserData(self, name:str, cpf:str, email:str)->BasicUSerData:
        pass

    @abstractmethod
    def createAddressData(self, state:str, city:str, CEP:int, neighborhood:str, address:str, number:int)-> Address:
        pass

    @abstractmethod
    def createUserPreferencesData(self, haveAnimal:str, favoriteAnimal:str, favoriteSize:str, characteristics:str, availableTime:str)->UserPreferences:
        pass

    @abstractmethod
    def createHomeCharacteristicsData(self, houseType:str, availableSpace:str, openArea:bool, escapeRoutes:bool, haveChildren:bool)->HomeCharacteristics:
        pass