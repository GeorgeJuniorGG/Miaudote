from datetime import datetime, timezone
from mlo.adoption.ARModel import ARModel
from .AdoptionDB import AdoptionDB
from config.firebase import getFirebaseFirestore

class FBAdoptionDB(AdoptionDB):

    __AR_COLLECTION = 'adoptionRequests'
    __CHAT_COLLECTION = 'Chats'

    def __init__(self) -> None:
        self.__db = getFirebaseFirestore()
        self.__c_ref = self.__db.collection(self.__AR_COLLECTION)
        self.__chat_c_ref = self.__db.collection(self.__CHAT_COLLECTION)
    
    def getAR(self, arID:str) -> ARModel:
        """Obter dados sobre a Requisição de Adoção no Firebase"""
        try:
            arDoc = self.__c_ref.document(arID).get()
            if not arDoc.exists:
                return None
            arData = arDoc.to_dict()
            return ARModel(**arData)
        except:
            return None

    def createAR(self, petID: str, adpID: str, pttID: str) -> str:
        """Criar uma nova Requisição de Adoção no Firebase"""
        try:
            fModel = ARModel(petID=petID, adopterID=adpID, protectorID=pttID)
            ar_doc_ref = self.__c_ref.add(fModel.dict())[-1]
            self.__c_ref.document(ar_doc_ref.id).update({'arID': ar_doc_ref.id})
            return ar_doc_ref.id
        except:
            return None

    def deleteAR(self, arID: str, chatID:str) -> bool:
        """
        Deletar uma Requisição de Adoção no Firebase
        juntamente com o chat associado a ela
        """
        try:
            self.__c_ref.document(arID).delete()
            if chatID != None:
                self.__chat_c_ref.document(chatID).delete()
            return True
        except:
            return False

    def updateARStatus(self, arID:str, status:bool) -> bool:
        """Atualizar o status de uma Requisição de Adoção no Firebase"""
        try:
            self.__c_ref.document(arID).update({'status': status})
            return True
        except:
            return False

    def createChat(self, petID:str, adpID:str, pttID:str) -> str:
        """
        Cria um canal de chat entre o Protetor e adotante
        após uma solicitação de adoção ser aprovada
        """
        try:
            chat_c_ref = self.__chat_c_ref
            chat_doc = chat_c_ref.add({
                'petID': petID,
                'adopterID': adpID,
                'protectorID': pttID,
                'createAt': datetime.now(timezone.utc) 
            })[-1]

            return chat_doc.id
        
        except:
            return None

    def includeChat(self, arID:str, chatID:str) -> bool:
        """
        Atualizar uma Requisição de Adoção no Firebase\n
        incluindo o id do chat quando a requisição é aprovada
        """
        try:
            self.__c_ref.document(arID).update({
                'chatID': chatID,
                'status': True
            })
            return True
        except:
            return False        