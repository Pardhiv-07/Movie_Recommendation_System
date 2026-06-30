import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --- 1. SET UP A RESILIENT NETWORK SESSION ---
# This opens a single, stable connection and automatically retries if a drop occurs
session = requests.Session()
# Retry up to 3 times, waiting a bit longer between each try (0.5s, 1s, 2s)
retry = Retry(connect=3, read=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)
session.mount('https://', adapter)

# --- 2. LOAD PRECOMPUTED ARTIFACTS ---
movies_dict = pickle.load(open("models/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("models/similarity.pkl", "rb"))


def fetch_poster(movie_id):
    """Fetches the poster using our stable Session."""
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        # Use session.get instead of requests.get!
        response = session.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://placehold.co/500x750/2a2a2a/ffffff.png?text=No+Poster+Available"

    except requests.exceptions.RequestException as e:
        print(f"Network error fetching poster for ID {movie_id}: {e}")
        return "https://placehold.co/500x750/2a2a2a/ffffff.png?text=Network+Error"


def get_recommendations(movie_title):
    """Returns a list of dictionaries containing top 5 recommended movie titles and posters."""
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            title = movies.iloc[i[0]].title
            poster = fetch_poster(movie_id)

            recommended_movies.append({
                'title': title,
                'poster': poster
            })

        return recommended_movies
    except IndexError:
        return []


def get_movie_list():
    """Returns an array of all movie titles for the HTML dropdown."""
    return movies['title'].values