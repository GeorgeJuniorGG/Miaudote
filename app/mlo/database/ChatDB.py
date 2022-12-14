from abc import ABC, abstractmethod
from mlo.chat.ChatMenssage import ChatMessage
from typing import List

class ChatDB(ABC):

    @abstractmethod
    def setClient(self, client)-> None:
        pass
    
    @abstractmethod
    def startListener(self, chatID:str, userID:str):
        pass
        
    @abstractmethod
    def getChatMessages(self, chatID: str) -> List[ChatMessage]:
        pass
    
    @abstractmethod
    def sendChatMessage(self, chatID: str, message:ChatMessage) -> bool:
        pass

    @abstractmethod
    def notifyReceivedChatMessage(self, message:ChatMessage):
        pass