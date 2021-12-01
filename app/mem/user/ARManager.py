from mlo.user.AdopterRequestsService import AdopterRequestsService
from mui.adopterrequests.RequestsScreen import RequestsScreen
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mem.screenmanager.screens import screens

class ARManager:

    def __init__(self, userService:UserService, petService:PetService, adoReqService: AdopterRequestsService) -> None:
        self.userService = userService
        self.petService = petService
        self.adoReqService = adoReqService
        self.screen = RequestsScreen(name=screens['adoRequests'])
        self.screen.controller = self
        self.screen.addViewRequests()
    
    def removeRequest(self, petID:str):
        self.adoReqService.removeRequest(petID)

    def getRequests(self):
        return self.adoReqService.getRequests()