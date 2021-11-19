import threading
from datetime import datetime, timezone
from typing import List
from mlo.chat.ChatMenssage import ChatMessage
from .ChatDB import ChatDB
from config.firebase import getFirebaseFirestore

class FChatDB(ChatDB):
    __CHAT_COLLECTION = u'Chats'
    __MESSAGE_COLLECTION = u'Messages'
    __callback_done = threading.Event()

    def __init__(self):
        self.__db = getFirebaseFirestore()
        self.__startTime = datetime.now(timezone.utc)
        self.__client = None

    def setClient(self, client) -> None:
        self.__client = client
    
    # Inicia um listener para notificar sobre novas mensagens recebidas
    def startListener(self, chatID:str, userID:str):
        chat = self.__db.collection(self.__CHAT_COLLECTION).document(chatID)
        chat_messages = chat.collection(self.__MESSAGE_COLLECTION)
        chat_messages.where('sentBy',"!=", userID).on_snapshot(
            lambda doc_snapshot, changes, read_time: self.on_snapshot(doc_snapshot, changes, read_time)
        )

    # obter todas as mensagens no chat
    def getChatMessages(self, chatID: str) -> List[ChatMessage]:
        chat = self.__db.collection(self.__CHAT_COLLECTION).document(chatID)
        chat_messages = chat.collection(self.__MESSAGE_COLLECTION)
        messages = chat_messages.order_by('sentAt').get()

        message_list = list()
        for message in messages:
            msg_obj = ChatMessage(**message.to_dict())
            message_list.append(msg_obj)

        return message_list

    # Enviar uma nova mensagem
    def sendChatMessage(self, chatID: str, message: ChatMessage) -> bool:
        chat = self.__db.collection(self.__CHAT_COLLECTION).document(chatID)
        chat_messages = chat.collection(self.__MESSAGE_COLLECTION)
        result = chat_messages.add(message.dict())

        if result == None:
            return False

        return True

    # Manda para o cliente uma nova mensagem recebida
    def notifyReceivedChatMessage(self, message:ChatMessage):
        self.__client.receiveMessage(message)

    # Listener: Observa a coleção do chat no firebase esperando novas mensagens
    def on_snapshot(self, doc_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'ADDED':
                message = change.document.to_dict()
                if message['sentAt'] >= self.__startTime:
                    self.notifyReceivedChatMessage(ChatMessage(**message))
        
        self.__callback_done.set()
