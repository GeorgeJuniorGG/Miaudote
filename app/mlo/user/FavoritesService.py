from mlo.pets.PetService import PetService
from mlo.user.UserModel import AdopterModel
from mlo.user.UserService import UserService

class FavoritesService:
    def __init__(self, userServ: UserService, petServ: PetService):
        self.userServ = userServ
        self.pets = petServ

    def addPet(self, petID):
        uData = self.userServ.getUserData()

        pet = self.pets.getPetData(petID)

        uData["favorites"].append(pet)

        self.userServ.updateUserData(uData)
    
    def removePet(self, petID):
        uData = self.userServ.getUserData()

        pet = self.pets.getPetData(petID)

        for fav in uData['favorites']:
            if(fav['pid'] == pet['pid']):
                uData['favorites'].remove(fav)
                break

        self.userServ.updateUserData(uData)
    
    def getFavorites(self):

        #if(isinstance(self.userServ.getUserData(), AdopterModel)):
        return self.userServ.getUserData()["favorites"]
    
    def getFavoriteStatus(self, petID):
        uData = self.userServ.getUserData()

        pet = self.pets.getPetData(petID)

        for fav in uData["favorites"]:
            if(fav['pid'] == pet['pid']):
                return True
        
        return False