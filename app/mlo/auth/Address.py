from pydantic.dataclasses import dataclass

@dataclass
class Address:
    state: str
    city: str
    CEP: int
    neighborhood: str
    address: str
    number: int

    def getJSONAdress(self):
        dataAddress = {
            u'address':{
                u'state': self.state,
                u'birthDate': self.city,
                u'CEP': self.CEP,
                u'neighborhood':self.neighborhood,
                u'address':self.address,
                u'number':self.number
            }
        }
        return dataAddress