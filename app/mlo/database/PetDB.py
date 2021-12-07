from abc import ABC, abstractmethod
from mlo.pets.PetModel import PetModel
from typing import List

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
    def getAllPets(self) -> List[PetModel]:
        pass

    @abstractmethod
    def addPet(self, petData:PetModel)->None:
        pass

    @abstractmethod
    def addPetImages(self, petID, images) -> bool:
        pass

    @abstractmethod
    def insertAR(self, petID:str, arID:str) -> bool:
        pass
    
    @abstractmethod
    def deleteAR(self, petID:str, arID:str) -> bool:
        pass