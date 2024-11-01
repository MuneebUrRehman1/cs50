SELECT movies.title, ratings.rating
FROM movies JOIN ratings on movies.id = ratings.movie_id
WHERE movies.year = 2012
ORDER BY ratings.rating DESC, movies.title ASC;
