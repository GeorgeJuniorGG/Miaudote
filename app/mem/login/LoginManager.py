from pydantic.error_wrappers import ValidationError
from mui.login.LoginScreen import LoginScreen
from mlo.auth.authService import AuthService
from mlo.auth.UserLoginData import UserLoginData

class LoginManager:

    def __init__(self, service:AuthService) -> None:
        self.screen = LoginScreen(name='LoginScreen')
        self.service = service
        self.screen.controller = self
    
    def login(self, email:str, password:str) -> bool:
        userLogin = False
        
        try: 
            userLogin = UserLoginData(email=email, password=password) 
        except ValidationError as e:
            self.screen.showToast(e.errors()[0]['msg'])

        if(userLogin):
            result = self.service.login(userLogin)
            if result:
                print(self.service.getUserID())
                self.screen.showToast("Entrando...")
                orchestrator = self.screen.manager.orchestrator
                userID = self.service.getUserID()
                orchestrator.userLogin(userID)
                return True
            else:
                self.screen.showToast("Usuário não cadastrado")
                return False
        else:
            return False

    def goBackward(self):
        self.screen.manager.goWelcome()