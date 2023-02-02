from pymongo import MongoClient

MongoClient()
client = MongoClient("mongodb+srv://username:password@cluster0.jl1jke6.mongodb.net/?retryWrites=true&w=majority")
db = client.mulnutrition
collection = db["Mulnutrition"]
