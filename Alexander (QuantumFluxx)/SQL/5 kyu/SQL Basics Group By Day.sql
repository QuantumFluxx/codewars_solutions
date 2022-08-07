SELECT CAST(created_at AS DATE) AS day,
       description,
       COUNT(name) AS count
FROM events
WHERE name = 'trained'
GROUP BY day, description