from pydantic import BaseModel, Field, validator
from datetime import datetime, timezone
from typing import List

class PetModel(BaseModel):
    pid: str = Field(default="")
    protectorId: str = Field(default="")
    name: str
    type: str
    origin: str
    health: str
    localization: str
    ambient: str
    details: str
    sex: str
    size: str
    color: str
    city: str = Field(default="")
    state: str = Field(default="")
    images: List[str] = ['https://firebasestorage.googleapis.com/v0/b/miaudote-b4e55.appspot.com/o/petImages%2Fdefault%2Fsem_imagem.png?alt=media&token=4a70b76b-1405-4e8d-a16d-8ce56d12b308']
    requestStatus: bool = Field(default=False)
    requestQueue: List[str] = Field(default_factory=list)
    createAt: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))
    Activities: str = Field(default="")
    Age: str = Field(default="")
    Personality: str = Field(default="")

class PetModelScreen1(BaseModel):
    name: str
    type: str
    color: str
    sex: str
    size: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

class PetModelScreen2(BaseModel):
    ambient: str
    origin: str
    health: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

class PetModelScreen3(BaseModel):
    details: str
    Personality: str
    Activities: str
    Age: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v
    
    @validator('details')
    def character_limit(cls, v):
        if len(str(v))>200:
            raise ValueError('Limite de 200 caracteres atingido')
        return v