from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class AdoptionService:

    def __init__(self, usrService:UserService, petService:PetService):
        self.userService = usrService
        self.petService = petService

    def getUserID(self) -> str:
        return self.userService.getUserID()

    def getUserData(self) -> dict:
        raw = self.userService.getUserData()
        
        data = {
            'name': raw['name'],
            'adopterImage': raw['userImage'],
            'city': raw['address']['city'],
            'state': raw['address']['city'],
            'homeCharacteristics': raw['homeCharacteristics'],
            'availableTime': raw['preferences']['availableTime'],
            'haveAnimal': raw['preferences']['haveAnimal'],
        }

        return data