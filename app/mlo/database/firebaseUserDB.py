from .UserDB import UserDB
from config.firebase import getFirebaseFirestore, getFirebase
from mlo.user.UserModel import AdopterModel, ProtectorModel, UserModel

class FUserDB(UserDB):

    __ADOPTER_COLLECTION = u'adopters'
    __PROTECTOR_COLLECTION = u'protectors'
    __IMAGE_STORAGE = u'userImages'
    __user: UserModel
    __isProtector: bool

    def __init__(self, userID) -> None:
        self.__db = getFirebaseFirestore()
        self.__sdb = getFirebase().storage()
        self.__userID = userID
        self.__user = self.__getUser(self.__userID)
        self.__c_a_ref = self.__db.collection(self.__ADOPTER_COLLECTION)
        self.__c_p_ref = self.__db.collection(self.__PROTECTOR_COLLECTION)

    # obtem do firebase os dados sobre um usuário pelo seu id
    def __getUser(self, uID) -> UserModel:
        db = self.__db
        user_doc = db.collection(self.__ADOPTER_COLLECTION)\
                     .document(uID).get()

        user: UserModel = None

        if user_doc.exists:
            user = self.__getAdopterData(user_doc)
            if uID == self.__userID:
                self.__isProtector = False

        else:
            user_doc = db.collection(self.__PROTECTOR_COLLECTION)\
                        .document(uID).get()        
        
            if user_doc.exists:
                user =  self.__getProtectorData(user_doc)
                if uID == self.__userID:
                    self.__isProtector = True
        
        return user

    def __getAdopterData(self, doc) -> AdopterModel:
        userData = doc.to_dict()
        userData['uid'] = self.__userID
        return AdopterModel(**userData)

    def __getProtectorData(self, doc) -> ProtectorModel:
        userData = doc.to_dict()
        userData['uid'] = self.__userID
        return ProtectorModel(**userData)        

    def __updateAdopterData(self, aData:AdopterModel) -> bool:
        db = self.__db
        user_doc_ref = db.collection(self.__ADOPTER_COLLECTION)\
                         .document(self.__userID)        
        result = user_doc_ref.set(aData.dict())
        return result

    def __updateProtectorData(self, pData:ProtectorModel) -> bool:
        db = self.__db
        user_doc_ref = db.collection(self.__PROTECTOR_COLLECTION)\
                        .document(self.__userID)
        result = user_doc_ref.set(pData.dict())
        return result

    def getUserData(self) -> UserModel:
        return self.__getUser(self.__userID)

    # TODO test
    def updateUserData(self, userData: UserModel) -> bool:
        result = None
        if self.__isProtector:
            result = self.__updateProtectorData(userData)
        else:
            result = self.__updateAdopterData(userData)

        #print(result)
        return result

    def getUserID(self) -> str:
        return self.__userID

    # obter os dados de outro usuário
    def getAnotherUserData(self, anUID):
        return self.__getUser(anUID)

    # Atualiza pets do usuário
    def addPetId(self, petId: str) -> None:
        userData = self.getUserData().dict()
        self.__db.collection(self.__PROTECTOR_COLLECTION)\
                                    .document(self.__userID)\
                                    .update({'pets': userData['pets']+[petId]})
    
    def isProtector(self) -> bool:
        return self.__isProtector

    def updateUserImage(self, imagePath:str) -> bool:
        c_ref = self.__c_a_ref
        if self.__isProtector:
            c_ref = self.__c_p_ref
        
        try:
            imageName = self.__user.name.replace(' ', '-') +'-Account-Image.'+imagePath.split('.')[-1]
            storagePath = f'{self.__IMAGE_STORAGE}/{self.__userID}/{imageName}'
            imgStorege = self.__sdb.child(storagePath).put(imagePath)
            imgUrl = self.__sdb.child(imgStorege['name']).get_url(None)
            c_ref.document(self.__userID).update({'userImage': imgUrl})
            return True
        
        except:
            return False