from mlo.database.PetDB import PetDB
from mlo.pets.PetModel import PetModel
from typing import List

class PetService:

    def __init__(self, db:PetDB) -> None:
        self.__db = db

    # Obtem todos os pets no banco
    def getAllPets(self) -> List[dict]:
        pets: List[PetModel]
        pets = self.__db.getAllPets()
        petsD = list(map(lambda p: p.dict(), pets))

        return petsD

    # Obtem os dados de um pet no banco
    def getPetData(self, petID:str) -> dict:
        pet = self.__db.getPetData(petID)
        return pet.dict()

    # Atualiza os dados de um pet no banco
    def updatePetData(self, petID:str, pData:dict) -> bool:
        return self.__db.updatePetData(petID, pData)