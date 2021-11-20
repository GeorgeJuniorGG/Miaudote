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
            print("Entrando...")
            print(self.service.getUserID())
            orchestrator = self.screen.manager.orchestrator
            userID = self.service.getUserID()
            orchestrator.userLogin(userID)
            
        else:
            print("E-mail ou senha incorreto")

    def goBackward(self):
        self.screen.manager.goBackward('right')