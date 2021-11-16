from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from .components.MenuItem import MenuItem
from kivy.properties import ObjectProperty
from mui.userprofile.FavoritesScreen import FavoritesScreen

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

    def open_favorites(self, app):
        app.change_screen(FavoritesScreen(name='Favorites'))
