from pydantic import BaseModel, validator

class UserPreferences(BaseModel):
    haveAnimal: str
    favoriteAnimal: str
    favoriteSize: str
    characteristics: str
    availableTime: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

    def getPreferencesForFireStore(self):
        dataPreferences = {u'preferences':self.dict()}
        return dataPreferences