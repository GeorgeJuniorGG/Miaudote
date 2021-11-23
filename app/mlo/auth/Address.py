from pydantic import BaseModel, validator
import re
from unidecode import unidecode

class Address(BaseModel):
    state: str
    city: str
    CEP: int
    neighborhood: str
    address: str
    number: int

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

    @validator('state')
    def state_without_numbers(cls, v):
        if not str(v).replace(" ", "").isalpha():
            raise ValueError('Estado não pode conter números')
        return v

    @validator('city')
    def city_without_numbers(cls, v):
        if not str(v).replace(" ", "").isalpha():
            raise ValueError('Cidade não pode conter números')
        return v

    @validator('CEP')
    def valid_CEP(cls, v):
        if len(str(v))!=8:
            raise ValueError('CEP inválido')
        return v
    
    @validator('neighborhood')
    def neighborhood_without_special_characters(cls, v):
        pattern = "^[A-Za-z0-9_-]*$"
        if not bool(re.match(pattern, unidecode(str(v)).replace(" ", ""))):
            raise ValueError('Bairro não pode conter caracteres especiais')
        return v

    @validator('address')
    def address_without_special_characters(cls, v):
        pattern = "^[A-Za-z0-9_-]*$"
        if not bool(re.match(pattern, unidecode(str(v)).replace(" ", "").replace(".", ""))):
            raise ValueError('Endereço não pode conter caracteres especiais')
        return v

    def getAdressForFireStore(self):
        dataAddress = {'address':self.dict()}
        return dataAddress  