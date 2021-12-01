from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class AdopterRequestsService:
    def __init__(self, userServ: UserService, petServ:PetService):
        self.userServ = userServ
        self.petServ = petServ
        self.userID = userServ.getUserData()['uid']

    def addRequest(self, petID:str):
        pet = self.petServ.getPetData(petID)

        if (self.userID not in pet["requestQueue"]):
            pet["requestQueue"].append(self.userID)

        self.petServ.updatePetData(petID, pet)

    def removeRequest(self, petID:str):
        pet = self.petServ.getPetData(petID)
        
        pet["requestQueue"].remove(self.userID)

        self.petServ.updatePetData(petID, pet)

    def getRequests(self):
        userRequests = []

        pets = self.petServ.getAllPets()

        for pet in pets:
            if(self.userID in pet["requestQueue"]):
                userRequests.append(pet)

        return userRequests