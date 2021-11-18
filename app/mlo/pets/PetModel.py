from pydantic import BaseModel, Field

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
    requestQueue: list[str] = Field(default_factory=list)