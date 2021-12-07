from mui.chat.ChatScreen import ChatScreen
from mlo.chat.ChatService import ChatService
from mem.screenmanager.screens import screens

class ChatManager:
    def __init__(self, service:ChatService, chatID:str, userID:str, anUserName:str, anUserImg:str):
        self.service = service
        self.userID = userID
        self.chatID = chatID
        self.anUserName = anUserName
        self.anUserImg = anUserImg
        
        self.screen = ChatScreen(name=screens['chat']+chatID)
        self.screen.controller = self
        self.screen.setAnotherUser(anUserName, anUserImg)
        
        self.service.setClient(self)
        self.__initialMessages()

    # Carregar as mensagens antigas
    def __initialMessages(self):
        msgs = self.service.getMessages()

        for msg in msgs:
            if msg['sentBy'] == self.userID:
                self.screen.createSentBalloon(msg['content'])
            else:
                self.screen.createReceivedBalloon(msg['content'])

    def sendMessage(self, msgContent:str):
        msgData = {
            'content': msgContent,
            'sentBy': self.userID
        }
        self.service.sendMessage(msgData)

    def receiveMessage(self, message:dict):
        self.screen.createReceivedBalloon(message['content'])