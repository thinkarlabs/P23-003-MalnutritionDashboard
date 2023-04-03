from pymongo import MongoClient

MongoClient()

client = MongoClient(
    "mongodb+srv://ssunanda02:pass123@cluster0.jl1jke6.mongodb.net/?retryWrites=true&w=majority")
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