import pyrebase

#Configuração de comunicação com o firebase
firebaseConfig = {
    'apiKey': "AIzaSyD4vtY7ROr9i81IYoHU2-G8IxW43fRHi5M",
    'authDomain': "miaudote-b4e55.firebaseapp.com",
    'databaseURL': "https://miaudote-b4e55-default-rtdb.firebaseio.com",
    'projectId': "miaudote-b4e55",
    'storageBucket': "miaudote-b4e55.appspot.com",
    'messagingSenderId': "894885887773",
    'appId': "1:894885887773:web:0ef3e74c5a7a5ab5142bf4",
    'measurementId': "G-RLCE5G7GZH"
}
def getFirebase():
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase