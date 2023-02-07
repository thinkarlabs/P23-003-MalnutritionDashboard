from pymongo import MongoClient

MongoClient()


client = MongoClient("mongodb+srv://<username>:<password>@cluster0.cythueh.mongodb.net/?retryWrites=true&w=majority")
db = client.malnutrition
collection = db["Malnutrition"]


client = MongoClient("mongodb+srv://username:password@cluster0.jl1jke6.mongodb.net/?retryWrites=true&w=majority")
db = client.mulnutrition
collection = db["Mulnutrition"]

