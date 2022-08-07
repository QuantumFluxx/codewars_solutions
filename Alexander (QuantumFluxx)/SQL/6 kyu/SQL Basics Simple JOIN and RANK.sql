SELECT RANK() OVER (ORDER BY COUNT(people.id)) as sale_rank, 
       people.id,
       people.name,
       COUNT(sales.people_id) AS sale_count
FROM people
LEFT JOIN sales
ON people.id = sales.people_id
GROUP BY people.id