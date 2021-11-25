from typing import List
from mlo.petsearch.resultsPrioritization import ResultsPrioritization
from mlo.petsearch.searchLogic import SearchLogic
from mlo.petrecommendation.RecommendedPets import RecommendedPets

class SearchService:
    def __init__(self, prioritizationServ: ResultsPrioritization, searchServ: SearchLogic, recommendationServ: RecommendedPets):
        self.prioritizationServ = prioritizationServ
        self.searchServ = searchServ
        self.recommendationServ = recommendationServ
    
    def getRecommended(self):
        results = self.recommendationServ.getRecommended()

        results = self.prioritizationServ.getResults(results)

        return results

    def getSearchResults(self, words: List):
        results = self.searchServ.getResults(words)

        if (results == "Limite de palavras ultrapassado"):
            pass
            
        elif (results == "Erro de busca (palavras não correspondem a filtros)"):
            pass

        elif (results == "Não encontrou resultados"):
            pass

        else:
            results = self.prioritizationServ.getResults(results)
        
        return results