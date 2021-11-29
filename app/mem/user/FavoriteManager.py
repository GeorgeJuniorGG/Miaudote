from mui.userprofile.FavoritesScreen import FavoritesScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mem.screenmanager.screens import screens

class FavoriteManager:

    def __init__(self, userService:UserService, petService:PetService) -> None:
        self.userService = userService
        self.petService = petService
        self.screen = FavoritesScreen(name=screens['favorites'])
        self.screen.controller = self

    def removeFavorite(self, petID:str):
        pass