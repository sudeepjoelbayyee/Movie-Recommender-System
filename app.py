import streamlit as st
import pickle
import pandas
import requests

def fetch_details(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=d78aa3db65bfea81ee182b224fcb06fb&language=en-US".format(movie_id))
    data = response.json()
    poster_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    movie_url = f"https://www.themoviedb.org/movie/{movie_id}"
    return poster_url, movie_url

movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_urls = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['movie_id']
        poster_url, movie_url = fetch_details(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(poster_url)
        recommended_movies_urls.append(movie_url)
    
    return recommended_movies, recommended_movies_posters, recommended_movies_urls

st.title("Movie Recommender System")

selected_movie_name = st.selectbox("Movies List",movies_list)

if st.button('Recommend'):
    names, posters,urls = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]

    for i, col in enumerate(columns):
        with col:
            st.markdown(f'<a href="{urls[i]}" target="_blank"><img src="{posters[i]}" alt="{names[i]}" style="width:100%;"></a>', unsafe_allow_html=True)
            st.text(names[i])