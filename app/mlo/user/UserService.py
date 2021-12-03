from os import truncate
from mlo.database.UserDB import UserDB
from .UserModel import AdopterModel, ProtectorModel, UserModel
from pydantic import ValidationError

class UserService:

    def __init__(self, db:UserDB) -> None:
        self.__db = db

    def getUserData(self) -> dict:
        uData: UserModel = None
        uData = self.__db.getUserData()

        if uData != None:
            return uData.dict()
        
        return None

    # Atualiza as informações do usuário no banco de dados
    def updateUserData(self, newData:dict) -> bool:
        uData = self.__db.getUserData()
        userData = uData.dict()
        udKeys = userData.keys()
        
        # Substituir os novos dados do usuário
        for key in newData.keys():
            if not key in udKeys:
                return False

            if key in ['address', 'homeCharacteristics', 'preferences']:
                subkeys = userData[key].keys()
                for skey in newData[key].keys():
                    if not skey in subkeys:
                        return False                    
                    userData[key][skey] = newData[key][skey]

            userData[key] = newData[key]

        
        # Determinar a classe do usuário
        clss = UserModel
        if isinstance(uData, AdopterModel):
            clss = AdopterModel
        else:
            clss = ProtectorModel

        try:
            uData = clss(**userData)
            #print(uData)
            return self.__db.updateUserData(uData)
        
        except ValidationError as e:
            return False

    # Salvar a nova imagem do usuário no banco
    def updateUserImage(self, imagePath:str) -> bool:
        return self.__db.updateUserImage(imagePath)

    # Obter dados de outro usuário
    def getAnotherUserData(self, anUID:str):
        return self.__db.getAnotherUserData(anUID)

    def addPetId(self, petId):
        self.__db.addPetId(petId)

    # Obter o tipo de usuario
    def getUserType(self) -> str:
        protector = self.__db.isProtector()

        if(protector):
            return "protector"
        
        else:
            return "adopter"

    # Obter o ID do usuário Host
    def getUserID(self) -> str:
        return self.__db.getUserID()