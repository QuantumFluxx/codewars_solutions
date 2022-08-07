SELECT people.id,
       people.name,
       COUNT(toys.id) AS toy_count
FROM people
LEFT JOIN toys
ON people.id = toys.people_id
GROUP BY people.id