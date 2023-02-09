from pymongo import MongoClient

MongoClient()

client = MongoClient("mongodb+srv://username:password@cluster0.cythueh.mongodb.net/?retryWrites=true&w=majority")
db = client.Malnutrition
NgoCollection = db["Ngo"]
UserCollection = db["User"]
db =client["ngo_login"]
DonorsCollection = db["donors"]

