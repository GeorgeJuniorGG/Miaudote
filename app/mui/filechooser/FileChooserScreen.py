from kivymd.uix.screen import MDScreen
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.properties import ObjectProperty

class FileChooserScreen(MDScreen):
    image = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.imgTypes = ('png', 'jpg', 'jpeg')
        self.fileManager = MDFileManager(
            exit_manager=self.exitManager,
            select_path=self.selectPath,
            preview=True,            
        )
        self.fileManager.ext.append('.pdf')

    def fileManagerOpen(self):
        self.fileManager.show('/')  # output manager to the screen
        self.manager_open = True

    def getImage(self, path):
        self.exitManager()
        self.image.source = path


    def selectPath(self, path):
        for type in self.imgTypes:
            if type in path:
                return self.getImage(path)

        toast("Arquivo não suportado")


    def exitManager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        self.manager_open = False
        self.fileManager.close()