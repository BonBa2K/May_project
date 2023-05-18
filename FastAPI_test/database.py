import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["demoDB"]
dblst = myclient.list_database_names()
