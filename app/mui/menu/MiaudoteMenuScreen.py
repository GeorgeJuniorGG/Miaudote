from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from .components.MenuItem import MenuItem
from kivy.properties import ObjectProperty
from mem.screenmanager.screens import screens

class MiaudoteMenuScreen(MDScreen):
    # Menu
    menu = ObjectProperty(MDGridLayout)
    # Item das solicitações de adoção (Adotante)
    adoptRequests = ObjectProperty(MenuItem)
    # Item para a inclusão de Pets (Protetos)
    addPet = ObjectProperty(MenuItem)
    # Item para as solicitações de adoção recebidas (Protetor)
    receivedRequests = ObjectProperty(MenuItem)
    # Item para os Pets favoritados (Adotante)
    favorites = ObjectProperty(MenuItem)

    controller = None

    # Facilita a mudança de telas no menu (Melhorar se possível)
    __screens = {}
    
    def bindAdopterScreens(self):
        self.__screens = {
        screens['favorites']: self.favorites,
        screens['adoRequests']: self.adoptRequests
    }
        self.ids.menu.remove_widget(self.ids.received_requests)   
        self.ids.menu.remove_widget(self.ids.add_pet)
    
    def bindProtectorScreens(self):
        self.__screens = {
        screens['petSignUp']: self.addPet,
        screens['recRequests']: self.receivedRequests
    }
        self.ids.menu.remove_widget(self.ids.adopt_requests)   
        self.ids.menu.remove_widget(self.ids.favorites)

    # Chamado quando há uma mudança de tela
    def callScreen(self, item:MenuItem):
        for screenName in self.__screens.keys():
            if self.__screens[screenName] == item:
                return self.controller.callChangeScreen(screenName)
