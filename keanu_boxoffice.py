import requests
import tmdbsimple as tmdb

# I'm establishing the variables I need in order to access the Keanu Reeves Filmography on TMDb
API_KEY = '93b29bf0b851209878217fccd1d8ca1a'
base_URL = "https://api.themoviedb.org/3"
url = f"{base_URL}/person/{6384}/movie_credits?api_key={API_KEY}"
print(f"Requesting URL: {url}")
response = requests.get(url)

# This block of code is to check if the API response was successful
if response.status_code == 200: 
    try:
        movie_data = response.json()
        print(f"Request Successful!")
    except requests.exceptions.JSONDecodeError:
        print("Error: Response could not be decoded as JSON")
else:
    print(f"Error: {response.status_code}")

# Here I'm parsing the API response and preparing the data
movie_data = response.json()
# This is optional debugging (commented out after testing)
# print(movie_data)

movies = movie_data.get('cast', [])
for movie in movies:
    print(f"Title: {movie.get('title')}, Release Date: {movie.get('release_date')}, Character: {movie.get('character')}, Box Office: {movie.get('revenue')}")

