import json

from mem.screenmanager.MainScreenManager import MainScreenManager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.welcome.WelcomeManager import WelcomeManager

from mlo.storage.firebaseDB import FirebaseDB
from mlo.auth.dataModel import DataModel
from mlo.auth.firebaseAuth import FireBaseAuthService

from mem.screenmanager.screens import screens

screenRecipes = {

    screens['welcome']: {
        'db': {
            'class': None,
            'args': None
        },
        'service': {
            'class': None,
            'args': None            
        },
        'controller': {
            'class': WelcomeManager,
            'args': None
        },
        
    },

    screens['login']: {
        'db': {
            'class': None,
            'args': None
        },
        'service': {
            'class': FireBaseAuthService,
            'args': None            
        },
        'controller': {
            'class': LoginManager,
            'args': None
        },    
    },

    screens['signUp']: {
        'db': {
            'class': None,
            'args': None
        },
        'service': {
            'class': FireBaseAuthService,
            'args': None            
        },
        'controller': {
            'class': SignUpManager,
            'args': None
        },
    },

    screens['root']: {
        'controller': None,
        'service': None,
        'appFlow': 'rootFlow'
    }


}


class Orchestrator:

    __USER_DATA = 'user.json'

    def __init__(self, manager:MainScreenManager) -> None:
        self.manager = manager
        self.manager.orchestrator = self
        self.userID = self.__openUserFile()
    
    def __openUserFile(self):
        with open(self.__USER_DATA, 'r+', encoding='utf-8') as uFile:
            suData = uFile.read()
            if suData == "":
                return ""
            uData = json.loads(suData)
            return uData['userID']

    def appFlow(self):
        appFlow = self.__welcomeFlow
        if self.userID != "":
            appFlow = self.__rootFlow

        appFlow()

    def dict(self):
        return {
            'userID': self.userID,
        }

    def __makeComponent(self, comp:dict, fArg=None, outArgs={}):
        if comp['args'] == None:
            if fArg == None:
                return comp['class']()

            return comp['class'](fArg)

        # TODO
        # carregar os argumentos do Componente usando dados do Orquestrador
        inArgs = self.dict()
        args = list()
        for arg in comp['args']:
            if arg in inArgs.keys():
                args.append(inArgs[arg])
            elif arg in outArgs.keys():
                args.append(outArgs[arg])

        if fArg != None:
            return comp['class'](fArg, *args)

        return comp['class'](*args)


    def __mixComponents(self, comp1:dict, comp2:dict, oA1:dict, oA2:dict):
        fArg = None
        if comp1['class'] == None:
            if comp2['class'] == None:
                return None
            
            fArg = self.__makeComponent(comp2, oA2)
        
        return self.__makeComponent(comp1, fArg, oA1)

    # Instancia uma Screen do App, inializando todas as suas dependencias
    def startScreen(self, screenName, outArgs:dict={}):
        if screenName == screens['signUp']:
            return self.__startSignUp()

        return self.__startScreen(screenName, outArgs)

    def __startScreen(self, screenName, outArgs:dict={}):
        screenRecipe = screenRecipes[screenName]
        dbComponent = screenRecipe['db']
        serviceComponent = screenRecipe['service']
        controllerComponent = screenRecipe['controller']

        argList = []
        for key in ['db', 'service', 'controller']:
            if key in outArgs.keys():
                argList.append(outArgs[key])
            else:
                argList.append({})
        
        dbArgs, sArgs, cArgs = argList

        service = self.__mixComponents(serviceComponent, dbComponent, sArgs, dbArgs)
        controller = self.__makeComponent(controllerComponent, service, cArgs)

        return controller.screen

    def __startSignUp(self):
        dataModel = DataModel()
        auth = FireBaseAuthService()
        storege = FirebaseDB()        
        controller = SignUpManager(auth, dataModel, storege)
        controller.manager = self.manager
        controller.addScreens()
        return None

    def __welcomeFlow(self):
        welcomeScreen = self.startScreen(screens['welcome'])
        self.manager.add_widget(welcomeScreen)
        #self.__startSignUp()


    def __rootFlow(self):
        rootScreen = self.startScreen(screens['root'])
        self.manager.add_widget(rootScreen)
