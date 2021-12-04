from mlo.user.ProtectorPetsService import ProtectorPetsService
from mui.userprofile.MyPetsScreen import MyPetsScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mem.screenmanager.screens import screens

class ProtectorPetsManager:

    def __init__(self, userService:UserService, petService:PetService, myPetsService:ProtectorPetsService) -> None:
        self.userService = userService
        self.petService = petService
        self.myPetsService = myPetsService
        self.screen = MyPetsScreen(name=screens['myPets'])
        self.screen.controller = self
        self.screen.addViewPets()

    def removePet(self, petID:str):
        self.myPetsService.removePet(petID)
    
    def petWasAdopted(self, petID:str):
        self.myPetsService.petWasAdopted(petID)

    def getProtectorPets(self):
        return self.myPetsService.getProtectorPets()