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
        petsD = []

        for pet in pets:
            petD = pet.dict()
            if (petD["requestStatus"] == False):
                petsD.append(petD)
        #petsD = list(map(lambda p: p.dict(), pets))

        return petsD

    # Obtem os dados de um pet no banco
    def getPetData(self, petID:str) -> dict:
        pet = self.__db.getPetData(petID)

        petD = pet.dict()

        if(petD["requestStatus"] == False):
            return petD
        
        else:
            return {}

    # Atualiza os dados de um pet no banco
    def updatePetData(self, petID:str, pData:dict) -> bool:
        return self.__db.updatePetData(petID, pData)

    def insertAR(self, petID:str, arID:str) -> bool:
        return self.__db.insertAR(petID, arID)

    def deleteAR(self, petID:str, arID:str) -> bool:
        return self.__db.deleteAR(petID, arID)
