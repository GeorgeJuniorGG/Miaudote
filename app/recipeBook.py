# Manager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.user.FavoriteManager import FavoriteManager
from mem.welcome.WelcomeManager import WelcomeManager
from mem.root.RootManager import RootManager
from mem.user.ARManager import ARManager
from mem.user.PRManager import PRManager
from mem.pet.PetProfileManager import PetProfileManager

# Service
from mlo.auth.dataModel import DataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.user.AdopterRequestsService import AdopterRequestsService
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mlo.petrecommendation.RecommendedPets import RecommendedPets
from mlo.petsearch.resultsPrioritization import ResultsPrioritization
from mlo.petsearch.searchLogic import SearchLogic
from mlo.petsearch.searchService import SearchService
from mlo.user.FavoritesService import FavoritesService

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
    'recom': 'RecommendedPets',
    'prior': 'ResultsPrioritization',
    'sLogic': 'SearchLogic',
    'search': 'SearchService',
    'favorites': 'FavoritesService',
    'adoReqs': 'AdopterRequestsService'
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
        'pArgs': None,
        'unique': True
    },

    services['auth'] : {
        'class': FireBaseAuthService,
        'deps': None,
        'pArgs': None,
        'unique': True
    },

    services['pet'] : {
        'class': PetService,
        'deps': (databases['pet'],),
        'pArgs': None,
        'unique': True
    },

    services['user'] : {
        'class': UserService,
        'deps': (databases['user'],),
        'pArgs': None,
        'unique': True
    },

    services['recom'] : {
        'class': RecommendedPets,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    services['prior'] : {
        'class': ResultsPrioritization,
        'deps': (services['pet'], services['user'],),
        'pArgs': None,
        'unique': True
    },

    services['sLogic'] : {
        'class': SearchLogic,
        'deps': (services['pet'], services['recom']),
        'pArgs': None,
        'unique': True
    },

    services['search'] : {
        'class': SearchService,
        'deps': (services['prior'], services['sLogic'], services['recom']),
        'pArgs': None,
        'unique': True
    },

    services['favorites'] : {
        'class': FavoritesService,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    services['adoReqs'] : {
        'class': AdopterRequestsService,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    databases['pet'] : {
        'class': FPetDB,
        'deps': None,
        'pArgs': None,
        'unique': True
    },

    databases['user'] : {
        'class': FUserDB,
        'deps': None,
        'pArgs': ('userID',)
    },

    databases['storage'] : {
        'class': FirebaseDB,
        'deps': None,
        'pArgs': None,
        'unique': True
    }, 

    screens['welcome'] : {
        'class': WelcomeManager,
        'deps': None,
        'pArgs': None,
        'unique': True
    },

    screens['login'] : {
        'class': LoginManager,
        'deps': (services['auth'],),
        'pArgs': None,
        'unique': True
    },

    screens['signUp'] : {
        'class': SignUpManager,
        'deps': (services['auth'], services['dataModel'], databases['storage']),
        'pArgs': None,
        'unique': True
    },
    
    screens['root'] : {
        'class': RootManager,
        'deps': (services['user'], services['pet'], services['search']),
        'pArgs': ('orchestrator',)  
    },

    screens['favorites']: {
        'class': FavoriteManager,
        'deps': (services['user'], services['pet'], services['favorites']),
        'pArgs': None,
        'unique': True
    },

    screens['adoRequests']: {
        'class': ARManager,
        'deps': (services['user'], services['pet'], services['adoReqs']),
        'pArgs': None,
        'unique': True
    },

    screens['addPet']: {
        'class': FavoriteManager,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    screens['recRequests']: {
        'class': PRManager,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    screens['petProfile']: {
        'class': PetProfileManager,
        'deps': (services['user'], services['pet'], services['favorites'], services['adoReqs']),
        'pArgs': ('petID',),
        'unique': False
    },


}