from mlo.auth.firebaseAuth import FireBaseAuthService
from mem.login.LoginManager import LoginManager

service = FireBaseAuthService()
loginManager = LoginManager(service)

def testEmptyEmail():
    email = ""
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testeEmptyPassword():
    email = "usuario@teste.com"
    password = ""
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidPassword_Short():
    email = "usuario@teste.com"
    password = "Teste"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidPassword_Long():
    email = "usuario@teste.com"
    password = "TesteTesteTeste0123456789"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidPassword_SpecialCharacter():
    email = "usuario@teste.com"
    password = "Teste123*"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidPassword_WrongFormat():
    email = "usuario@teste.com"
    password = "teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmail_WithoutAt():
    email = "usuarioteste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailDomain_WithoutDotCom():
    email = "usuario@teste"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailDomain_WrongFirstOrLastCharacter():
    email = "usuario@.teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailDomainFormat_WrongFormat():
    email = "usuario@te$te.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailLocalPart_WrongFirstOrLastCharacter():
    email = "usuario?@teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailLocalPart_WrongFormat():
    email = "u$uario@teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testInvalidEmailLocalPart_Dots():
    email = "usu...ario@teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testNotRegistredValidUser():
    email = "usuario0@teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == False

def testRegistredValidUser():
    email = "usuario@teste.com"
    password = "Teste123"
    validation = loginManager.login(email, password)
    assert validation == True