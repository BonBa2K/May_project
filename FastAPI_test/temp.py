import requests

url = 'http://127.0.0.1:8000/flights_oid/64623b57049781f013573eb0'
myobj = {'o_id': '64623b57049781f013573eb0'}

x = requests.post(url, json = myobj)

print("x.text")
print(x.text)