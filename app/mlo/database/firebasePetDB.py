from .PetDB import PetDB
from config.firebase import getFirebaseFirestore
from mlo.pets.PetModel import PetModel
from typing import List

class FPetDB(PetDB):

    __PET_COLLECTION = u'pets'

    def __init__(self):
        self.__db = getFirebaseFirestore()
        self.__c_ref = self.__db.collection(self.__PET_COLLECTION)

    def getPetData(self, petID: str):
        pet_doc = self.__c_ref.document(petID).get()
        if not pet_doc.exists:
            return None

        petData = pet_doc.to_dict()
        petData['pid'] = petID
        return PetModel(**petData)

    def updatePetData(self, petID: str, pData: dict) -> bool:
        pet_doc_ref = self.__c_ref.document(petID)
        result = None
        result = pet_doc_ref.set(pData)
        if result != None:
            return True
        return False

    # TODO
    # Obter pets que satisfazem a consulta
    def getPets(self, query: dict):
        pass

    # Obter todos os pets do banco
    def getAllPets(self) -> List[PetModel]:
        db_pets = self.__c_ref.stream()
        
        pets: List[PetModel] = list()

        for pet in db_pets:
            pet_dict = pet.to_dict()
            pet_dict['pid'] = pet.id
            pets.append(PetModel(**pet_dict))

        return pets