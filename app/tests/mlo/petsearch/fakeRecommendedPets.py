from mlo.petrecommendation.RecommendedPets import RecommendedPets
from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService
from mlo.database.firebasePetDB import FPetDB
from mlo.database.firebaseUserDB import FUserDB

class FakeRecommendedPets(RecommendedPets):

    def __init__(self):
        user = UserService(FUserDB("yrTvyZUTHnchSKRZdPap1GmFPru2"))
        pets = PetService(FPetDB())
        super().__init__(user, pets)

    def getRecommended(self):
        return "recomendados"