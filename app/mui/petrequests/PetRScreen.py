from kivymd.uix.screen import MDScreen

class PetRScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.petName = "nome"
        self.petSex = "sexo"
        self.petAge = "0"
        self.petAddr = "Campinas/SP"
        self.petDscp = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

        fav = 1

        if(fav == 0):
            self.petFav = "heart-outline"
        else:
            self.petFav = "heart-remove-outline"

        request = 1

        if(request == 0):
            self.msgRequest = "O protetor de " + self.petName + " não aprovou sua solicitação."
        elif(request == 1):
            self.msgRequest = "O protetor de " + self.petName + " aprovou sua solicitação. Agora você pode conversar com o protetor!"
        else:
            self.msgRequest = "O protetor de " + self.petName + " ainda não visualizou a sua solicitação."

    def favourite(self):
        print("FAVORITO " + str(self.petFav))

    def alert(self):
        print("DENÚNCIA!")

    def open_chat(self):
        print("CHAT")

    def cancel_request(self):
        print("CANCELAR SOLICITAÇÃO")

    def go_backwards(self):
        pass