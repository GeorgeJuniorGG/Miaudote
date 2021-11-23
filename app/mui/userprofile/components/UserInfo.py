from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import (
    StringProperty,
    ObjectProperty
)

class UserInfo(MDFloatLayout):
    fieldName = StringProperty()
    fieldValue = StringProperty()
