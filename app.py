import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movies_id):
    data = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d78aa3db65bfea81ee182b224fcb06fb&language=en-US'.format(movies_id)).json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.title("Movie Recommender System")

selected_movie = st.selectbox("Select",movies['title'].values)

if st.button("Recommend"):
    recommendations,posters = recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])


