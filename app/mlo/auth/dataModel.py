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
        except ValidationError as e:
                print(e)
        return userData

    def createAddressData(self, state:str, city:str, CEP:int, neighborhood:str, address:str, number:int):
        userAddress = False
        try:
            userAddress = Address(state=state, city=city, CEP=CEP, neighborhood=neighborhood, address=address, number=number)
        except ValidationError as e:
                print(e)
        return userAddress

    def createUserPreferencesData(self, haveAnimal:str, favoriteAnimal:str, favoriteSize:str, personalityCharacteristics: str, activitiesCharacteristics: str, ageCharacteristics: str, availableTime:str)->UserPreferences:
        userPreferences = False
        try:
            userPreferences = UserPreferences(haveAnimal=haveAnimal, favoriteAnimal=favoriteAnimal, favoriteSize=favoriteSize, personalityCharacteristics=personalityCharacteristics, activitiesCharacteristics=activitiesCharacteristics, ageCharacteristics=ageCharacteristics, availableTime=availableTime)
        except ValidationError as e:
                print(e)
        return userPreferences

    def createHomeCharacteristicsData(self, houseType:str, availableSpace:str, openArea:bool, escapeRoutes:bool, haveChildren:bool)->HomeCharacteristics:
        userHomeCharacteristics = False
        try: 
            userHomeCharacteristics = HomeCharacteristics(houseType=houseType, availableSpace=availableSpace, openArea=openArea, escapeRoutes=escapeRoutes, haveChildren=haveChildren)
        except ValidationError as e:
            print(e)
        return userHomeCharacteristics