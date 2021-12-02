from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.properties import ObjectProperty

class FileChooserScreen(MDScreen):
    #image = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.imgTypes = ('png', 'jpg', 'jpeg')
        self.fileManager = MDFileManager(
            exit_manager=self.exitManager,
            select_path=self.selectPath,
            preview=True,            
        )
        self.controller = None

    def fileManagerOpen(self):
        self.fileManager.show(self.controller.currentDir)  # output manager to the screen
        self.chooserOpen = True


    def selectPath(self, path):
        self.controller.currentDir = self.fileManager.current_path
        for type in self.imgTypes:
            if type in path:
                self.exitManager(sel=True)
                self.controller.sendFilePath(path)
                return

        toast("Arquivo não suportado")


    def exitManager(self, *args, sel=False):
        '''Called when the user reaches the root of the directory tree.'''
        self.chooserOpen = False
        self.fileManager.close()
        
        if not sel:
            self.controller.exitScreen()