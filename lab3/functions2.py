#1
 def is_good_movie(movie_title, imdb_score):
    if imdb_score > 5.5:
        return True
    else:
        return False
#2
def movies_by_category(movies, category):
    return [(movie_title, movie_category) for movie_title, movie_category in movies if movie_category == category]

#3
def average_imdb_score(movies):
    if not movies:
        return 0.0 

    total_score = sum(imdb_score for _, imdb_score in movies)
    num_movies = len(movies)
    return total_score / num_movies

#4
def compute_average_imdb_score(category, movie_data):
    total_score = 0
    num_movies = 0
    for movie in movie_data:
        if movie['category'] == category:
            total_score += movie['imdb_score']
            num_movies += 1
    if num_movies == 0:
        return 0 
    else:
        return total_score / num_movies

#5
def compute_average_imdb_score(movies):
    total_score = 0
    num_movies = len(movies)
    for movie in movies:
        total_score += movie['imdb_score']
    if num_movies == 0:
        return 0 
    else:
        return total_score / num_movies
