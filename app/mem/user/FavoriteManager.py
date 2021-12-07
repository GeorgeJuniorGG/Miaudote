from mlo.user.FavoritesService import FavoritesService
from mui.userprofile.FavoritesScreen import FavoritesScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mem.screenmanager.screens import screens

class FavoriteManager:

    def __init__(self, userService:UserService, petService:PetService, favService:FavoritesService) -> None:
        self.userService = userService
        self.petService = petService
        self.favService = favService
        self.screen = FavoritesScreen(name=screens['favorites'])
        self.screen.controller = self
        self.screen.addViewPets()

    def removeFavorite(self, petID:str):
        self.favService.removePet(petID)

    def getFavorites(self):
        return self.favService.getFavorites()

    def openPetProfile(self, petID:str):
        if(self.petService.getPetData(petID) != {}):
            orchestrator = self.screen.manager.orchestrator
            orchestrator.openPetProfile(petID)
        else:
            self.screen.addViewPets()
            self.screen.showToast("Esse pet já foi adotado!")