from mlo.petrecommendation.RecommendedPets import RecommendedPets

class FakeRecommendedPets(RecommendedPets):

    def getRecommended(self):
        return "recomendados"