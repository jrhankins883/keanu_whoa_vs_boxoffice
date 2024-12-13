import requests

# Your TMDb API key
API_KEY = '93b29bf0b851209878217fccd1d8ca1a'

# Keanu Reeves's ID
keanu_id = 6384

# Step 1: Get Keanu's movies
movies_url = f"https://api.themoviedb.org/3/person/{keanu_id}/movie_credits?api_key={API_KEY}"
response = requests.get(movies_url)

if response.status_code == 200:
    movie_data = response.json()
    print("Keanu Reeves's Movies and Revenue:")
    
    # Step 2: Loop through each movie and get details
    for movie in movie_data['cast']:
        movie_id = movie.get('id')
        title = movie.get('title', 'Unknown Title')
        release_date = movie.get('release_date', 'Unknown Release Date')

        # Fetch movie details for revenue
        movie_details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        details_response = requests.get(movie_details_url)

        if details_response.status_code == 200:
            details = details_response.json()
            revenue = details.get('revenue', 'No Revenue Data')
            print(f"{title} ({release_date}) - Revenue: ${revenue:,}")
        else:
            print(f"Failed to fetch details for {title} ({movie_id})")
else:
    print(f"Error fetching movies: {response.status_code}")
