from mui.adopterrequests.RequestsScreen import RequestsScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mem.screenmanager.screens import screens

class ARManager:

    def __init__(self, userService:UserService, petService:PetService) -> None:
        self.userService = userService
        self.petService = petService
        self.screen = RequestsScreen(name=screens['adoRequests'])
        self.screen.controller = self