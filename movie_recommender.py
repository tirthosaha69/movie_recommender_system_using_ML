# recommender.py

import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess the data once at startup
df = pd.read_csv('csv\movie.csv', engine='python', on_bad_lines='skip')

# Fill missing values in selected features
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    df[feature] = df[feature].fillna('')

# Combine features into a single string
combined = df['genres'] + ' ' + df['keywords'] + ' ' + df['tagline'] + ' ' + df['cast'] + ' ' + df['director']

# Vectorize the combined features
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined)

# Calculate similarity matrix
similarity = cosine_similarity(feature_vectors)

# Reset index column to avoid missing it
df = df.reset_index()


def recommend(movie_name, top_n=20):
    """
    Returns a list of top_n recommended movie titles similar to the given movie_name.
    """
    movie_name = movie_name.lower()
    list_of_all_titles = df['title'].str.lower().tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return ["No close match found for the movie. Please check the spelling."]

    close_match = find_close_match[0]
    index_of_movie = df[df['title'].str.lower() == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    i = 0

    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = df.loc[index, 'title']
        if title_from_index.lower() != close_match:  # Avoid recommending the same movie
            recommended_movies.append(title_from_index)
            i += 1
        if i >= top_n:
            break

    return recommended_movies


# response = recommend(movie_name="iron man",top_n=10)
# print(response)