from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

class ProfileScreen(MDScreen):
    
    def getUserData(self):
        userData = {
            'name': 'Nome do Usuário',
            'cpf': 'XXX.XXX.XXX-XX',
            'email': 'Email do Usuário',
            'phone': '(DD) XXXXX-XXXX',
            'user_image': 'keanu_reeves.jpg'
        }
        for itemName in self.ids:
            item = self.ids[itemName]
            if itemName == 'user_image':
                item.source = 'keanu_reeves.jpg'
            elif itemName in userData.keys():
                #print(itemName, userData[itemName])
                item.fieldValue = userData[itemName]


    def go_backward(self):
        pass