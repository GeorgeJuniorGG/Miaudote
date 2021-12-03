from mlo.adoption.AdoptionService import AdoptionService

from mem.screenmanager.screens import screens

from mui.protectorrequests.RequesterProfileScreen import RequesterProfileScreen

class PRPManager:

    def __init__(self, adoption:AdoptionService) -> None:
        self.aService = adoption
        sName = screens['requesterProfile'] + self.aService.getUserID()
        self.screen = RequesterProfileScreen(name = sName)
        self.screen.controller = self
        self.screen.insertAdopterData()

    def adopterProfileData(self):
        return self.aService.getUserData()