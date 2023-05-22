# import requests

# url = 'http://127.0.0.1:8000/flights/'
# myobj = {"arrivalAirportCode": "KIX","departureAirportCode": "TPE","departureDate": "5月29日","arrivalDate": "5月30日",}

# x = requests.post(url, json = myobj)

# print("x.text")
# print(x.text)
# ----------------------------------------------------------------------

import csv
import pymongo
from datetime import date,timedelta

# pick the trend data you want
with open("./trendfukuoka.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    temp = []
    pass_date=date.fromisoformat('2023-05-20')
    
    for row in reader:
        # print(row["outboundDate"], int(row["price"]))
        D_first=date.fromisoformat(row["outboundDate"])
        while D_first != pass_date:
            # print("------------------")
            offset=timedelta(days=1)
            # print("pass_date == ")
            # print(pass_date)
            temp.append({"outboundDate": str(pass_date), "price": None})
            pass_date=pass_date+offset
        # print("------------------")
        temp.append({"outboundDate": row["outboundDate"], "price": int(row["price"])})
        pass_date=pass_date+offset
        
    # print("temp == ")
    # print(temp)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["demoDB"]
mycol = mydb["TrendData"]
# change the destination of data
mydict = {"TD": temp, "destination": "CJU"}


x = mycol.insert_one(mydict)
