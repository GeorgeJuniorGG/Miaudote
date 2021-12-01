# Manager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.welcome.WelcomeManager import WelcomeManager
from mem.root.RootManager import RootManager
from mem.petSignUp.petSignUpManager import PetSignUpManager

# Service
from mlo.auth.dataModel import DataModel
from mlo.pets.PetDataModel import PetDataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mlo.petrecommendation.RecommendedPets import RecommendedPets
from mlo.petsearch.resultsPrioritization import ResultsPrioritization
from mlo.petsearch.searchLogic import SearchLogic
from mlo.petsearch.searchService import SearchService

# Database
from mlo.storage.firebaseDB import FirebaseDB
from mlo.database.firebaseUserDB import FUserDB
from mlo.database.firebasePetDB import FPetDB

# Screen Names
from mem.screenmanager.screens import screens

services = {
    'dataModel': 'DataModel',
    'petDataModel': 'PetDataModel',
    'auth': 'FirebaseAuth',
    'user': 'UserService',
    'pet': 'PetService',
    'recom': 'RecommendedPets',
    'prior': 'ResultsPrioritization',
    'sLogic': 'SearchLogic',
    'search': 'SearchService'   
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

    services['petDataModel'] : {
        'class': PetDataModel,
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

    services['recom'] : {
        'class': RecommendedPets,
        'deps': (services['user'], services['pet']),
        'pArgs': None
    },

    services['prior'] : {
        'class': ResultsPrioritization,
        'deps': (services['pet'], services['user'],),
        'pArgs': None
    },

    services['sLogic'] : {
        'class': SearchLogic,
        'deps': (services['pet'], services['recom']),
        'pArgs': None
    },

    services['search'] : {
        'class': SearchService,
        'deps': (services['prior'], services['sLogic'], services['recom']),
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
        'deps': (services['user'], services['pet'], services['search']),
        'pArgs': ('orchestrator',)  
    },

    screens['petSignUp'] : {
        'class': PetSignUpManager,
        'deps': (databases['pet'],services['petDataModel'],services['user']),
        'pArgs': None
    }
}