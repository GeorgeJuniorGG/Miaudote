import json
from datetime import datetime, timedelta

from mem.screenmanager.MainScreenManager import MainScreenManager
from mem.screenmanager.screens import screens
from recipeBook import recipes

class Orchestrator:

    __USER_DATA = 'user.json'

    def __init__(self, manager:MainScreenManager) -> None:
        self.manager = manager
        self.mTransition = 'SlideTransition'
        self.manager.changeTransition(self.mTransition)
        self.manager.orchestrator = self
        self.__components = dict()
        self.userID = self.__openUserFile()
    
    # Abrir o arquivo com as informações de login do Usuário
    # Permite mudança de flow no app
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

    # Determina qual deve ser o flow ao iniciar o app
    def appFlow(self):
        appFlow = self.__welcomeFlow
        print(self.userID)
        if self.userID != "":
            appFlow = self.__rootFlow

        appFlow()

    # Coloca algumas propriedades do objeto em um dicionário
    # necessária para obter alguns argumentos de componentes
    def dict(self):
        return {
            'userID': self.userID,
            'orchestrator': self,
            'mTransition': self.mTransition,
        }

    # Adiciona uma referência de um componente ao orchestrator
    # minimiza a necessiade de recursão em __buildComponent
    # faz com que componentes que usam a mesma dependência a compartilhem
    def __addComponent(self, cName:str, component):
        self.__components[cName] = component
    
    # Carrega os argumentos primitivos requeridos por um componente
    def __loadArgs(self, cArgs, outArgs:dict):
        pArgs = list()
        if cArgs != None:
            inArgs = self.dict()
            inArgsKeys = inArgs.keys()
            outArgsKeys = outArgs.keys()
            for arg in cArgs:
                if arg in inArgsKeys:
                    pArgs.append(inArgs[arg])
                elif arg in outArgsKeys:
                    pArgs.append(outArgs[arg])

        return pArgs

    # Verifica se uma dependência já foi criada
    # TODO?: Futuramente talvez seja necessário estabelecer
    #       uma indicação de exclusividade para alguns componentes
    #       que não podem ser compartilhados entre diferentes telas
    def __checkDep(self, dep):
        if dep in self.__components.keys():
            return self.__components[dep]

        return None

    # Função recursiva que constroi algum componente do App
    # instânciando se necessário suas dependências
    def __buildComponent(self, component:dict, outArgs:dict={}):
        deps = list()
        cDeps = component['deps']
        if cDeps != None:
            for dep in cDeps:
                cDep = self.__checkDep(dep)
                if cDep == None or (not component['unique']):
                    cDep = self.__buildComponent(recipes[dep], outArgs)
                    self.__addComponent(dep, cDep)
                deps.append(cDep)

        cArgs = component['pArgs']
        pArgs = self.__loadArgs(cArgs, outArgs)
        return component['class'](*deps, *pArgs)

    # Constroi um componente do app a partir de sua receita
    def buildComponent(self, cName, outArgs:dict={}):
        recipe = recipes[cName]
        return self.__buildComponent(recipe, outArgs)

    # Inicializa os componentes necessário para criar uma tela do app
    def startScreen(self, screenName, outArgs:dict={}):
        controller = self.buildComponent(screenName, outArgs)

        # Os Managers de SignUp Possuem mais 1 tela,
        # por isso optei por fazer a adição de tela deles diferente
        if screenName in (screens['signUp'], screens['petSignUp']):
            controller.manager = self.manager
            controller.addScreens()
            return None

        # retorna a tela para ser adicionada ao ScreenManager
        return controller.screen

    # Flow do app relacionado a etapa de login e cadastro de usuários
    def __welcomeFlow(self):
        welcomeManager = self.buildComponent(screens['welcome'])
        self.manager.add_widget(welcomeManager.screen)
        #self.__startSignUp()

    # Flow do app relacionado ao pós-login
    def __rootFlow(self):
        rootManager = self.buildComponent(screens['root'])
        self.manager.add_widget(rootManager.screen)

    # Armazena as informações de login do Usuário
    # Permite que o usuário não precise logar novamente
    def __registerLogin(self, userID:str):
        self.userID = userID
        userData = {
            'userID': self.userID,
            'lastLogin': datetime.now().isoformat(sep=' ', timespec='milliseconds')
        }
        with open(self.__USER_DATA, 'w', encoding='utf-8') as uFile:
            json.dump(userData, uFile, indent=2)

    # Apaga o registro de login do usuário
    # util para o recurso de logout
    def __eraseLoginData(self):
        with open(self.__USER_DATA, 'w', encoding='utf-8') as uFile:
            uFile.write("")

        # limpar os dados após o logout
        self.userID = ""
        self.__components = dict()

    # Quando o usuário efetua o login essa função salvas as informações de login
    # e redireciona para a HomeScreen do app
    def userLogin(self, userID:str):
        self.__registerLogin(userID)
        self.manager.clear_widgets()
        self.__rootFlow()
        self.manager.changeScreen('left', screens['root'])

    # Quando o usuário efetuar o logout do app seus dados são apagados
    # e o app redireciona para a tela de welcome
    def userLogout(self):
        self.__eraseLoginData()
        self.manager.clear_widgets()
        self.__welcomeFlow()
        self.manager.changeScreen('left', screens['welcome'])

    def callChangeScreen(self, screenName:str):
        # if self.mTransition != 'RiseInTransition':
        #     self.mTransition = 'RiseInTransition'
        #     self.manager.changeTransition(self.mTransition)

        self.manager.changeScreen('left', screenName)
    
    # Abrir a tela de perfil do pet
    def openPetProfile(self, petID:str):
        cName = screens['petProfile']
        if cName+petID in self.manager.screen_names:
            self.manager.remove_widget(self.manager.get_screen(cName+petID))
        
        outArgs = {'petID': petID}
        screen = self.startScreen(cName, outArgs=outArgs)
        self.manager.add_widget(screen)
        self.manager.changeScreen('left', screen.name)

    # Abrir a tela de requisição do pet
    def openPetRProfile(self, arID:str):
        cName = screens['petRP']
        if cName+arID in self.manager.screen_names:
            self.manager.remove_widget(self.manager.get_screen(cName+arID))
        
        outArgs = {'arID': arID}
        screen = self.startScreen(cName, outArgs=outArgs)
        self.manager.add_widget(screen)
        self.manager.changeScreen('left', screen.name)


    # Abrir a tela com informações sobre o adotante em uma AR
    def openARProfile(self, arID:str):
        cName = screens['requesterProfile']
        if cName+arID in self.manager.screen_names:
            self.manager.remove_widget(self.manager.get_screen(cName+arID))
        
        outArgs = {'arID': arID}
        screen = self.startScreen(cName, outArgs=outArgs)
        self.manager.add_widget(screen)
        self.manager.changeScreen('left', screen.name)

    # Abrir a tela de Chat
    def openChat(self, chatData:dict):
        cName = screens['chat']
        if cName+chatData['chatID'] in self.manager.screen_names:
            self.manager.remove_widget(self.manager.get_screen(cName+chatData['chatID']))
        
        screen = self.startScreen(cName, outArgs=chatData)
        self.manager.add_widget(screen)
        self.manager.changeScreen('left', screen.name)

    # Abrir o FileChooserScreen
    def openFileManager(self, fClient):
        cName = screens['fileChooser']
        if cName in self.manager.screen_names:
            self.manager.remove_widget(self.manager.get_screen(cName))

        outArgs = {'client': fClient}
        controller = self.buildComponent(cName, outArgs=outArgs)
        self.__addComponent(cName, controller)
        self.manager.add_widget(controller.screen)
        self.manager.changeScreen('left', cName)

    def callGoBackward(self, screen:str=''):
        if screen != '':
            return self.manager.changeScreen('right', screen)
        
        return self.manager.goBackward('right')
