from config.firebase import getFirebaseFirestore
class FakePetsDB():
    def getPets(self):
        db = getFirebaseFirestore()
        return db.collection("pets")