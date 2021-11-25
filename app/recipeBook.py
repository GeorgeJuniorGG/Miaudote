# Manager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.welcome.WelcomeManager import WelcomeManager
from mem.root.RootManager import RootManager

# Service
from mlo.auth.dataModel import DataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService

# Database
from mlo.storage.firebaseDB import FirebaseDB
from mlo.database.firebaseUserDB import FUserDB
from mlo.database.firebasePetDB import FPetDB

# Screen Names
from mem.screenmanager.screens import screens

services = {
    'dataModel': 'DataModel',
    'auth': 'FirebaseAuth',
    'user': 'UserService',
    'pet': 'PetService',
}

databases = {
    'user': 'FUserDB',
    'storage': 'FirebaseDB',
    'pet': 'FPetDB'
}

recipes = {

    services['dataModel'] : {
        'class': DataModel,
        'deps': None,
        'pArgs': None
    },

    services['auth'] : {
        'class': FireBaseAuthService,
        'deps': None,
        'pArgs': None
    },

    services['pet'] : {
        'class': PetService,
        'deps': (databases['pet'],),
        'pArgs': None
    },

    services['user'] : {
        'class': UserService,
        'deps': (databases['user'],),
        'pArgs': None
    },

    databases['pet'] : {
        'class': FPetDB,
        'deps': None,
        'pArgs': None
    },

    databases['user'] : {
        'class': FUserDB,
        'deps': None,
        'pArgs': ('userID',)
    },

    databases['storage'] : {
        'class': FirebaseDB,
        'deps': None,
        'pArgs': None
    }, 

    screens['welcome'] : {
        'class': WelcomeManager,
        'deps': None,
        'pArgs': None
    },

    screens['login'] : {
        'class': LoginManager,
        'deps': (services['auth'],),
        'pArgs': None
    },

    screens['signUp'] : {
        'class': SignUpManager,
        'deps': (services['auth'], services['dataModel'], databases['storage']),
        'pArgs': None
    },
    
    screens['root'] : {
        'class': RootManager,
        'deps': (services['user'], services['pet']),
        'pArgs': ('orchestrator',)  
    }
}