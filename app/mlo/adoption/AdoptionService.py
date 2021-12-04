from mlo.adoption.ARModel import ARModel
from mlo.database.AdoptionDB import AdoptionDB
from mlo.pets.PetService import PetService
from mlo.user.UserService import UserService

class AdoptionService:

    def __init__(self, adopRDB:AdoptionDB, usrService:UserService, petService:PetService):
        self.__db = adopRDB
        self.userService = usrService
        self.petService = petService


    def __checkARCreation(self, rQueue:list, adpID:str) -> bool:
        """
        Verifica que o adotante já realizou uma solicitação de adoção ao pet\n
        Caso já tenha feito retorna False, caso não exita uma solicitação
        Retorna True
        """
        for arID in rQueue:
            request = self.getAR(arID)
            if request != None:
                if request['adopterID'] == adpID:
                    return False
        
        return True

    def createAR(self, petID:str) -> bool:
        """
        Criar uma solicitação de adoção e registrar no banco de dados\n
        Esse é um recurso exclusivo para adotantes
        """
        try:
            adopterID = self.getUserID()
            petData = self.petService.getPetData(petID)

            # Impedir que um adotante tente solicitar a adoção de um pet mais de uma vez
            if not self.__checkARCreation(petData['requestQueue'], adopterID):
                return False

            protectorID = petData['protectorId']
            arID = self.__db.createAR(petID, adopterID, protectorID)
            
            if arID == None:
                return False

            if not self.petService.insertAR(petID, arID):
                self.deleteAR(arID)
                return False

            if not self.userService.insertAR(adopterID, arID):
                self.deleteAR(arID)
                return False
            
            if len(petData['requestQueue']) == 0:
                if not self.userService.insertAR(protectorID, arID):
                    self.deleteAR(arID)
                    return False
            
            
            return arID
        
        except:
            return False

    def getAR(self, arID:str) -> dict:
        """
        Obtem uma solicitação de adoção do BD\n
        Retorna um dicionário com as informações dela
        """
        arData:ARModel = self.__db.getAR(arID)
        if arData == None:
            return None

        return arData.dict()


    def deleteAR(self, arID:str) -> bool:
        """
        Deletar uma solicitação de adoção\n
        É necessário tentar deletar a referência a solicitação\n
        em todas as classes que utilizam ela
        """
        try:
            arData:ARModel = self.__db.getAR(arID)
            self.petService.deleteAR(arData.petID, arID)
            self.userService.deleteAR(arData.adopterID, arID)
            self.userService.deleteAR(arData.protectorID, arID)
            return self.__db.deleteAR(arID)
        except:
            return False

    def updateARStatus(self, arID:str, status:bool) -> bool:
        """
        Atualiza o status da Solicitação de Adoção:\n
        * status = None -> Solicitação em andamento\n
        * status = False -> Solicitação recusada\n
        * status = True -> Solicitação aceita
        """
        return self.__db.updateARStatus(arID, status)

    def getUserID(self) -> str:
        return self.userService.getUserID()

    def getARData(self):

        try:
            userData = self.userService.getUserData()
            arUserList = userData['adoptationRequests']

            arList = list()

            for arID in arUserList:
                request: ARModel = self.__db.getAR(arID)
                petData = self.petService.getPetData(request.petID)
                arData = {
                    'arID': arID,
                    'arStatus': request.status,
                    'imageSource': petData['images'][0],
                    'petName': petData['name'],
                    'pid': petData['pid'],
                    'description': f'{petData["name"]} recebeu uma solicitação de adoção!',
                    'details': petData['details'],
                    'petChars': [petData['sex'],
                                petData['size'],
                                petData['color']]                 
                }

                arList.append(arData)

            return arList

        except:
            return None

    def getAdopterData(self, arID:str) -> dict:

        try:
            arData:ARModel = self.__db.getAR(arID)
            if arData == None:
                return None

            # Dados do Adotante
            raw = self.userService.getAnotherUserData(arData.adopterID)
            raw = raw.dict()

            data = {
                'name': raw['name'],
                'adopterImage': raw['userImage'],
                'city': raw['address']['city'],
                'state': raw['address']['city'],
                'homeCharacteristics': raw['homeCharacteristics'],
                'availableTime': raw['preferences']['availableTime'],
                'haveAnimal': raw['preferences']['haveAnimal'],
                'adoptationRequests': raw['adoptationRequests']
            }

            return data

        except:
            return None