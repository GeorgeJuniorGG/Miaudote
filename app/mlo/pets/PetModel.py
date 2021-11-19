from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List

class PetModel(BaseModel):
    pid: str
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
    requestStatus: bool = Field(default=False)
    requestQueue: List[str] = Field(default_factory=list)
    createAt: datetime = Field(default_factory=lambda x: datetime.now(timezone.utc))