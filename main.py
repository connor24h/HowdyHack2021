
import requests

url = "https://sridurgayadav-chart-lyrics-v1.p.rapidapi.com/apiv1.asmx/SearchLyricDirect"

querystring = {"artist":"michael jackson","song":"bad"}

headers = {
    'x-rapidapi-host': "sridurgayadav-chart-lyrics-v1.p.rapidapi.com",
    'x-rapidapi-key': "undefined"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)