from kivymd.uix.screen import MDScreen

class ProfileScreen(MDScreen):
    
    controller = None

    # Adicionar as Informações do Usuário na tela de perfil
    def getUserData(self):
        userData = self.controller.getUserData()
        userData['user_image'] = 'keanu_reeves.jpg'
        for itemName in self.ids:
            item = self.ids[itemName]
            if itemName == 'user_image':
                item.source = userData['user_image']
            elif itemName in userData.keys():
                item.fieldValue = userData[itemName]

    def changeUserImage(self, imagePath):
        self.ids['user_image'].source = imagePath