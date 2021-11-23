from pydantic.error_wrappers import ValidationError
from .dataModelService import DataModelService
from .Address import Address
from .HomeCharacteristics import HomeCharacteristics
from .Preferences import UserPreferences
from .basicUserdata import BasicUSerData

class DataModel(DataModelService):
    
    def createUserData(self, name:str, cpf:int, email:str):
        userData=False
        try:
            userData = BasicUSerData(name=name, cpf=cpf, email=email)
            return userData
        except ValidationError as e:
            if(e.errors()[0]['msg']=='value is not a valid integer'): 
                return "Alguns campos devem ser preenchidos com números"
            elif(e.errors()[0]['msg'] =='value is not a valid email address'): 
                return "Preencha um email válido"
            return e.errors()[0]['msg']

    def createAddressData(self, state:str, city:str, CEP:int, neighborhood:str, address:str, number:int):
        userAddress = False
        try:
            userAddress = Address(state=state, city=city, CEP=CEP, neighborhood=neighborhood, address=address, number=number)
            return userAddress
        except ValidationError as e:
            if(e.errors()[0]['msg']=='value is not a valid integer'): 
                return "Alguns campos devem ser preenchidos com números"
            return e.errors()[0]['msg']

    def createUserPreferencesData(self, haveAnimal:str, favoriteAnimal:str, favoriteSize:str, personalityCharacteristics: str, activitiesCharacteristics: str, ageCharacteristics: str, availableTime:str)->UserPreferences:
        userPreferences = False
        try:
            userPreferences = UserPreferences(haveAnimal=haveAnimal, favoriteAnimal=favoriteAnimal, favoriteSize=favoriteSize, personalityCharacteristics=personalityCharacteristics, activitiesCharacteristics=activitiesCharacteristics, ageCharacteristics=ageCharacteristics, availableTime=availableTime)
            return userPreferences
        except ValidationError as e:
            return e.errors()[0]['msg']

    def createHomeCharacteristicsData(self, houseType:str, availableSpace:str, openArea:bool, escapeRoutes:bool, haveChildren:bool)->HomeCharacteristics:
        userHomeCharacteristics = False
        try: 
            userHomeCharacteristics = HomeCharacteristics(houseType=houseType, availableSpace=availableSpace, openArea=openArea, escapeRoutes=escapeRoutes, haveChildren=haveChildren)
            return userHomeCharacteristics
        except ValidationError as e:
            return e.errors()[0]['msg']