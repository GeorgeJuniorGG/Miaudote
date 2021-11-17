from mui.chat.ChatScreen import ChatScreen
from mlo.chat.ChatService import ChatService

class ChatManager:
    def __init__(self, screen:ChatScreen, service:ChatService, userID:str):
        self.screen = screen
        self.userID = userID
        self.screen.controller = self
        self.service = service
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