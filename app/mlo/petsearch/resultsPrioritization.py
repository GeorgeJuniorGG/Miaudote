from datetime import datetime
from typing import List
from pytz import utc

from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class ResultsPrioritization:
    def __init__(self, petService: PetService, userService: UserService):        
        self.pets = petService.getAllPets()
        self.user = userService.getUserData()
        self.userType = userService.getUserType()
    
    def getResults(self, searchResults: List):
        self.searchResults = searchResults

        if self.userType == "adopter":
            results = [[], [], []]  # Primeiro: resultados finais, Segundo: localizacoes, Terceiro: data de insercao

            self.getLocationPriority(results)
            self.getOldestPriority(results)
            self.getNonRequestedPriority(results)
            
            return results[0]
        
        else:
            return self.getProtectorResults(searchResults)

    def getProtectorResults(self, searchResults: List):
        results = []

        for result in searchResults:
            for pet in self.pets:
                if pet["pid"] == result:
                    results.append(pet)
        
        return results

    def getLocationPriority(self, results: List):
        locations = {}

        for result in self.searchResults:
            for pet in self.pets:
                if pet["pid"] == result:
                    results[1].append(int(pet["localization"]))
                    
        for i in range(len(results[1])):
            locations[str(results[1][i]) + str(i)] = abs(results[1][i] - self.user["address"]["CEP"])

        locations = {k: v for k, v in sorted(locations.items(), key=lambda item: item[1])}

        results[1] = [*locations]

        for i in range(len(results[1])):
            results[1][i] = int(str(results[1][i])[:-1])

        for location in results[1]:
            for pet in self.pets:
                if(pet["pid"] in self.searchResults):
                    if int(pet["localization"]) == location and pet not in results[0]:
                        results[0].append(pet)

    def getOldestPriority(self, results: List):
        for i in range(len(results[0])):
            results[2].append(results[0][i]["createAt"])
        
        for i in range(len(results[0]) - 1):
            if(results[1][i] - results[1][i + 1] < 50000):

                first = results[0][i]["createAt"]
                second = results[0][i + 1]["createAt"]

                if (second < first):
                    aux1 = results[0][i]
                    aux2 = results[1][i]
                    aux3 = results[2][i]

                    results[0][i] = results[0][i + 1]
                    results[1][i] = results[1][i + 1]
                    results[2][i] = results[2][i + 1]

                    results[0][i + 1] = aux1
                    results[1][i + 1] = aux2
                    results[2][i + 1] = aux3

    def getNonRequestedPriority(self, results: List):
        for i in range(len(results[0]) - 1):
            try:
                dueDate = datetime(day = results[2][i].day + 8, year = results[2][i].year, month = results[2][i].month)
            except:
                dueDate = datetime(day = (results[2][i].day + 8)%30, year = results[2][i].year, month = results[2][i].month + 1)

            dueDate = utc.localize(dueDate)

            if(results[1][i] - results[1][i + 1] < 50000 and results[2][i + 1] < dueDate):

                first = results[0][i]["requestStatus"]
                second = results[0][i + 1]["requestStatus"]

                if (first == False and second == True):
                    aux1 = results[0][i]
                    aux2 = results[1][i]
                    aux3 = results[2][i]

                    results[0][i] = results[0][i + 1]
                    results[1][i] = results[1][i + 1]
                    results[2][i] = results[2][i + 1]

                    results[0][i + 1] = aux1
                    results[1][i + 1] = aux2
                    results[2][i + 1] = aux3