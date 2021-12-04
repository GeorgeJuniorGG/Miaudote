from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Union

# Modelo para solicitações de adoção
class ARModel(BaseModel):
    arID:str = Field(default='')
    petID:str
    adopterID:str
    protectorID:str
    status:bool = Field(default=None)
    chatID:str = Field(default=None)
    createAt: datetime = Field(default_factory = lambda: datetime.now(timezone.utc))
