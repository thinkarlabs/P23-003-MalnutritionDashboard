from pymongo import MongoClient

MongoClient()

client = MongoClient(
    "mongodb+srv://root:Emids123@cluster0.jwkiznj.mongodb.net/?retryWrites=true&w=majority")
db = client.Malnutrition
NgoCollection = db["Ngo"]
UserCollection = db["User"]
DonorsCollection = db["Donors"]
AanganwadiCollection = db["Aanganwadi"]
ChildCollection = db["Child"]
ChildMalnutritionCollection = db["ChildMalnutrition"]
SupplementaryCollection = db["Supplementary"]
SupplementDetailsCollection = db["SupplementsDetails"]
ProgramsCollection = db["Programs"]
ProgramJoiningCollection = db["ProgramJoining"]
