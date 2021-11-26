from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class RecommendedPets():
    def __init__(self, user: UserService, pets: PetService):
        self.user = user.getUserData()
        self.pets = pets.getAllPets()

    def getRecommended(self):
        results = []
        characteristicsFilters = self.getCharacteristicsFilters()
        sizeFilters = self.getSizeFilters()
        animalFilters = self.getAnimalFilters()

        for pet in self.pets:
            if(pet["size"] in sizeFilters):

                if(pet["type"] in animalFilters and pet["pid"] not in results):
                    if(pet["Activities"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])
                    if(pet["Age"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])
                    if(pet["Personality"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])

                    if(len(characteristicsFilters) == 0 and pet["pid"] not in results):
                        results.append(pet["pid"])

                if(pet["type"] != "cachorro" and pet["type"] != "gato" and "outro" in animalFilters and pet["pid"] not in results):
                    if(pet["Activities"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])
                    if(pet["Age"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])
                    if(pet["Personality"] in characteristicsFilters and pet["pid"] not in results):
                        results.append(pet["pid"])

                    if(len(characteristicsFilters) == 0 and pet["pid"] not in results):
                        results.append(pet["pid"])     
        if (len(results) == 0):
            results = [pet["pid"] for pet in self.pets]

        return results

    def getCharacteristicsFilters(self):
        characteristicsFilters = []

        if (self.user["preferences"]["activitiesCharacteristics"] != "Não possuo preferência"):
            characteristicsFilters.append(self.user["preferences"]["activitiesCharacteristics"])

        if (self.user["preferences"]["ageCharacteristics"] != "Não possuo preferência"):
            characteristicsFilters.append(self.user["preferences"]["ageCharacteristics"])

        if (self.user["preferences"]["personalityCharacteristics"] != "Não possuo preferência"):
            characteristicsFilters.append(self.user["preferences"]["personalityCharacteristics"])

        return characteristicsFilters

    def getSizeFilters(self):
        sizeFilters = []

        houseType = self.user["homeCharacteristics"]["houseType"]
        availableSpace = self.user["homeCharacteristics"]["availableSpace"]
        openArea = self.user["homeCharacteristics"]["openArea"]
        favoriteSize = self.user["preferences"]["favoriteSize"]

        if (openArea and (houseType == "Chácara" or houseType == "Casa")):
            if(houseType == "Chácara" or availableSpace == "Mais de 100 m²"):
                sizeFilters.append("grande")
            elif (availableSpace == "De 50m² a 100 m²"):
                sizeFilters.append("grande")
                sizeFilters.append("médio")
            else:
                sizeFilters.append("médio")
    
        elif (openArea and availableSpace == "De 25m² a 50 m²"):
            sizeFilters.append("pequeno")
            sizeFilters.append("médio")
        
        elif (not openArea or houseType == "Apartamento" or availableSpace == "Até 25 m²"):
            sizeFilters.append("pequeno")

        else:
            sizeFilters.append("médio")

        if (favoriteSize != "Não possuo preferência"):
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

        elif (favoriteAnimal == "Não possuo preferência"):
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