from mlo.storage.firebaseDB import FirebaseDB
from mlo.auth.dataModel import DataModel
from mlo.auth.firebaseAuth import FireBaseAuthService
from fakeSignUpManager import FakeSignUpManager

dataModel = DataModel()
auth = FireBaseAuthService()
storege = FirebaseDB()  

signUpManager = FakeSignUpManager(auth,dataModel,storege)

def testInvalidName():
    loginScreenData = {
        'name':'@123',
        'cpf':10916877784,
        'email':'carlos1@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "Preencha os campos corretamente"
    
def testCPFWith10Digits():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':1091687778,
        'email':'carlos2@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "CPF inválido"

def testInvalidEmail():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlosgmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "Preencha um email válido" 

def testInvalidPassword():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos3@gmail.com',
        'password1':'123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "A senha deve ter no mínimo 6 digitos"

def testInvalidPasswordConfirmation():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos4@gmail.com',
        'password1':'asd123',
        'password2':'123asd',
        'minimumAge': True,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "As senhas inseridas são diferentes"

def testInvalidMinimumAge():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos5@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': False,
        'check':True
    }
    action = signUpManager.singUpScreenManager(**loginScreenData)
    assert action == "Você deve ter mais de 18 anos para usar o aplicativo"

def testInvalidState():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos5@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'@123',
        'city':'Campinas',
        'CEP':13083872,
        'neighborhood':'Cidade Universitária',
        'address':'R. da Reitoria',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Preencha os campos corretamente"

def testInvalidCity():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos6@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'@123',
        'CEP':13083872,
        'neighborhood':'Cidade Universitária',
        'address':'R. da Reitoria',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Preencha os campos corretamente"

def testCEPWith7digits():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos7@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'Campinas',
        'CEP':1308387,
        'neighborhood':'Cidade Universitária',
        'address':'R. da Reitoria',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "CEP inválido"

def testInvalidNeighborhood():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos8@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'Campinas',
        'CEP':13083872,
        'neighborhood':'@123',
        'address':'R. da Reitoria',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Preencha os campos corretamente"

def testInvalidAddress():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos9@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'Campinas',
        'CEP':13083872,
        'neighborhood':'Cidade Universitária',
        'address':'@123',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Preencha os campos corretamente"

def testInvalidNumber():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos10@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'Campinas',
        'CEP':13083872,
        'neighborhood':'Cidade Universitária',
        'address':'R. da Reitoria',
        'number':'@123'
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Alguns campos devem ser preenchidos com números"

def testAllCorrect():
    loginScreenData = {
        'name':'Carlos de Souza',
        'cpf':10916877784,
        'email':'carlos11@gmail.com',
        'password1':'asd123',
        'password2':'asd123',
        'minimumAge': True,
        'check':True
    }
    signUpManager.singUpScreenManager(**loginScreenData)
    singUpScreen2bData = {
        'state':'São Paulo',
        'city':'Campinas',
        'CEP':13083872,
        'neighborhood':'Cidade Universitária',
        'address':'R. da Reitoria',
        'number':121
    }
    action = signUpManager.singUpScreen2bManager(**singUpScreen2bData)
    assert action == "Cadastro realizado com sucesso"