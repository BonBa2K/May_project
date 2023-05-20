import requests

url = 'http://127.0.0.1:8000/flights/'
myobj = {"arrivalAirportCode": "KIX","departureAirportCode": "TPE","departureDate": "5月29日","arrivalDate": "5月30日",}

x = requests.post(url, json = myobj)

print("x.text")
print(x.text)