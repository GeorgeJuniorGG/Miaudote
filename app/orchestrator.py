import json
from datetime import datetime, time, timedelta

from mem.screenmanager.MainScreenManager import MainScreenManager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.welcome.WelcomeManager import WelcomeManager
from mem.root.RootManager import RootManager

from mlo.storage.firebaseDB import FirebaseDB
from mlo.auth.dataModel import DataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.user.UserService import UserService
from mlo.database.firebaseUserDB import FUserDB
from mlo.database.firebasePetDB import FPetDB
from mlo.pets.PetService import PetService

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
        'db': {
            'class': FUserDB,
            'args': ('userID',)
        },
        'service': {
            'class': UserService,
            'args': None            
        },
        'controller': {
            'class': RootManager,
            'args': ('orchestrator',)
        },
    },
    screens['home']: {
        'db': {
            'class': FPetDB,
            'args': None
        },
        'service': {
            'class': PetService,
            'args': None            
        }        
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

            lastLogin = datetime.strptime(uData['lastLogin'], '%Y-%m-%d %H:%M:%S.%f')
            now = datetime.now()
            interv = lastLogin + timedelta(days=8)
            if interv < now:
                return ""

            return uData['userID']

    def appFlow(self):
        appFlow = self.__welcomeFlow
        if self.userID != "":
            appFlow = self.__rootFlow

        appFlow()

    def dict(self):
        return {
            'userID': self.userID,
            'orchestrator': self
        }

    def __makeComponent(self, comp:dict, fArg=None, outArgs={}):
        if comp['args'] == None:
            if fArg == None:
                return comp['class']()

            return comp['class'](fArg)

        # TODO
        # carregar os argumentos do Componente usando dados do Orquestrador
        inArgs = self.dict()
        #print(inArgs)
        args = list()
        for arg in comp['args']:
            #print(arg)
            if arg in inArgs.keys():
                args.append(inArgs[arg])
            elif arg in outArgs.keys():
                args.append(outArgs[arg])

        if fArg != None:
            return comp['class'](fArg, *args)

        #print(args)
        return comp['class'](*args)


    def __mixComponents(self, comp1:dict, comp2:dict, oA1:dict, oA2:dict):
        fArg = None
        if comp1['class'] == None:
            return None

        if comp2['class'] != None:    
            fArg = self.__makeComponent(comp2, outArgs=oA2)
        #print(fArg)
        
        return self.__makeComponent(comp1, fArg, outArgs=oA1)

    def __splitArgs(self, outArgs:dict):
        argList = []
        for key in ['db', 'service', 'controller']:
            if key in outArgs.keys():
                argList.append(outArgs[key])
            else:
                argList.append({})
        
        return argList

    def __startScreen(self, screenName, outArgs:dict={}):
        screenRecipe = screenRecipes[screenName]
        dbComponent = screenRecipe['db']
        serviceComponent = screenRecipe['service']
        controllerComponent = screenRecipe['controller']

        dbArgs, sArgs, cArgs = self.__splitArgs(outArgs)

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

    # Instancia uma Screen do App, inializando todas as suas dependencias
    def startScreen(self, screenName, outArgs:dict={}):
        if screenName == screens['signUp']:
            return self.__startSignUp()

        return self.__startScreen(screenName, outArgs)

    def makeComponent(self, screenName, outArgs:dict={}):
        compRecipe = screenRecipes[screenName]
        dbComponent = compRecipe['db']
        serviceComponent = compRecipe['service']        

        dbArgs, sArgs, dummy = self.__splitArgs(outArgs)
        service = self.__mixComponents(serviceComponent, dbComponent, sArgs, dbArgs)
        return service

    def __welcomeFlow(self):
        welcomeScreen = self.startScreen(screens['welcome'])
        self.manager.add_widget(welcomeScreen)
        #self.__startSignUp()


    def __rootFlow(self):
        rootScreen = self.startScreen(screens['root'])
        self.manager.add_widget(rootScreen)

    def __registerLogin(self, userID:str):
        self.userID = userID
        userData = {
            'userID': self.userID,
            'lastLogin': datetime.now().isoformat(sep=' ', timespec='milliseconds')
        }
        with open(self.__USER_DATA, 'w', encoding='utf-8') as uFile:
            json.dump(userData, uFile, indent=2)

    def userLogin(self, userID:str):
        self.__registerLogin(userID)
        self.manager.clear_widgets()
        self.__rootFlow()
        self.manager.changeScreen('left', screens['root'])
    