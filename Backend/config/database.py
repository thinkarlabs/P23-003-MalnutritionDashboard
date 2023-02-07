from pymongo import MongoClient

MongoClient()

client = MongoClient(
    "mongodb+srv://username:password@cluster0.mbx9gz6.mongodb.net/?retryWrites=true&w=majority")
db = client.Malnutrition
NgoCollection = db["Ngo"]
UserCollection = db["User"]

