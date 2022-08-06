SELECT RANK() OVER (ORDER BY SUM(points) DESC) as rank,
       COALESCE(NULLIF(clan, ''), '[no clan specified]') as clan,
       SUM(points) AS total_points,
       COUNT(name) AS total_people
FROM people
GROUP BY clan