import streamlit as st
import pickle
import pandas as pd
import requests
import urllib3
import gdown
import os
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "e55660144f725e5111f60dad55335d97"

@st.cache_resource
def load_data():
    movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movie_dict)

    if not os.path.exists("similarity.pkl"):
        with st.spinner("Model load ho raha hai... thoda wait karo ⏳"):
            gdown.download(
                "https://drive.google.com/uc?id=1gXuq7Qqkpvm8vq4COp44iPrCtoxEGmJo",
                "similarity.pkl",
                quiet=False
                fuzzy=True
            )

    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)

    try:
        response = session.get(
            url,
            params={"api_key": API_KEY},
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "application/json",
            },
            timeout=15,
            verify=True
        )
        data = response.json()
        poster_path = data.get("poster_path")
        if not poster_path:
            return None
        return "https://image.tmdb.org/t/p/w500" + poster_path

    except Exception as e:
        print(f"Error for movie {movie_id}: {e}")
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# ── App Start ──
movies, similarity = load_data()

st.title('🎬 Movie Recommender System')
selected_movie = st.selectbox('Select a movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.text("Poster unavailable")
