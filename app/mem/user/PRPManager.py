from mlo.adoption.AdoptionService import AdoptionService

from mem.screenmanager.screens import screens

from mui.protectorrequests.RequesterProfileScreen import RequesterProfileScreen

class PRPManager:

    def __init__(self, adoption:AdoptionService, arID:str) -> None:
        self.aService = adoption
        self.arID = arID
        sName = screens['requesterProfile'] + arID
        self.screen = RequesterProfileScreen(name = sName)
        self.screen.controller = self
        self.screen.insertAdopterData()
        self.screen.hideButtons()

    def adopterProfileData(self):
        data = self.aService.getAdopterData(self.arID)
        return data

    def approveRequest(self):
        if self.aService.approveAR(self.arID):
            msg = 'Converse com o adotante pelo chat para concluir a adoção!'
            self.screen.showToast(msg)
            return self.screen.manager.goBackward('right')

    def declineRequest(self):
        if self.aService.declineAR(self.arID):
            self.screen.showToast('Solicitação de adoção recusada com sucesso!')
            return self.screen.manager.goBackward('right')