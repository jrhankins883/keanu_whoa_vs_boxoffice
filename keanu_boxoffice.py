import requests

# I'm establishing the variables I need in order to access the Keanu Reeves Filmography on TMDb
pass #I guess it's bad to braodcast an API key so I've removed it from this file.  Pull from the other file in this folder when working on the project.
base_URL = "https://api.themoviedb.org"
url = f"{base_URL}/person/{6384}/movie_credits?api_key={API_KEY}"
response = requests.get(url)

# This block of code is to check if the API response was successful
if response.status_code == 200: 
    print(f"Request Successful!")
else:
    print(f"Error: {response.status_code}")
    
data = response.json()