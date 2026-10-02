import streamlit as st
import pickle
import requests
API_KEY = st.secrets["TMDB_API_KEY"]


# -----------------------------
# Load saved recommendation data
# -----------------------------
movies = pickle.load(open("model/movie_list.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))


# -----------------------------
# TMDB API
# -----------------------------



def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path

    return None


# -----------------------------
# Recommendation function
# -----------------------------
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]]["movie_id"]

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and get 5 similar movie recommendations."
)


# Movie selection
selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)


# Recommendation button
if st.button("Recommend Movies"):

    with st.spinner("Finding recommendations..."):

        names, posters = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):

        with col:

            if poster:
                st.image(poster, use_container_width=True)

            st.write(name)