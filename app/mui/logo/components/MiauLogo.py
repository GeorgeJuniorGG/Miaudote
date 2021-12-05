from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from mem.screenmanager.screens import screens

class MiauLogo(MDFloatLayout):
    screen = ObjectProperty()

    def goBack(self):
        manager = self.screen.manager
        # manager.remove_widget(self.screen)
        if screens['requesterProfile'] in self.screen.name:
            return manager.goBackward('right')
        
        return manager.goHome()