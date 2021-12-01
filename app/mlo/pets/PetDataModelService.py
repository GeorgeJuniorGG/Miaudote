from __future__ import annotations
from abc import ABC, abstractmethod
from mlo.pets.PetModel import (PetModel, PetModelScreen1, PetModelScreen2, PetModelScreen3)

class PetDataModelService(ABC):

    @abstractmethod
    def createPetModelScreen1(self, name:str, type:str, color:str, sex:str, size:str)->PetModelScreen1:
        pass

    @abstractmethod
    def createPetModelScreen2(self, ambient:str, origin:str, health:str, localization:int)-> PetModelScreen2:
        pass

    @abstractmethod
    def createPetModelScreen3(self, details:str, Personality:str, Activities:str, Age:str)->PetModelScreen3:
        pass

    @abstractmethod
    def createCompleteModel(self):
        pass
