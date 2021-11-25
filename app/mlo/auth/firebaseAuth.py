from .UserLoginData import UserLoginData
from .basicUserdata import BasicUSerData
from .authService import AuthService
from config.firebase import getFirebase
from mlo.storage.firebaseDB import FirebaseDB

class FireBaseAuthService(AuthService):

    def __init__(self) -> None:
        self.__auth = getFirebase().auth()
        self.__userID = ""

    def correctFormat(self, password1):
        cbaixa = False
        calta = False
        digito = False

        for i in range(len(str(password1))):
            c = str(password1)[i]  # Caractere

            if (c.isdigit()) and (digito == False):
                digito = True
            else:
                if (c.islower()) and (cbaixa == False):
                    cbaixa = True
                elif (c.isupper()) and (calta == False):
                    calta = True
        if (cbaixa == False) or (calta == False) or (digito == False):
            return False
        return True

    #Cadastra novo usuario
    def signUp(self, password1:str, password2:str, minimumAge:bool, isProtector:bool, userData:BasicUSerData):
        if(not password1 or not password2):
            return "Preencha os campos corretamente"
        elif(len(password1)<6):
            return "A senha deve ter no mínimo 6 digitos"
        elif(len(password1)>20):
            return "A senha não pode ter mais do que 20 caracteres"
        elif(str(password1).isalnum() == False):
            return "A senha não pode ter caracteres especiais"
        elif(not self.correctFormat(password1)):
            return "A senha deve ter ao menos uma letra minúscula, uma letra maiúscula e um dígito"
        elif(password1 != password2):
            return "As senhas inseridas são diferentes"
        elif(not minimumAge):
            return "Você deve ter mais de 18 anos para usar o aplicativo"
        else:
            try:
                currentUser = self.__auth.create_user_with_email_and_password(userData.email, password1)['localId']
                print("Cadastro realizado com sucesso!")
            except:
                return "E-mail já cadastrado"
            if(isProtector):
                FirebaseDB.createProtector(currentUser,userData)
            else:
                FirebaseDB.createAdopter(currentUser,userData)
            self.__userID = currentUser
            return True

    #Verifica cadastro do usuario
    # def login(self, email:str, password:str) -> bool:
    def login(self, userLogin: UserLoginData) -> bool:
        try:
            result = self.__auth.sign_in_with_email_and_password(userLogin.email, userLogin.password)
            self.__userID = result['localId']
            return True
        except:
            print("Invalid email or password")
        return False

    # Obtem o Id do usuário no firebase
    def getUserID(self) -> str:
        return self.__userID