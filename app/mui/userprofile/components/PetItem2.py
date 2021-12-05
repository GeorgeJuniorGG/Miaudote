from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from functools import partial
from mui.protectorrequests.components.ARItem import RemoveButton

from kivy.properties import (
    StringProperty,
    ObjectProperty
)

from kivy.clock import Clock


class PetLabel2(MDLabel):
    def __init__(self, charName, **kwargs):
        super().__init__(**kwargs)
        self.text = charName
        self.font_size = '10sp'
        self.halign = 'center'
        self.pos_hint = {'center_y': 0.5}


class PetItem2(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
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
    petCharsBox = ObjectProperty(MDBoxLayout)
    # Label com a Descrição do Pet
    petDLabel = ObjectProperty(MDLabel)
    # Label com o Nome do Pet
    petNLabel = ObjectProperty(MDLabel)
    # FloatLayout com a Imagem do pet
    petImage = ObjectProperty(MDFloatLayout)
    # MDIconButton para exclusão do item
    buttonsContainer = ObjectProperty()

    def __init__(self, data:dict, screen, **kwargs):
        super().__init__(**kwargs)

        self.screen = screen
        self.petImageSource = data['imageSource']
        self.petName = data['petName']
        self.petDescription = data['petDecription']
        self.petID = data['pid']
        #if data['arStatus'] == True:
        #    Clock.schedule_once(lambda x: self.insertButtons(ChatButton()))

        Clock.schedule_once( lambda x: self.insertButtons(
                RemoveButton(on_release=partial(self.screen.remove_item_dialog, data['pid'])))
        )

        labels = data['petChars']
        Clock.schedule_once(lambda x: self.insertLabels(labels))

    # inserir os chips com as caracteristicas dos animais
    def insertLabels(self, labels):
        
        for i in range(len(labels)):
            petChar = PetLabel2(labels[i])
            self.petCharsBox.ids[f'label{i}'] = petChar
            self.petCharsBox.add_widget(petChar)

    def insertButtons(self, button):
        self.buttonsContainer.add_widget(button)

    def openPetProfile(self):
        self.screen.openPetProfile(self.petID)