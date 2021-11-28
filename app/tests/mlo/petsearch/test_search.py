from mlo.pets.PetService import PetService
from mlo.petsearch.searchLogic import SearchLogic
from .fakeRecommendedPets import FakeRecommendedPets
from mlo.database.firebasePetDB import FPetDB

db = FPetDB()
service = PetService(db)
recomendacoes = FakeRecommendedPets()

def testEmpty():
    words = "".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == recomendacoes.getRecommended()

def testExceedMaxWords():
    words = "gato gato gato grande grande médio gato gato gato gato gato".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == "Limite de palavras ultrapassado"

def testSearchError():
    words = "pão francês".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == "Erro de busca (palavras não correspondem a filtros)"

def testOneTypeFilterOneOutput():
    words = "coelho".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["5dGugzeDyHGCnzOKUOa4"]

def testOneTypeFilterAliasOneOutput():
    words = "coelha".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["5dGugzeDyHGCnzOKUOa4"]

def testOneColorFilterOneOutput():
    words = "alaranjado".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["4prTZhzu71iQaGpCo1bE"]

def testOneColorFilterTwoOutputs():
    words = "cinza".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["5dGugzeDyHGCnzOKUOa4", "ooN3HLD1KIwEuLfU5N3e"]

def testOneColorFilterInsidePetAttribute():
    words = "preta".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf", "UpQ5n7zunKQtxj6lssWD", "hSUEibsTv9s9qXZ3bc6W"]

def testTextInsideOneColorFilterOneOutput():
    words = "laranja".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["4prTZhzu71iQaGpCo1bE"]

def testOneFilterAliasInsidePetAttribute():
    words = "preto".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf", "UpQ5n7zunKQtxj6lssWD", "hSUEibsTv9s9qXZ3bc6W"]

def testOneFilterHigherCaseLowerCaseTextInsidePetAttribute():
    words = "PrEtA".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf", "UpQ5n7zunKQtxj6lssWD", "hSUEibsTv9s9qXZ3bc6W"]

def testOneTypeFilterOneColorFilter():
    words = "cachorro preto".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf"]

def testOneColorFilterOneTypeFilter():
    words = "preto cachorro".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf"]

def testFourDifferentFilters():
    words = "gato cor alaranjado macho tamanho pequeno".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["4prTZhzu71iQaGpCo1bE"]

def testTwoTypeFilters():
    words = "cachorro gato".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["4prTZhzu71iQaGpCo1bE", "CuPW0ls75210CnlQtFsf", "MZE6I2In7LGcUdt1vgfh", "UpQ5n7zunKQtxj6lssWD", "hSUEibsTv9s9qXZ3bc6W", "ooN3HLD1KIwEuLfU5N3e", "xz3x7XD4wgGcBZ5SofIA"]

def testTwoTypeTwoColorFilters():
    words = "cachorro preto gato branco".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == ["CuPW0ls75210CnlQtFsf", "UpQ5n7zunKQtxj6lssWD", "hSUEibsTv9s9qXZ3bc6W", "xz3x7XD4wgGcBZ5SofIA"]

def testNoResults():
    words = "coelho preta".split(" ")
    busca = SearchLogic(service, recomendacoes)
    resultados = busca.getResults(words)
    assert resultados == "Não encontrou resultados"