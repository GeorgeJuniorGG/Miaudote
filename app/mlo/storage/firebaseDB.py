from .storageService import StoregeService
from mlo.auth.basicUserdata import BasicUSerData
from mlo.auth.Address import Address
from mlo.auth.Preferences import UserPreferences
from mlo.auth.HomeCharacteristics import HomeCharacteristics
from config.firebase import getFirebaseFirestore
    
db = getFirebaseFirestore()

class FirebaseDB(StoregeService):
    
    def createProtector(currentUser:str, userData:BasicUSerData)->None:
        docRef = db.collection(u'protectors').document(currentUser)
        docRef.set(userData.dict())

    def createAdopter(currentUser:str, userData:BasicUSerData)->None:
        docRef = db.collection(u'adopters').document(currentUser)
        docRef.set(userData.dict())

    def storeAddress(self, collection:str,currentUser:str, userAddress: Address)->bool:
        docRef = db.collection(collection).document(currentUser)
        if(docRef.update(userAddress.getAdressForFireStore())):
            return True
        return False

    def storePreferences(self, currentUser:str, userPreferences:UserPreferences)->bool:
        docRef = db.collection(u'adopters').document(currentUser)
        if(docRef.update(userPreferences.getPreferencesForFireStore())):
            return True
        return False

    def storeHomeCharacteristics(self, currentUser:str, userHomeCharacteristics: HomeCharacteristics)->bool:
        docRef = db.collection(u'adopters').document(currentUser)
        if(docRef.update(userHomeCharacteristics.getHomeCharacteristicsForFireStore())):
            return True
        return False