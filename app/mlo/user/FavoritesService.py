from mlo.pets.PetService import PetService
from mlo.user.UserModel import AdopterModel
from mlo.user.UserService import UserService

class FavoritesService:
    def __init__(self, userServ: UserService, petServ: PetService):
        self.userServ = userServ
        self.pets = petServ
        self.userType = userServ.getUserType()

    def addPet(self, petID):
        if(self.userType == "adopter"):
            uData = self.userServ.getUserData()

            pet = self.pets.getPetData(petID)

            uData["favorites"].append(pet)

            self.userServ.updateUserData(uData)
    
    def removePet(self, petID):
        if(self.userType == "adopter"):
            uData = self.userServ.getUserData()

            pet = self.pets.getPetData(petID)

            for fav in uData['favorites']:
                if(fav['pid'] == pet['pid']):
                    uData['favorites'].remove(fav)
                    break

            self.userServ.updateUserData(uData)
    
    def getFavorites(self):
        if(self.userType == "adopter"):
            return self.userServ.getUserData()["favorites"]
        
        else:
            return []
    
    def getFavoriteStatus(self, petID):
        if(self.userType == "adopter"):
            uData = self.userServ.getUserData()

            pet = self.pets.getPetData(petID)

            for fav in uData["favorites"]:
                if(fav['pid'] == pet['pid']):
                    return True
            
            return False
        
        else:
            return False