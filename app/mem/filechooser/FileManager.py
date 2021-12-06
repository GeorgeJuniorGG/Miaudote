from .FMClient import FMClient
from mui.filechooser.FileChooserScreen import FileChooserScreen
from mem.screenmanager.screens import screens

class FileManager:
    def __init__(self, client:FMClient) -> None:
        self.client = client
        self.client.registreFM(self)
        self.screen = None
        self.currentDir = self.client.getCurrentPath()
        self.manager = None
        self.openFileChooser()
        self.__openScreen()

    def __openScreen(self):
        self.screen.fileManagerOpen()

    def openFileChooser(self):
        if self.screen != None:
            self.manager = self.screen.manager
            self.screen = None

        self.screen = FileChooserScreen(name=screens['fileChooser'])
        self.screen.controller = self

        if self.manager != None:
            self.manager.add_widget(self.screen)
            self.__openScreen()

    def exitScreen(self):
        print('Passou aqui')
        if self.screen != None:
            self.manager = self.screen.manager
            self.screen = None

        self.sendFilePath(None)

    def sendFilePath(self, filePath:str):
        self.client.receiveFile(filePath, self.currentDir)
