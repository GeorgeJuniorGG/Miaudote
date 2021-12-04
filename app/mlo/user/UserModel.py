from pydantic import BaseModel, Field
from typing import List
from mlo.auth import Address, HomeCharacteristics, Preferences
from mlo.pets.PetModel import PetModel

class UserModel(BaseModel):
    uid: str
    name: str
    cpf: str
    email:str
    address: Address.Address
    userImage:str = Field(default="user_image.jpg")
    adoptationRequests:List[str] = Field(default_factory=list)

class AdopterModel(UserModel):
    favorites: List[PetModel] = Field(default_factory=list)
    homeCharacteristics: HomeCharacteristics.HomeCharacteristics
    preferences: Preferences.UserPreferences

class ProtectorModel(UserModel):
    pets: List[str] = Field(default_factory=list)

