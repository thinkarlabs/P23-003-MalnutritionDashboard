from pymongo import MongoClient

MongoClient()

client = MongoClient("mongodb+srv://username:password@cluster0.cythueh.mongodb.net/?retryWrites=true&w=majority")
db = client.Malnutrition
NgoCollection = db["Ngo"]
UserCollection = db["User"]
DonorsCollection = db["donors"]

AanganwadiCollection = db["Aanganwadi"]
