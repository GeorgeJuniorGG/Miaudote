from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.behaviors.elevation import FakeRectangularElevationBehavior
from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

from mui.ColorTheme import Color

class MiaudoteLogo(MDFloatLayout):
    ...

class MiaudoteNavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    cor = Color()
    tabManager = ObjectProperty(ScreenManager)
    buttonContainer = ObjectProperty(MDGridLayout)

    def home(self):
        homeItem = self.ids.home_icon
        homeItem.ids.icon.text_color = self.cor.azulEscuro()
        homeItem.ids.label.text_color = self.cor.azulEscuro()

    def changeTab(self, tabName:str, transition):
        self.tabManager.transition = SlideTransition()
        if self.tabManager.current == 'Menu':
            self.tabManager.transition.direction = 'down'
        else:
            self.tabManager.transition.direction = transition
        self.tabManager.current = tabName

    def changeButtonColor(self, selItem):
        for itemName in self.ids:
            item = self.ids[itemName]
            if item != self.buttonContainer:
                if item != selItem:
                    item.ids.label.text_color = self.cor.branco()
                    item.ids.icon.text_color = self.cor.branco()
        
        selItem.ids.icon.text_color = self.cor.azulEscuro()
        selItem.ids.label.text_color = self.cor.azulEscuro()

class NavBarItem(ButtonBehavior, MDFloatLayout):
    icon = StringProperty()
    text = StringProperty()

class ManagerRootTabs(ScreenManager):
    tabPanel = ObjectProperty(MiaudoteNavBar)

class RootScreen(MDScreen):
    tabManager = ObjectProperty(ManagerRootTabs)
    homeScreen = ObjectProperty()
    menuScreen = ObjectProperty()
    profileScreen = ObjectProperty()
    controller = None