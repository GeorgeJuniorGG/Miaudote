from .ChatMenssage import ChatMessage
from mlo.database.ChatDB import ChatDB
from typing import List

class ChatService:

    __chatdb: ChatDB
    __client = None

    def __init__(self, db:ChatDB):
        self.__chatdb = db
        self.__chatdb.setClient(self)
        self.__chatID = None
        self.__userID = None
        
    def setClient(self, client):
        self.__client = client
        self.__userID = client.userID
        self.__chatID = client.chatID
        self.__chatdb.startListener(self.__chatID, self.__userID)

    def sendMessage(self, mData:dict) -> None:
        
        try:
            message = ChatMessage(**mData)
            self.__chatdb.sendChatMessage(self.__chatID, message)
        
        except Exception as e:
            print(e)

    def getMessages(self) -> List[dict]:
        msg_obj_list = self.__chatdb.getChatMessages(self.__chatID)
        msg_list = list(map(lambda x:x.dict(), msg_obj_list))
        return msg_list

    def receiveMessage(self, message:ChatMessage):
        msg_dict = message.dict()
        self.__client.receiveMessage(msg_dict)