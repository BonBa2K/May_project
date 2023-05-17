import requests

url = "https://instagram28.p.rapidapi.com/username"

querystring = {"user_id":"4159535681"}

headers = {
	"X-RapidAPI-Key": "5f3fc4eaf6mshaa358eef5285042p171836jsnad4613921270",
	"X-RapidAPI-Host": "instagram28.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())