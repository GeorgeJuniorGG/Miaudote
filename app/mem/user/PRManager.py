from mui.protectorrequests.RequestsReceivedScreen import RequestsReceivedScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService

from mem.screenmanager.screens import screens

class PRManager:
    def __init__(self, userService:UserService, petService:PetService) -> None:
        self.userService = userService
        self.petService = petService
        self.screen = RequestsReceivedScreen(name=screens['recRequests'])
        self.screen.controller = self