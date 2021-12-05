from mlo.adoption.AdoptionService import AdoptionService
from mui.adopterrequests.RequestsScreen import RequestsScreen

from mem.screenmanager.screens import screens

class ARManager:

    def __init__(self, adoptionService: AdoptionService) -> None:
        self.adoptionService = adoptionService
        self.screen = RequestsScreen(name=screens['adoRequests'])
        self.screen.controller = self
        self.screen.addViewRequests()
    
    def removeRequest(self, arID:str):
        self.adoptionService.deleteAR(arID)

    def getRequests(self):
        return self.adoptionService.getARData()

    def openRequest(self, arID:str):
        orchestrator = self.screen.manager.orchestrator
        orchestrator.openPetRProfile(arID)

    def openChat(self, arID:str):
        chatData = self.adoptionService.getChatData(arID)
        orchestrator = self.screen.manager.orchestrator
        orchestrator.openChat(chatData)