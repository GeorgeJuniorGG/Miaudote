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
    
class AdopterModel(UserModel):
    favorites: List[PetModel] = Field(default_factory=list)
    homeCharacteristics: HomeCharacteristics.HomeCharacteristics
    preferences: Preferences.UserPreferences

class ProtectorModel(UserModel):
    pets: List[PetModel] = Field(default_factory=list)

