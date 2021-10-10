from config.firebase import getFirebase

auth = getFirebase().auth()

#Cadastra novo usuario
def signUp(self, email, password):
    if(not email or not password):
        print('Preencha os campos corretamente')
    else:
        try:
            user = auth.create_user_with_email_and_password(email, password)
            print("Cadastro realizado com sucesso!")
        except: 
            print("E-mail já cadastrado")
    return

#Verifica cadastro do usuario
def login(self, email, password):
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        return True
    except:
        print("Invalid email or password")
    return False