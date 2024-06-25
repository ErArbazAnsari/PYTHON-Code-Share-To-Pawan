import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample movie data
data = {
    'Title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'Genre': ['Drama', 'Crime, Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Initialize CountVectorizer to convert text data (genre) into numerical features
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['Genre'])

# Compute cosine similarity between movie genres
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Function to get movie recommendations based on similarity
def get_recommendations(title, cosine_similarities):
    movie_index = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_similarities[movie_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar movies
    movie_indices = [score[0] for score in sim_scores]
    return df['Title'].iloc[movie_indices].values

# Get movie recommendations for a given title
movie_title = 'The Godfather'
recommendations = get_recommendations(movie_title, cosine_sim)
print(f"Recommended movies for '{movie_title}': {', '.join(recommendations)}")

