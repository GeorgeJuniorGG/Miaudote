from pydantic import BaseModel, validator

class HomeCharacteristics(BaseModel):
    houseType: str
    availableSpace: str
    openArea:bool = False 
    escapeRoutes: bool = False
    haveChildren: bool = False

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

    def getHomeCharacteristicsForFireStore(self):
        dataHomeCharacteristics = {u'homeCharacteristics':self.dict()}
        return dataHomeCharacteristics