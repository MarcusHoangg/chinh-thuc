'''
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
response = requests.get(request).json()
print(response)

for a in response:
    print(a["show"]["name"])

import json
import requests

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        # print(json.dumps(json_response, indent=2))
        for a in json_response:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")
'''
#ex1
'''
import requests
response = requests.get("https://api.chucknorris.io/jokes/random").json()
print(response['value'])
'''
#ex2
'''
import requests
import json

country = input("Enter your municipality (city): ")
country_api = ("https://api.openweathermap.org/data/2.5/weather?q="
               + country
               + "&limit=5&appid=fe076d38a7a7af9a836f793bfec86c9e&units=metric")
response = requests.get(country_api).json()

with open('ScratchOutput.txt', 'w') as file:
    file.write(json.dumps(response, indent = 4))
    file.write('\n\n#----------- END OF OUTPUT -----------#\n\n')
lat = str(response['coord']['lat'])
lon = str(response['coord']['lon'])
request = ("https://api.openweathermap.org/data/2.5/weather?lat="
           + lat + "&lon=" + lon
           + "&appid=fe076d38a7a7af9a836f793bfec86c9e&units=metric")
response = requests.get(request).json()

with open("ScratchOutput.txt", 'a') as file:
    file.write(json.dumps(response, indent = 4))
print(f"Today {country}'s weather is: {response['weather'][0]['description']}")
print(f"The temperature (in Celsius) is: {response['main']['temp'] :.2f}")
'''