from mlo.auth.Address import Address
from mlo.auth.Preferences import userPreferences
from mlo.auth.HomeCharacteristics import homeCharacteristics
from config.firebase import getFirebaseFirestore

db = getFirebaseFirestore()
def createProtector(currentUser, name, birthDate, CPF):
    docRef = db.collection(u'protectors').document(currentUser)
    docRef.set({
        u'name': name,
        u'birthDate': birthDate,
        u'CPF': CPF
    })

def createAdopter(currentUser, name, birthDate, CPF):
    docRef = db.collection(u'adopters').document(currentUser)
    docRef.set({
        u'name': name,
        u'birthDate': birthDate,
        u'CPF': CPF
    })

def storeAddress(collection:str,currentUser:str, state:str, city:str, CEP:int, neighborhood:str, address:str, number:int)->bool:
    try:
        userAddress = Address(state, city, CEP, neighborhood, address, number)
    except:
        return False
    docRef = db.collection(collection).document(currentUser)
    if(docRef.update(userAddress.getJSONAdress())):
        return True
    return False

def storePreferences(currentUser:str, possuiAnimal:str, animalPreferido:str, portePreferido:str, caracteristicas:str, tempoDisponivel:str):
    if(possuiAnimal and animalPreferido and portePreferido and caracteristicas and tempoDisponivel):
        try:
            preferences = userPreferences(possuiAnimal, animalPreferido, portePreferido, caracteristicas, tempoDisponivel)
        except:
            return False
    else:
        return False
    docRef = db.collection(u'adopters').document(currentUser)
    if(docRef.update(preferences.getJSONPreferences())):
        return True
    return False

def storeHomeCharacteristics(currentUser:str, tipoResidencia:str, espacoDisponivel:str, ambienteAberto:str, rotasFuga:str, possuiCriancas:str):
    if(tipoResidencia and espacoDisponivel):
        try:
            userHomeCharacteristics = homeCharacteristics(tipoResidencia, espacoDisponivel, ambienteAberto, rotasFuga, possuiCriancas)
        except:
            return False
    else:
        return False
    docRef = db.collection(u'adopters').document(currentUser)
    if(docRef.update(userHomeCharacteristics.getJSONHomeCharacteristics())):
        return True
    return False