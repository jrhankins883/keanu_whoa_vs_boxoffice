import requests
import tmdbsimple as tmdb
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables and API key
load_dotenv()
API_KEY = os.getenv("TMDb_API_KEY")
if not API_KEY:
    raise ValueError("TMDB API Key not found. Make sure it's set in the .env file.")

tmdb.API_KEY = API_KEY
BASE_URL = "https://api.themoviedb.org/3"
WHOA_API_URL = "https://whoa.onrender.com/whoas/ordered/1-118"

# Function to fetch movie credits from TMDb API
def fetch_tmdb_data():
    url = f"{BASE_URL}/person/{6384}/movie_credits?api_key={API_KEY}"
    print(f"Requesting URL: {url}")
    response = requests.get(url)

    if response.status_code == 200:
        try:
            # Parsing JSON response
            movie_data = response.json()
            print("Request Successful!")

            # Extracting 'cast' information
            movies = movie_data.get('cast', [])

            # Creating a DataFrame with selected columns
            columns = ['movie_id', 'title', 'release_date', 'character', 'revenue']
            refined_movies = [
                {
                    'movie_id': movie.get('id'),  # Extract movie_id
                    'title': movie.get('title'),
                    'release_date': movie.get('release_date'),
                    'character': movie.get('character'),
                    'revenue': None  # Placeholder for now
                }
                for movie in movies
            ]

            tmdb_df = pd.DataFrame(refined_movies, columns=columns)
            print("TMDb DataFrame:")
            print(tmdb_df.head())
            return tmdb_df

        except requests.exceptions.JSONDecodeError:
            print("Error: Response could not be decoded as JSON")
            return pd.DataFrame()
    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return pd.DataFrame()


# Function to fetch "Whoa API" data
def fetch_whoa_data():
    headers = {"accept": "application/json"}
    response = requests.get(WHOA_API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        unique_movies = {movie['movie']: movie for movie in data}.values()
        df = pd.DataFrame(unique_movies)
        columns_to_keep = ['movie', 'year', 'release_date', 'character', 'total_whoas_in_movie']
        return df[columns_to_keep]
    else:
        print(f"Failed to fetch data from Whoa API. Status code: {response.status_code}")
        return pd.DataFrame()

# Function to merge TMDb and Whoa API data
def merge_data(tmdb_df, whoa_df):
    combined_df = pd.merge(
        whoa_df,
        tmdb_df,
        left_on=['movie'],
        right_on=['title'],
        how='left'
    )
    return combined_df

# Function to fetch and update revenue information
def update_revenue_data(combined_df):
    revenues = []

    for index, row in combined_df.iterrows():
        movie_title = row['movie']
        movie_id = row.get('movie_id')

        if pd.isna(movie_title) or movie_id is None:
            revenues.append(None)
            print(f"Skipping movie: {movie_title} (No movie_id)")
            continue

        details_url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}"
        response = requests.get(details_url)

        if response.status_code == 200:
            movie_details = response.json()
            revenue = movie_details.get('revenue', None)
            revenues.append(revenue)
        else:
            print(f"Failed to fetch revenue for {movie_title} (ID: {movie_id})")
            revenues.append(None)

    combined_df['revenue'] = revenues
    return combined_df

# Main execution
if __name__ == "__main__":
    print("Fetching TMDb data...")
    tmdb_df = fetch_tmdb_data()

    print("Fetching Whoa API data...")
    whoa_df = fetch_whoa_data()

    if not tmdb_df.empty and not whoa_df.empty:
        print("Merging data...")
        combined_df = merge_data(tmdb_df, whoa_df)

        print("Updating revenue data...")
        combined_df = update_revenue_data(combined_df)

        output_file = "keanu_combined_data_with_revenue.csv"
        combined_df.to_csv(output_file, index=False)
        print(f"Combined data saved to {output_file}")
    else:
        print("Error: One or more data sources are empty. Aborting.")
