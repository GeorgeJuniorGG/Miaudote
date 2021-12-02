from kivymd.uix.screen import MDScreen

class ProfileScreen(MDScreen):
    
    controller = None

    # Adicionar as Informações do Usuário na tela de perfil
    def getUserData(self):
        userData = self.controller.getUserData()
        #userData['userImage'] = 'keanu_reeves.jpg'
        for itemName in self.ids:
            item = self.ids[itemName]
            if itemName == 'userImage':
                item.source = userData['userImage']
            elif itemName in userData.keys():
                item.fieldValue = userData[itemName]

    def changeUserImage(self, imagePath):
        oldImage = self.ids['userImage'].source
        self.ids['userImage'].source = imagePath
        return oldImage