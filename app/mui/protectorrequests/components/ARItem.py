from functools import partial
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

from kivy.clock import Clock


class ARLabel(MDLabel):
    def __init__(self, charName, **kwargs):
        super().__init__(**kwargs)
        self.text = charName
        self.font_size = '10sp'
        self.halign = 'center'
        self.pos_hint = {'center_y': 0.5}

class ChatButton(MDIconButton):
    pass

class RemoveButton(MDIconButton):
    pass

class ARItem(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    # indicar o local da imagem
    petImageSource = StringProperty()
    # adicionar o nome do Pet
    petName = StringProperty()
    # adicionar descrição do Pet
    petDescription = StringProperty()
    # adicionar o ID do pet
    petID = StringProperty()

    # FloatLayout com o conteudo textual sobre o Pet
    petContent = ObjectProperty(MDFloatLayout)
    # BoxLayout com os Chips das Características do Pet
    petCharsBox = ObjectProperty(MDGridLayout)
    # Label com a Descrição do Pet
    petDLabel = ObjectProperty(MDLabel)
    # Label com o Nome do Pet
    petNLabel = ObjectProperty(MDLabel)
    # FloatLayout com a Imagem do pet
    petImage = ObjectProperty(MDFloatLayout)
    # MDIconButton para exclusão do item
    buttonsContainer = ObjectProperty(MDFloatLayout)

    def __init__(self, data:dict, screen, **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.petImageSource = data['imageSource']
        self.petName = data['petName']
        self.petDescription = data['description']
        self.petID = data['pid']
        self.arID = data['arID']

        if data['arStatus'] == True:
            Clock.schedule_once(lambda x: self.insertButtons(ChatButton(
                on_release=partial(self.screen.openChat, data['arID'])
            )))

        Clock.schedule_once(lambda x: self.insertButtons(
            RemoveButton(
                on_release=partial(self.screen.remove_item_dialog, data['arID'])
            ))
        )

        labels = data['petChars']
        Clock.schedule_once(lambda x: self.insertLabels(labels))

    # inserir os chips com as caracteristicas dos animais
    def insertLabels(self, labels):
        
        for i in range(len(labels)):
            petChar = ARLabel(labels[i])
            self.petCharsBox.ids[f'label{i}'] = petChar
            self.petCharsBox.add_widget(petChar)

    def insertButtons(self, button):
        self.buttonsContainer.add_widget(button)

    def openRequest(self):
        self.screen.openRequest(self.arID)