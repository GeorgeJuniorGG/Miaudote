from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class RecommendedPets():
    def __init__(self, user: UserService, pets: PetService):
        self.user = user.getUserData()
        self.pets = pets
        self.userType = user.getUserType()

    def getRecommended(self):
        results = []
        pets = self.pets.getAllPets()

        if self.userType == "adopter":
            characteristicsFilters = self.getCharacteristicsFilters()
            sizeFilters = self.getSizeFilters()
            animalFilters = self.getAnimalFilters()

            for pet in pets:
                if(pet["size"].lower() in sizeFilters):

                    if(pet["type"].lower() in animalFilters and pet["pid"] not in results):
                        if(pet["Activities"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])
                        if(pet["Age"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])
                        if(pet["Personality"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])

                        if(len(characteristicsFilters) == 0 and pet["pid"] not in results):
                            results.append(pet["pid"])

                    if(pet["type"].lower() != "cachorro" and pet["type"].lower() != "gato" and "outro" in animalFilters and pet["pid"] not in results):
                        if(pet["Activities"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])
                        if(pet["Age"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])
                        if(pet["Personality"] in characteristicsFilters and pet["pid"] not in results):
                            results.append(pet["pid"])

                        if(len(characteristicsFilters) == 0 and pet["pid"] not in results):
                            results.append(pet["pid"])
                            
            if (len(results) == 0):
                results = [pet["pid"] for pet in pets]
        
        else:
            results = [pet["pid"] for pet in pets]

        return results

    def getCharacteristicsFilters(self):
        characteristicsFilters = []

        if (self.user["preferences"]["activitiesCharacteristics"] != "N??o possuo prefer??ncia"):
            characteristicsFilters.append(self.user["preferences"]["activitiesCharacteristics"])

        if (self.user["preferences"]["ageCharacteristics"] != "N??o possuo prefer??ncia"):
            characteristicsFilters.append(self.user["preferences"]["ageCharacteristics"])

        if (self.user["preferences"]["personalityCharacteristics"] != "N??o possuo prefer??ncia"):
            characteristicsFilters.append(self.user["preferences"]["personalityCharacteristics"])

        return characteristicsFilters

    def getSizeFilters(self):
        sizeFilters = []

        houseType = self.user["homeCharacteristics"]["houseType"]
        availableSpace = self.user["homeCharacteristics"]["availableSpace"]
        openArea = self.user["homeCharacteristics"]["openArea"]
        favoriteSize = self.user["preferences"]["favoriteSize"]

        if (openArea and (houseType == "Ch??cara" or houseType == "Casa")):
            if(houseType == "Ch??cara" or availableSpace == "Mais de 100 m??"):
                sizeFilters.append("grande")
            elif (availableSpace == "De 50m?? a 100 m??"):
                sizeFilters.append("grande")
                sizeFilters.append("m??dio")
            else:
                sizeFilters.append("m??dio")
    
        elif (openArea and availableSpace == "De 25m?? a 50 m??"):
            sizeFilters.append("pequeno")
            sizeFilters.append("m??dio")
        
        elif (not openArea or houseType == "Apartamento" or availableSpace == "At?? 25 m??"):
            sizeFilters.append("pequeno")

        else:
            sizeFilters.append("m??dio")

        if (favoriteSize != "N??o possuo prefer??ncia"):
            favoriteSize = favoriteSize.lower()
            if (favoriteSize not in sizeFilters):
                sizeFilters.append(favoriteSize)
        
        return sizeFilters
    
    def getAnimalFilters(self):
        animalFilters = []

        favoriteAnimal = self.user["preferences"]["favoriteAnimal"]
        currentAnimal = self.user["preferences"]["haveAnimal"]

        if (favoriteAnimal == "Cachorro(s)"):
            animalFilters.append("cachorro")
        
        elif (favoriteAnimal == "Gato(s)"):
            animalFilters.append("gato")
        
        elif (favoriteAnimal == "Cachorros(s) e Gato(s)"):
            animalFilters.append("gato")
            animalFilters.append("cachorro")

        elif (favoriteAnimal == "Outros"):
            animalFilters.append("outro")

        elif (favoriteAnimal == "N??o possuo prefer??ncia"):
            animalFilters.append("gato")
            animalFilters.append("cachorro")
            animalFilters.append("outro")
        
        if (currentAnimal == "Cachorros(s) e Gato(s)"):
            if ("gato" not in animalFilters):
                animalFilters.append("gato")
            if ("cachorro" not in animalFilters):
                animalFilters.append("cachorro")

        elif (currentAnimal == "Cachorro(s)" and "cachorro" not in animalFilters):
            animalFilters.append("cachorro")

        elif (currentAnimal == "Gato(s)" and "gato" not in animalFilters):
            animalFilters.append("gato")
        
        elif (currentAnimal == "Outros" and "outro" not in animalFilters):
            animalFilters.append("outro")
        
        return animalFilters