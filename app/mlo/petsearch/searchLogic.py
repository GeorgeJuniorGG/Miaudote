from typing import List
from mlo.petrecommendation.RecommendedPets import RecommendedPets
from mlo.pets.PetService import PetService

class SearchLogic:

    def __init__(self, petService:PetService, recommendations: RecommendedPets):
        self.recommendations = recommendations
        self.__petService = petService
        self.dictPets = self.__petService.getAllPets()
    
    def getResults(self, words: List):

        self.words = words

        for i in range(len(self.words)):
            self.words[i] = self.words[i].lower()

        if(len(self.words) == 1 and self.words[0] == ""):
            return self.recommendations.getRecommended()

        elif(len(self.words) > 10):
            return "Limite de palavras ultrapassado"
        
        elif(self.getUserFilters() == [[],[],[],[]]):
            return "Erro de busca (palavras não correspondem a filtros)"

        elif (self.getSearchResults() == []):
            return "Não encontrou resultados"

        return self.getSearchResults()
    
    def getUserFilters(self):
        userColorFilters = []
        userSizeFilters = []
        userTypeFilters = []
        userGenderFilters = []

        availableFilters = self.getAvailableFilters()
        availableColors = availableFilters[0]
        availableSizes = availableFilters[1]
        availableTypes = availableFilters[2]
        availableGenders = availableFilters[3]

        aliases = self.getAliases()
        
        for word in self.words:
            for color in availableColors:
                if word in color:
                    userColorFilters.append(word)
            for size in availableSizes:
                if word in size:
                    userSizeFilters.append(word)
            for type in availableTypes:
                if word in type:
                    userTypeFilters.append(word)
            for gender in availableGenders:
                if word in gender:
                    userGenderFilters.append(word)

        for alias in aliases:
            for color in availableColors:
                if alias in color:
                    userColorFilters.append(alias)
            for size in availableSizes:
                if alias in size:
                    userSizeFilters.append(alias)
            for type in availableTypes:
                if alias in type:
                    userTypeFilters.append(alias)
            for gender in availableGenders:
                if alias in gender:
                    userGenderFilters.append(alias)

        userFilters = [userColorFilters, userSizeFilters, userTypeFilters, userGenderFilters]

        return userFilters
    
    def getAvailableFilters(self):
        colors = []
        sizes = []
        types = []
        genders = []

        docs = self.dictPets
        for doc in docs:

            if(doc['type'] not in types):
                types.append(doc["type"])

            if(doc["color"] not in colors):
                colors.append(doc["color"])

            if(doc["size"] not in sizes):
                sizes.append(doc['size'])
            
            if(doc['sex'] not in genders):
                genders.append(doc['sex']) 
        
        availableFilters = [colors, sizes, types, genders]
        return availableFilters
    
    def getSearchResults(self):
        searchResults = []
        searchColorResults = []
        searchSizeResults = []
        searchTypeResults = []
        searchGenderResults = []
        finalResults = []

        filters = self.getUserFilters()

        docs = self.dictPets
        for doc in docs:
            for colorFilter in filters[0]:
                if(colorFilter in doc["color"] and doc["pid"] not in searchColorResults):
                    searchColorResults.append(doc["pid"])
            for sizeFilter in filters[1]:
                if (sizeFilter in doc["size"] and doc["pid"] not in searchSizeResults):
                    searchSizeResults.append(doc["pid"])
            for typeFilter in filters[2]:
                if (typeFilter in doc["type"] and doc["pid"] not in searchTypeResults):
                    searchTypeResults.append(doc["pid"])
            for genderFilter in filters[3]:
                if (genderFilter in doc["sex"] and doc["pid"] not in searchGenderResults):
                    searchGenderResults.append(doc["pid"])
        
        if(searchColorResults != []):
            searchResults.append(searchColorResults)
        if(searchSizeResults != []):
            searchResults.append(searchSizeResults)
        if(searchTypeResults != []):
            searchResults.append(searchTypeResults)
        if (searchGenderResults != []):
            searchResults.append(searchGenderResults)

        allResults = searchColorResults + searchSizeResults + searchTypeResults + searchGenderResults

        for result in allResults:
            belongs = True
            for i in range(len(searchResults)):
                if result not in searchResults[i]:
                    belongs = False
            if (belongs) and (result not in finalResults):
                finalResults.append(result)
        
        return finalResults
    
    def getAliases(self):
        aliases = []
        for word in self.words:
            if word[-1] == "a" and word != "fêmea" and word != "femea":
                aliases.append(word[:-1] + "o")
            elif word[-1] == "o" and word != "macho":
                aliases.append(word[:-1] + "a")
        return aliases