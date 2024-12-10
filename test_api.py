# Cell 1
import requests
import tmdbsimple as tmdb
import pandas as pd

from dotenv import load_dotenv
import os

# This loads the environment variables from the .env file
load_dotenv()

# This retrieves the API Key
API_KEY = os.getenv("TMDb_API_KEY")

if not API_KEY:
    raise ValueError("TMDB API Key not found. Make sure it's set in the .env file.")

# Cell 2
# Set the TMDb API Key for tmdbsimple
tmdb.API_KEY = API_KEY
base_URL = "https://api.themoviedb.org/3"
url = f"{base_URL}/person/{6384}/movie_credits?api_key={API_KEY}"

print(f"Requesting URL: {url}")
response = requests.get(url)

# Cell 3
# Checking the response status
if response.status_code == 200: 
    try:
        # Parsing JSON response 
        movie_data = response.json()
        print(f"Request Successful!")
        # Extracting 'cast' information and creating a DataFrame
        movies = movie_data.get('cast', [])
        df = pd.DataFrame(movies)
        # Displaying the first few rows of the DataFrame
        print(df.head())
    except requests.exceptions.JSONDecodeError:
        print("Error: Response could not be decoded as JSON")
else:
    print(f"Error: {response.status_code} - {response.reason}")
    
# Cell 4
    columns = ['title', 'release_date', 'character', 'revenue']
refined_movies = []

for movie in movies:
    refined_movies.append({
        'title': movie.get('title'),
        'release_date': movie.get('release_date'),
        'character': movie.get('character'),
        'revenue': movie.get('revenue')
    })
    
df_refined = pd.DataFrame(refined_movies, columns=columns)
print(df_refined[:5])


# Cell 5 - This starts the API call for the Whoa API
whoa_base_url = "https://whoa.onrender.com/"
# I will adjust this based on API needs
endpoint = "whoas/random"

# Cell 6
response = requests.get(f"{whoa_base_url}{endpoint}")
if response.status_code == 200:
    try:
        whoa_data = response.json()
        print("Data Retrieved Successfully")
    except requests.exceptions.JSONDecodeError:
        print("Error decoding JSON response")
else:
    print(f"Error: {response.status_code} - {response.reason}")
    
# Cell 7
whoa_movies = []
for item in whoa_data:
    whoa_movies.append({
        'movie': item.get('movie'),
        'year': item.get('year'),
        'release_date': item.get('release_date'),
        'character': item.get('character'),
        'total_whoas_in_movie': item.get('total_whoas_in_movie')
    })

# Covert to DataFrame
df_whoa = pd.DataFrame(whoa_movies, columns=['movie', 'year', 'release_date', 'character', 'total_whoas_in_movie'])
print(df_whoa.head())