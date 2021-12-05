from mui.adopterrequests.AdoptionRScreen import AdoptionRScreen

from mem.screenmanager.screens import screens

class PARManager:

    def __init__(self) -> None:
        
        self.screen = AdoptionRScreen(name=screens['PARScreen'])
        self.screen.controller = self

    def openARs(self):
        orchestrator = self.screen.manager.orchestrator
        orchestrator.callChangeScreen(screens['adoRequests'])