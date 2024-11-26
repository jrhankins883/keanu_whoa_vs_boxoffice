import requests

# I'm establishing the variables I need in order to access the Keanu Reeves Filmography on TMDb
API_KEY = '93b29bf0b851209878217fccd1d8ca1a'
base_URL = "https://api.themoviedb.org"
url = f"{base_URL}/person/{6384}/movie_credits?api_key={API_KEY}"
response = requests.get(url)

# This block of code is to check if the API response was successful
if response.status_code == 200: 
    print(f"Request Successful!")
else:
    print(f"Error: {response.status_code}")
    
data = response.json()