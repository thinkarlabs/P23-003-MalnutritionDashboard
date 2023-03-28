from pymongo import MongoClient

MongoClient()

client = MongoClient(
    "mongodb+srv://findjassi121212:Change456@cluster0.qzwhu7z.mongodb.net/?retryWrites=true&w=majority")
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