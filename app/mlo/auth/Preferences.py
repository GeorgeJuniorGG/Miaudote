from pydantic.dataclasses import dataclass

@dataclass
class userPreferences:
    possuiAnimal: str
    animalPreferido: str
    portePreferido: str
    caracteristicas: str
    tempoDisponivel: str

    def getJSONPreferences(self):
        dataPreferences = {
            u'preferences':{
                u'possuiAnimal': self.possuiAnimal,
                u'animalPreferido': self.animalPreferido,
                u'portePreferido': self.portePreferido,
                u'caracteristicas':self.caracteristicas,
                u'tempoDisponivel':self.tempoDisponivel,
            }
        }
        return dataPreferences