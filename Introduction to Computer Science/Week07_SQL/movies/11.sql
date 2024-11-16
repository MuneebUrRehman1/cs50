SELECT title FROM movies
JOIN ratings on movies.id = ratings.movie_id
JOIN stars on stars.movie_id = movies.id
JOIN people on people.id = stars.person_id
WHERE people.name = 'Chadwick Boseman'
ORDER BY ratings.rating DESC LIMIT 5;
