from pymongo import MongoClient

MongoClient()
client = MongoClient("mongodb+srv://AlekhyaA:alli2414@cluster0.cythueh.mongodb.net/?retryWrites=true&w=majority")
db = client.malnutrition
collection = db["Malnutrition"]
