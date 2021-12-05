from mlo.adoption.AdoptionService import AdoptionService
from mlo.pets.PetService import PetService
from mui.petrequests.PetRScreen import PetRScreen
from mem.screenmanager.screens import screens

class PetRProfileManager:

    def __init__(self, adoService: AdoptionService, arID:str) -> None:
        self.adoService = adoService
        self.petData = self.adoService.getPetData(arID)
        self.arID = arID
        self.screen = PetRScreen(self.petData, name=screens['petRP']+arID)
        self.screen.controller = self
            
    def cancelRequest(self):
        if not self.adoService.deleteAR(self.arID):
            self.screen.showToast('Ocorreu um erro ao tentar cancelar a solicitação')

    def openChat(self):
        chatData = self.adoService.getChatData(self.arID)
        orchestrator = self.screen.manager.orchestrator
        orchestrator.openChat(chatData)