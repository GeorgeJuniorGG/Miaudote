from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty

class MiauLogo(MDFloatLayout):
    screen = ObjectProperty()

    def goBack(self):
        manager = self.screen.manager
        # manager.remove_widget(self.screen)
        manager.goBackward('right')