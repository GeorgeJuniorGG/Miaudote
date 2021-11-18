from pydantic import BaseModel, validator


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

    @validator('CEP')
    def valid_CEP(cls, v):
        if len(str(v))!=8:
            raise ValueError('CEP inválido')
        return v

    def getAdressForFireStore(self):
        dataAddress = {'address':self.dict()}
        return dataAddress  