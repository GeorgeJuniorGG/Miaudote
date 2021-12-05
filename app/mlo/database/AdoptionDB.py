from abc import ABC, abstractmethod
from mlo.adoption import ARModel

class AdoptionDB(ABC):

    @abstractmethod
    def getAR(self, arID:str) -> ARModel:
        pass

    @abstractmethod
    def createAR(self, petID:str, adpID:str, pttID:str) -> str:
        pass
    
    @abstractmethod
    def deleteAR(self, arID:str, chatID:str) -> bool:
        pass

    @abstractmethod
    def updateARStatus(self, arID:str, status:bool) -> bool:
        pass

    @abstractmethod
    def createChat(self, petID:str, adpID:str, pttID:str) -> str:
        pass

    @abstractmethod
    def includeChat(self, arID:str, chatID:str) -> bool:
        pass