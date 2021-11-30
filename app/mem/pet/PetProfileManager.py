from mui.petprofile.PetProfileScreen import PetProfileScreen
from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

from mem.screenmanager.screens import screens

class PetProfileManager:

    def __init__(self, userService:UserService, petService:PetService, petID:str) -> None:
        self.userService = userService
        self.petService = petService
        self.petID = petID
        self.petData = self.petService.getPetData(petID)
        self.screen = PetProfileScreen(self.petData, name=screens['petProfile']+petID)
        self.screen.controller = self