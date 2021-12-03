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

            uData["favorites"].append(petID)

            self.userServ.updateUserData(uData)
    
    def removePet(self, petID):
        if(self.userType == "adopter"):
            uData = self.userServ.getUserData()

            uData['favorites'].remove(petID)

            self.userServ.updateUserData(uData)
    
    def getFavorites(self):
        favorites = []

        if(self.userType == "adopter"):
            for fav in self.userServ.getUserData()["favorites"]:
                favorites.append(self.pets.getPetData(fav))
        
        return favorites
    
    def getFavoriteStatus(self, petID):
        if(self.userType == "adopter"):
            uData = self.userServ.getUserData()

            if petID in uData["favorites"]:
                return True
            
            return False
        
        else:
            return False