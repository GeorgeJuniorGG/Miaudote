from mlo.adoption.AdoptionService import AdoptionService
from mlo.user.FavoritesService import FavoritesService
from mui.petprofile.PetProfileScreen import PetProfileScreen
from mlo.pets.PetService import PetService

from mem.screenmanager.screens import screens

class PetProfileManager:

    def __init__(self, petService:PetService, favService:FavoritesService,
                 adoService: AdoptionService, petID:str) -> None:
        
        self.petService = petService
        self.favService = favService
        self.adoService = adoService
        self.petID = petID
        self.petData = self.petService.getPetData(petID)
        self.screen = PetProfileScreen(self.petData, name=screens['petProfile']+petID)
        self.screen.controller = self
        self.screen.start_favorite_state(self.getFavoriteStatus(petID))

        if(self.userService.getUserType()=='protector'):
            self.screen.screenToProtector()

    def addFavorite(self, petID:str):
        self.favService.addPet(petID)
    
    def removeFavorite(self, petID:str):
        self.favService.removePet(petID)

    def getFavoriteStatus(self, petID:str):
        return self.favService.getFavoriteStatus(petID)
    
    def addRequest(self, petID:str):
        if not self.adoService.createAR(petID):
            self.screen.showToast('Não foi possível realizar a solicitação de adoção!')
        