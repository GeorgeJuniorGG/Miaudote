from .UserDB import UserDB
from config.firebase import getFirebaseFirestore
from mlo.user.UserModel import AdopterModel, ProtectorModel, UserModel

class FUserDB(UserDB):

    __ADOPTER_COLLECTION = u'adopters'
    __PROTECTOR_COLLECTION = u'protectors'
    __user: UserModel
    __isProtector: bool

    def __init__(self, userID) -> None:
        self.__db = getFirebaseFirestore()
        self.__userID = userID
        self.__user = self.__getUser(self.__userID)

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
        return self.__user

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