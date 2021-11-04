from pydantic.dataclasses import dataclass

@dataclass
class homeCharacteristics():
    tipoResidencia: str
    espacoDisponivel: str
    ambienteAberto:bool = False 
    rotasFuga: bool = False
    possuiCriancas: bool = False

    def getJSONHomeCharacteristics(self):
        dataHomeCharacteristics = {
            u'homeCharacteristics':{
                u'tipoResidencia': self.tipoResidencia,
                u'espacoDisponivel': self.espacoDisponivel,
                u'ambienteAberto': self.ambienteAberto,
                u'rotasFuga':self.rotasFuga,
                u'possuiCriancas':self.possuiCriancas,
            }
        }
        return dataHomeCharacteristics