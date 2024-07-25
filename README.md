# Movie Recommender System

This project is a movie recommender system that suggests movies similar to a given movie. The system is built using Python and several machine learning libraries, including scikit-learn, nltk, gensim, and sentence_transformers.

## Dataset

The project uses the TMDB 5000 Movies dataset and the TMDB 5000 Credits dataset, which contain information about movies, including their genres, keywords, cast, and crew.

## Methodology

The system uses a content-based filtering approach to recommend movies. This means that it recommends movies similar in content to the movies the user has liked in the past.

The following steps are involved in building the recommender system:

1. **Data Cleaning and Preprocessing:** The datasets are merged, and irrelevant columns are removed. Missing values are handled, and duplicate entries are removed.
2. **Feature Engineering:** The text data in the "genres," "keywords," "cast," and "crew" columns is converted into a list of relevant keywords.
3. **Text Vectorization:** The text data is converted into numerical vectors using Word2Vec and sentence transformers.
4. **Cosine Similarity:** Cosine similarity is used to calculate the similarity between movies based on their vector representations.
5. **Recommendation Generation:** For a given movie, the system finds the movies with the highest cosine similarity scores and recommends them to the user.

## Streamlit App

A Streamlit app has been created to provide a user-friendly interface for the recommender system. The app allows users to input a movie title and receive a list of recommended movies. The recommendations are clickable links that take the user to more information about the movie.

## Files

* `movies.pkl`: Contains the preprocessed movie data.
* `similarity.pkl`: Contains the cosine similarity matrix.
* `app.py`: Contains the code for the Streamlit app.

## How to Use

1. Clone the repository.
2. Install the required libraries.
3. Run the Streamlit app using `streamlit run app.py`.
4. Enter a movie title in the app to get recommendations.
