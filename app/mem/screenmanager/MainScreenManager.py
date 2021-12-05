from kivy.uix.screenmanager import FadeTransition, RiseInTransition, ScreenManager, SlideTransition
from kivy.properties import ObjectProperty
from mem.screenmanager.screens import screens

class MainScreenManager(ScreenManager):

    orchestrator = ObjectProperty()
    __TRANSITIONS = {'FadeTransition': FadeTransition, 
                     'SlideTransition': SlideTransition,
                     'RiseInTransition': RiseInTransition
                    }
    __refreshingScreens = {
        screens['adoRequests']: None,
        screens['recRequests']: None,
        screens['favorites']: None,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__previous = screens['welcome']

    def changeScreen(self, direction:str, screenName:str):
        if not self.has_screen(screenName) or screenName in self.__refreshingScreens.keys():
            screen = self.orchestrator.startScreen(screenName)
            if screen != None:
                if screenName in self.__refreshingScreens:
                    if (self.__refreshingScreens[screenName] != None):
                        self.remove_widget(self.__refreshingScreens[screenName])

                    self.__refreshingScreens[screenName] = screen

                self.add_widget(screen)

        self.transition.direction = direction
        if not 'SignUp' in screenName:
            self.__previous = self.current

        self.current = screenName

    def goBackward(self, direction:str):
        self.transition.direction = direction
        self.__previous, self.current = self.current, self.__previous

    def goHome(self):
        self.transition.direction = 'right'
        self.previous = screens['root']
        self.current = self.previous

    def changeTransition(self, tName:str):
        if tName in self.__TRANSITIONS.keys():
            self.transition = self.__TRANSITIONS[tName]()
