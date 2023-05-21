# import requests

# url = 'http://127.0.0.1:8000/flights/'
# myobj = {"arrivalAirportCode": "KIX","departureAirportCode": "TPE","departureDate": "5月29日","arrivalDate": "5月30日",}

# x = requests.post(url, json = myobj)

# print("x.text")
# print(x.text)
# ----------------------------------------------------------------------

import csv
import pymongo

# pick the trend data you want
with open("./trendfukuoka.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    temp = []
    for row in reader:
        print(row["outboundDate"], int(row["price"]))
        temp.append({"outboundDate": row["outboundDate"], "price": int(row["price"])})
    print('temp[0]["price"] == ')
    print(temp[0]["price"])


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["demoDB"]
mycol = mydb["TrendData"]
# change the destination of data
mydict = {"TD": temp, "destination": "fukuoka"}

x = mycol.insert_one(mydict)
