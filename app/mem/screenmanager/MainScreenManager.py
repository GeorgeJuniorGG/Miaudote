from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from mem.screenmanager.screens import screens

class MainScreenManager(ScreenManager):

    orchestrator = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__previous = screens['welcome']

    def changeScreen(self, direction:str, screenName:str):
        if not self.has_screen(screenName):
            screen = self.orchestrator.startScreen(screenName)
            if screen != None:
                self.add_widget(screen)

        self.transition.direction = direction
        if not screens['signUp'] in screenName:
            self.__previous = self.current

        self.current = screenName

    def goBackward(self, direction:str):
        self.transition.direction = direction
        self.__previous, self.current = self.current, self.__previous  
