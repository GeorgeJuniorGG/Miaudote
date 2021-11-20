from pydantic.error_wrappers import ValidationError
from mui.login.LoginScreen import LoginScreen
from mlo.auth.authService import AuthService
from mlo.auth.UserLoginData import UserLoginData

class LoginManager:

    def __init__(self, service:AuthService) -> None:
        self.screen = LoginScreen(name='LoginScreen')
        self.service = service
        self.screen.controller = self
    
    def login(self, email:str, password:str):
        userLogin = False
        try: 
            userLogin = UserLoginData(email=email, password=password) 
        except ValidationError as e:
            print(e)

        if(userLogin):
            result = self.service.login(userLogin)
            if result:
                print(self.service.getUserID())
                print("Entrando...")
        else:
            print("E-mail ou senha incorreto")

    def goBackward(self):
        self.screen.manager.goBackward('right')