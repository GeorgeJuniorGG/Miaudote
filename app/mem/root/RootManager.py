from mlo.petsearch.searchService import SearchService
from mui.root.RootScreen import RootScreen

from mem.screenmanager.screens import screens

from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService

class RootManager:

    petService: PetService
    profileScreen = None
    menuScreen = None
    homeScreen = None

    def __init__(self, uService: UserService, petService:PetService, searchService: SearchService, orchestrator) -> None:
        self.userService = uService
        self.petService = petService
        self.searchService = searchService
        self.orchetrator = orchestrator
        self.screen = RootScreen(name=screens['root'])
        self.screen.controller = self
        self.setController()
        self.profileScreen.getUserData()
        self.homeScreen.addViewPets()
    
    def setController(self):
        self.profileScreen = self.screen.profileScreen
        self.profileScreen.controller = self
        self.homeScreen = self.screen.homeScreen
        self.homeScreen.controller = self
        self.menuScreen = self.screen.menuScreen
        self.menuScreen.controller = self

    def getUserData(self):
        return self.userService.getUserData()

    def getAllPets(self):
        return self.petService.getAllPets()

    def logout(self):
        self.orchetrator.userLogout()
    
    def getRecommended(self):
        return self.searchService.getRecommended()
    
    def getSearchResults(self, text):
        words = text.split(" ")
        return self.searchService.getSearchResults(words)    