from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class ProtectorPetsService:
    def __init__(self, userServ: UserService, petServ:PetService):
        self.userServ = userServ
        self.petServ = petServ
        self.userID = userServ.getUserData()['uid']

    def removePet(self, petID:str):
        uData = self.userServ.getUserData()

        if petID in uData["pets"]:
            pet = self.petServ.getPetData(petID)
            if(pet != {}):
                pet["requestStatus"] = True
                self.petServ.updatePetData(petID, pet)

    
    def petWasAdopted(self, petID:str):
        uData = self.userServ.getUserData()

        if petID in uData["pets"]:
            pet = self.petServ.getPetData(petID)
            if (pet!= {}):
                pet["requestStatus"] = True
                self.petServ.updatePetData(petID, pet)

    def getProtectorPets(self):
        protectorPets = []
        if(self.userServ.getUserType() == "protector"):
            pets = self.userServ.getUserData()["pets"]
            allPets = self.petServ.getAllPets()

            for mypet in pets:
                for pet in allPets:
                    if(pet != {}):
                        if(pet["pid"] == mypet):
                            protectorPets.append(pet)

        return protectorPets
