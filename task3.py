import numpy as np
import pandas as pd

ratings = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3],
    'movie_id': [1, 2, 1, 3, 2, 4],
    'rating': [5, 3, 4, 2, 5, 4]
})

movies = pd.DataFrame({
    'movie_id': [1, 2, 3, 4],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'genre': ['Action', 'Comedy', 'Action', 'Thriller']
})

def recommend_movies_user_based(user_id):
    similar_users = ratings[ratings['user_id'] != user_id]
    user_ratings = ratings[ratings['user_id'] == user_id]
    recommendations = similar_users[~similar_users['movie_id'].isin(user_ratings['movie_id'])]
    return recommendations.groupby('movie_id')['rating'].mean().sort_values(ascending=False)

def recommend_movies_content_based(user_genre):
    return movies[movies['genre'] == user_genre]

user_id = 1
print("User-Based Recommendations:")
print(recommend_movies_user_based(user_id))

print("\nContent-Based Recommendations for Action genre:")
print(recommend_movies_content_based('Action'))
