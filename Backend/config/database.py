from pymongo import MongoClient

MongoClient()

client = MongoClient(
    "mongodb+srv://username:password@cluster0.cythueh.mongodb.net/?retryWrites=true&w=majority")
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
AangawadiSummaryCollection = db["AaganwadiSummary"]