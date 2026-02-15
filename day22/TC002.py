from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

# IMPORTANT: match exact DB name case
db = client["Company_DB"]
collection = db["employees"]

print("Connected to MongoDB")

employee = {
    "name": "Mounika",
    "dep": "CSE",
    "course": "Python",
    "salary": 50000
}

collection.insert_one(employee)
print("Employee inserted")

for emp in collection.find():
    print(emp)

client.close()