from abc import ABC, abstractmethod
from mlo.pets.PetModel import PetModel

class PetDB(ABC):

    @abstractmethod
    def getPetData(self, petID: str) -> PetModel:
        pass

    @abstractmethod
    def updatePetData(self, petID: str, pData:dict) -> bool:
        pass

    @abstractmethod
    def getPets(self, query:dict):
        pass

    @abstractmethod
    def getAllPets(self) -> list[PetModel]:
        pass