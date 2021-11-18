from .basicUserdata import BasicUSerData
from .authService import AuthService
from config.firebase import getFirebase
from mlo.storage.firebaseDB import FirebaseDB

auth = getFirebase().auth()

class FireBaseAuthService(AuthService):
    #Cadastra novo usuario
    def signUp(self, password1:str, password2:str, minimumAge:bool, isProtector:bool, userData:BasicUSerData):
        if(not password1 or not password2):
            print("Preencha os campos corretamente")
            return False
        elif(password1 != password2):
            print("As senhas inseridas são diferentes")
            return False
        elif(len(password1)<6):
            print("A senha deve ter no mínimo 6 digitos")
            return False
        elif(not minimumAge):
            print("Você deve ter mais de 18 anos para usar o aplicativo")
            return False
        else:
            try:
                currentUser = auth.create_user_with_email_and_password(userData.email, password1)['localId']
                print("Cadastro realizado com sucesso!")
            except:
                print("E-mail já cadastrado")
                return False
            if(isProtector):
                FirebaseDB.createProtector(currentUser,userData)
            else:
                FirebaseDB.createAdopter(currentUser,userData)
            return currentUser

    #Verifica cadastro do usuario
    def login(self, email:str, password:str) -> bool:
        try:
            auth.sign_in_with_email_and_password(email, password)
            return True
        except:
            print("Invalid email or password")
        return False