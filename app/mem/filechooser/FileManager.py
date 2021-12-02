from .FMClient import FMClient
from mui.filechooser.FileChooserScreen import FileChooserScreen
from mem.screenmanager.screens import screens

class FileManager:
    def __init__(self, client:FMClient) -> None:
        self.client = client
        self.client.registreFM(self)
        self.screen = None
        self.currentDir = '/'
        self.manager = None
        self.openFileChooser()
        self.__openScreen()

    def __openScreen(self):
        self.screen.fileManagerOpen()

    def openFileChooser(self):
        if self.screen != None:
            self.manager = self.screen.manager
            self.manager.remove_widget(self.screen)
            self.screen = None

        self.screen = FileChooserScreen(name=screens['fileChooser'])
        self.screen.controller = self
        
        if self.manager != None:
            self.manager.add_widget(self.screen)
            self.__openScreen()

    def exitScreen(self):
        if self.screen != None:
            self.manager = self.screen.manager
            self.manager.remove_widget(self.screen)
            self.screen = None

        if self.manager != None:
            self.screen = FileChooserScreen(name=screens['fileChooser'])
            self.screen.controller = self
            self.manager.add_widget(self.screen)
            self.__openScreen()

    def sendFilePath(self, filePath:str):
        self.client.receiveFile(filePath)
