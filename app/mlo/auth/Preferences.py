from pydantic import BaseModel, validator

class UserPreferences(BaseModel):
    haveAnimal: str
    favoriteAnimal: str
    favoriteSize: str
    personalityCharacteristics: str
    activitiesCharacteristics: str
    ageCharacteristics: str
    availableTime: str

    @validator('*')
    def no_empty_fields(cls, v):
        if v == '':
            raise ValueError('Existem campos vazios')
        return v

    def getPreferencesForFireStore(self):
        dataPreferences = {'preferences':self.dict()}
        return dataPreferences