from __future__ import annotations
from abc import ABC, abstractmethod
from mlo.auth.basicUserdata import BasicUSerData
from mlo.auth.Address import Address
from mlo.auth.Preferences import UserPreferences
from mlo.auth.HomeCharacteristics import HomeCharacteristics


class StoregeService(ABC):

    @abstractmethod
    def createProtector(currentUser:str, userData:BasicUSerData)->None:
        pass

    @abstractmethod
    def createAdopter(currentUser:str, userData:BasicUSerData)->None:
        pass

    @abstractmethod
    def storeAddress(self, collection:str, currentUser:str, userAddress: Address)->bool:
        pass

    @abstractmethod
    def storePreferences(self, currentUser:str, userPreferences:UserPreferences)->bool:
        pass

    @abstractmethod
    def storeHomeCharacteristics(self, currentUser:str, userHomeCharacteristics: HomeCharacteristics)->bool:
        pass