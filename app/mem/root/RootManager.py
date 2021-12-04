from mlo.petsearch.searchService import SearchService
from mui.root.RootScreen import RootScreen

from mem.screenmanager.screens import screens
from mem.filechooser.FMClient import FMClient

from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService

from kivy.clock import Clock
from functools import partial
from kivymd.toast import toast

class RootManager(FMClient):

    petService: PetService
    profileScreen = None
    menuScreen = None
    homeScreen = None

    def __init__(self, uService: UserService, petService:PetService,
                 searchService: SearchService, orchestrator) -> None:

        self.userService = uService
        self.petService = petService
        self.searchService = searchService
        self.orchetrator = orchestrator
        self.screen = RootScreen(name=screens['root'])
        self.screen.controller = self
        self.setController()
        self.profileScreen.getUserData()
        self.homeScreen.addViewPets()
        self.__FM = None
        self.__CP = "/"
    
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

    def callChangeScreen(self, screenName:str):
        self.orchetrator.callChangeScreen(screenName)

    def openPetProfile(self, petID:str):
        if(self.petService.getPetData(petID) != {}):
            self.orchetrator.openPetProfile(petID)
        else:
            self.homeScreen.addViewPets()
            toast("Esse pet já foi adotado!")
            

    def openFileManager(self):
        self.orchetrator.openFileManager(self)

    def registreFM(self, FM):
        self.__FM = FM

    # Recebe a nova imagem do usuário do File Chooser
    def receiveFile(self, file: str, path:str):
        self.__CP = path
        if file != None:
            oldImage = self.profileScreen.changeUserImage(file)
            self.orchetrator.callGoBackward()
            Clock.schedule_once(partial(self.updateImage, file, oldImage), 0.5)

    # Atualiza a imagem do usuário no banco            
    def updateImage(self, file, oldImage, *largs):
        update_status = self.userService.updateUserImage(file)
        if not update_status:
            print('Ocorreu um erro ao tentar trocar a imagem!')
            print('Tente novamente mais tarde!')
            self.profileScreen.changeUserImage(oldImage)

    # Abrir o File Chooser
    def callFileManager(self):
        self.__FM.openFileChooser()

    def getCurrentPath(self) -> str:
        return self.__CP