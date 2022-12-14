from abc import ABC, abstractmethod
from mlo.user.UserModel import UserModel

class UserDB(ABC):

    @abstractmethod
    def getUserData(self) -> UserModel:
        pass

    @abstractmethod
    def updateUserData(self, userData:UserModel) -> bool:
        pass

    @abstractmethod
    def getUserID(self) -> str:
        pass

    @abstractmethod
    def getAnotherUserData(self, anUID):
        pass

    @abstractmethod
    def addPetId(self, petId: str) -> None:
        pass
    
    @abstractmethod
    def isProtector(self) -> bool:
        pass

    @abstractmethod
    def updateUserImage(self, imagePath:str) -> bool:
        pass

    @abstractmethod
    def insertAR(self, userID:str, arID:str) -> bool:
        pass

    @abstractmethod
    def deleteAR(self, userID:str, arID:str) -> bool:
        pass    