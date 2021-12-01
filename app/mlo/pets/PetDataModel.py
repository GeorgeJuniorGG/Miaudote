from pydantic.error_wrappers import ValidationError

from mlo.pets.PetDataModelService import PetDataModelService
from mlo.pets.PetModel import (PetModel, PetModelScreen1, PetModelScreen2, PetModelScreen3)

class PetDataModel(PetDataModelService):
    
    def createPetModelScreen1(self, name:str, type:str, color:str, sex:str, size:str)->PetModelScreen1:
        try:
            self.petDataScreen1 = PetModelScreen1(name=name, type=type, color=color, sex=sex, size=size)
            return True
        except ValidationError as e:
            return e.errors()[0]['msg']

    def createPetModelScreen2(self, ambient:str, origin:str, health:str)->PetModelScreen2:
        try:
            self.petDataScreen2 = PetModelScreen2(ambient=ambient, origin=origin, health=health)
            return True
        except ValidationError as e:
            if(e.errors()[0]['msg']=='value is not a valid integer'): 
                return "Alguns campos devem ser preenchidos com números"
            return e.errors()[0]['msg']

    def createPetModelScreen3(self, details:str, Personality:str, Activities:str, Age:str)->PetModelScreen3:
        try:
            self.petDataScreen3 = PetModelScreen3(details=details, Personality=Personality, Activities=Activities, Age=Age)
            return True
        except ValidationError as e:
            return e.errors()[0]['msg']

    def createCompleteModel(self, userData: dict):  
        allData =  {**self.petDataScreen1.dict(),**self.petDataScreen2.dict(),**self.petDataScreen3.dict()}
        allData['localization'] = userData['address']['CEP']
        allData['city'] = userData['address']['city']
        allData['protectorId'] = userData['uid']
        try:
            completeModel = PetModel(**allData)
            return completeModel
        except ValidationError as e:
            return e.errors()[0]['msg']
