# Manager
from mem.login.LoginManager import LoginManager
from mem.signUp.signUpManager import SignUpManager
from mem.user.FavoriteManager import FavoriteManager
from mem.welcome.WelcomeManager import WelcomeManager
from mem.root.RootManager import RootManager
from mem.petSignUp.petSignUpManager import PetSignUpManager
from mem.user.ARManager import ARManager
from mem.user.PRManager import PRManager
from mem.user.PRPManager import PRPManager
from mem.pet.PetProfileManager import PetProfileManager
from mem.filechooser.FileManager import FileManager
from mem.chat.ChatManager import ChatManager
from mem.user.ProtectorPetsManager import ProtectorPetsManager

# Service
from mlo.auth.dataModel import DataModel
from mlo.database.firebaseAdoptionDB import FBAdoptionDB
from mlo.pets.PetDataModel import PetDataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from mlo.user.AdopterRequestsService import AdopterRequestsService
from mlo.user.UserService import UserService
from mlo.pets.PetService import PetService
from mlo.petrecommendation.RecommendedPets import RecommendedPets
from mlo.petsearch.resultsPrioritization import ResultsPrioritization
from mlo.petsearch.searchLogic import SearchLogic
from mlo.petsearch.searchService import SearchService
from mlo.user.FavoritesService import FavoritesService
from mlo.adoption.AdoptionService import AdoptionService
from mlo.chat.ChatService import ChatService
from mlo.user.ProtectorPetsService import ProtectorPetsService

# Database
from mlo.storage.firebaseDB import FirebaseDB
from mlo.database.firebaseUserDB import FUserDB
from mlo.database.firebasePetDB import FPetDB
from mlo.database.firebaseChatDB import FChatDB

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
    'search': 'SearchService',
    'favorites': 'FavoritesService',
    'adoReqs': 'AdopterRequestsService',
    'adoption': 'AdoptionService',
    'chat': 'ChatService',
    'myPets': 'ProtectorPetsService'
}

databases = {
    'user': 'FUserDB',
    'storage': 'FirebaseDB',
    'pet': 'FPetDB',
    'adoptation': 'FBAdoptionDB',
    'chat': 'FChatDB'
}

recipes = {

    services['dataModel'] : {
        'class': DataModel,
        'deps': None,
        'pArgs': None,
        'unique': True
    },

    services['petDataModel'] : {
        'class': PetDataModel,
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

    services['adoption'] : {
        'class': AdoptionService,
        'deps': (databases['adoptation'], services['user'], services['pet']),
        'pArgs': None,
        'unique': True    
    },

    services['myPets'] : {
        'class': ProtectorPetsService,
        'deps': (services['user'], services['pet']),
        'pArgs': None,
        'unique': True
    },

    services['chat'] : {
        'class': ChatService,
        'deps': (databases['chat'],),
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
        'pArgs': ('userID',),
        'unique': True
    },

    databases['storage'] : {
        'class': FirebaseDB,
        'deps': None,
        'pArgs': None,
        'unique': True
    }, 

    databases['adoptation'] : {
        'class': FBAdoptionDB,
        'deps': None,
        'pArgs': None,
        'unique': True
    },

    databases['chat'] : {
        'class': FChatDB,
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
        'pArgs': ('orchestrator',),
        'unique': True
    },

    screens['petSignUp'] : {
        'class': PetSignUpManager,
        'deps': (databases['pet'],services['petDataModel'],services['user']),
        'pArgs': None,
        'unique': True
    },

    screens['favorites'] : {
        'class': FavoriteManager,
        'deps': (services['user'], services['pet'], services['favorites']),
        'pArgs': None,
        'unique': True
    },

    screens['adoRequests'] : {
        'class': ARManager,
        'deps': (services['adoption'],),
        'pArgs': None,
        'unique': True
    },

    screens['recRequests'] : {
        'class': PRManager,
        'deps': (services['adoption'],),
        'pArgs': None,
        'unique': True
    },

    screens['petProfile'] : {
        'class': PetProfileManager,
        'deps': (services['pet'], services['favorites'], services['adoption']),
        'pArgs': ('petID',),
        'unique': False
    },

    screens['fileChooser'] : {
        'class': FileManager,
        'deps': None,
        'pArgs': ('client',),
        'unique': True
    },

    screens['requesterProfile'] : {
        'class': PRPManager,
        'deps': (services['adoption'],),
        'pArgs': ('arID',),
        'unique': True        
    },

    screens['chat'] : {
        'class': ChatManager,
        'deps': (services['chat'],),
        'pArgs': ('chatID','userID','anUserName', 'anUserImg'),
        'unique': True        
    },

    screens['myPets'] : {
        'class': ProtectorPetsManager,
        'deps': (services['myPets'],),
        'pArgs': None,
        'unique': True        
    }

}