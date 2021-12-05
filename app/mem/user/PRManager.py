from mui.protectorrequests.RequestsReceivedScreen import RequestsReceivedScreen
from mlo.adoption.AdoptionService import AdoptionService

from mem.screenmanager.screens import screens


class PRManager:

    def __init__(self, adpt:AdoptionService) -> None:
        self.adoptionService = adpt
        self.screen = RequestsReceivedScreen(name=screens['recRequests'])
        self.screen.controller = self
        self.screen.addRequestsViews()

    def getRequests(self):
        return self.adoptionService.getARData()

    def removeRequest(self, arID:str):
        self.adoptionService.declineAR(arID)

    def openRequest(self, arID:str):
        orchestrator = self.screen.manager.orchestrator
        orchestrator.openARProfile(arID)

    def openChat(self, arID:str):
        chatData = self.adoptionService.getChatData(arID)
        orchestrator = self.screen.manager.orchestrator
        orchestrator.openChat(chatData)