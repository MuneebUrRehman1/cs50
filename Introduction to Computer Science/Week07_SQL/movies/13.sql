SELECT name FROM people
JOIN stars on stars.person_id = people.id
JOIN movies on stars.movie_id = movies.id
where movies.id in
(SELECT movies.id from movies
JOIN people on stars.person_id = people.id
JOIN stars on stars.movie_id = movies.id
WHERE people.name = "Kevin Bacon"
AND people.birth = 1958 )
AND people.name != "Kevin Bacon";
