from pydantic import BaseModel, validator, EmailStr


class BasicUSerData(BaseModel):
    name: str
    cpf: int
    email: EmailStr

    @validator('name')
    def name_not_empty(cls, v):
        if len(v)<1:
            raise ValueError('Preencha seu nome')
        return v

    @validator('cpf')
    def cpf_with_eleven_numbers(cls, v):
        if len(str(v))!=11:
            raise ValueError('CPF inválido')
        return v