from typing import List, final
from mlo.petrecommendation.RecommendedPets import RecommendedPets
from tests.mlo.petsearch.fakePetsDB import FakePetsDB

class SearchLogic:

    def __init__(self, words: List, recommendations: RecommendedPets):
        self.words = words
        self.recommendations = recommendations
        mock = FakePetsDB()
        self.dictPets = mock.getPets()
    
    def getResults(self):
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

        docs = self.dictPets.stream()
        for doc in docs:
            pet = doc.to_dict()

            if(pet['type'] not in types):
                types.append(pet["type"])

            if(pet["color"] not in colors):
                colors.append(pet["color"])

            if(pet["size"] not in sizes):
                sizes.append(pet['size'])
            
            if(pet['sex'] not in genders):
                genders.append(pet['sex']) 
        
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

        docs = self.dictPets.stream()
        for doc in docs:
            pet = doc.to_dict()
            for colorFilter in filters[0]:
                if(colorFilter in pet["color"] and doc.id not in searchColorResults):
                    searchColorResults.append(doc.id)
            for sizeFilter in filters[1]:
                if (sizeFilter in pet["size"] and doc.id not in searchSizeResults):
                    searchSizeResults.append(doc.id)
            for typeFilter in filters[2]:
                if (typeFilter in pet["type"] and doc.id not in searchTypeResults):
                    searchTypeResults.append(doc.id)
            for genderFilter in filters[3]:
                if (genderFilter in pet["sex"] and doc.id not in searchGenderResults):
                    searchGenderResults.append(doc.id)
        
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