from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

class MenuItem(RectangularRippleBehavior, ButtonBehavior, MDFloatLayout):
    text = StringProperty('Item')