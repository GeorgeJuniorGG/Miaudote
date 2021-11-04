from config.firebase import getFirebase
from .authService import AuthService

auth = getFirebase().auth()

class FireBaseAuthService(AuthService):

    #Cadastra novo usuario
    def signUp(self, email:str, password:str, passwordConfirmation:str) -> bool:
        try:
            currenteUser = auth.create_user_with_email_and_password(email, password)['localId']
            print("Cadastro realizado com sucesso!")
        except:
            print("E-mail já cadastrado")
            return False
        return currenteUser

    #Verifica cadastro do usuario
    def login(self, email:str, password:str) -> bool:
        try:
            auth.sign_in_with_email_and_password(email, password)
            return True
        except:
            print("Invalid email or password")
        return False