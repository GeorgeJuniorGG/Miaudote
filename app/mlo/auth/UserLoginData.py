from pydantic import BaseModel, validator, EmailStr
from pydantic.types import SecretStr

class UserLoginData(BaseModel):
    email: EmailStr
    password: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

    @validator('password')
    def passwordMustBeMoreThan6Digits(cls, v):
        if len(str(v))<6:
            raise ValueError('Sua senha deve ter mais de 6 dígitos')
        return v