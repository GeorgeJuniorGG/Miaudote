from mui.login.LoginScreen import LoginScreen
from mlo.auth.authService import AuthService

class LoginManager:

    def __init__(self, service:AuthService) -> None:
        self.screen = LoginScreen(name='LoginScreen')
        self.service = service
        self.screen.controller = self
    
    def login(self, email:str, password:str):
        result = self.service.login(email, password)
        if result:
            print(self.service.getUserID())
            print("Entrando...")
        else:
            print("E-mail ou senha incorreto")