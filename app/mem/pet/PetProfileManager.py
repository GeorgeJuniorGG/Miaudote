from mlo.user.AdopterRequestsService import AdopterRequestsService
from mlo.user.FavoritesService import FavoritesService
from mui.petprofile.PetProfileScreen import PetProfileScreen
from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

from mem.screenmanager.screens import screens

class PetProfileManager:

    def __init__(self, userService:UserService, petService:PetService, favService:FavoritesService, adoReqService: AdopterRequestsService, petID:str) -> None:
        self.userService = userService
        self.petService = petService
        self.favService = favService
        self.adoReqService = adoReqService
        self.petID = petID
        self.petData = self.petService.getPetData(petID)
        self.screen = PetProfileScreen(self.petData, name=screens['petProfile']+petID)
        self.screen.controller = self
        self.screen.start_favorite_state(self.getFavoriteStatus(petID))

    def addFavorite(self, petID:str):
        self.favService.addPet(petID)
    
    def removeFavorite(self, petID:str):
        self.favService.removePet(petID)

    def getFavoriteStatus(self, petID:str):
        return self.favService.getFavoriteStatus(petID)
    
    def addRequest(self, petID:str):
        self.adoReqService.addRequest(petID)