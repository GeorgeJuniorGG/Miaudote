from firebase import firebase

firebase = firebase.FirebaseApplication('https://miaudote-b4e55-default-rtdb.firebaseio.com/', None)

#Cadastra novo usuario
def registerUser(self, email, password):
    if(not email or not password):
        print('Preencha os campos corretamente')
    elif(isRegistered(email)):
        print('E-mail já cadastrado')
    else:
        data = {
            'Email': email,
            'Password': password
        }
        firebase.post('miaudote-b4e55-default-rtdb/Users', data)

#Verifica cadastro do usuario
def loginUser(self, email, password):
    result = firebase.get('miaudote-b4e55-default-rtdb/Users', '')
    for i in result.keys():
        if(result[i]['Email']==email and password== result[i]['Password']):
            return True
    return False

#Verifica se um e-mail ja foi cadastrado
def isRegistered(email):
    result = firebase.get('miaudote-b4e55-default-rtdb/Users', '')
    for i in result.keys():
        if(email == result[i]['Email']):
            return True
        return False
