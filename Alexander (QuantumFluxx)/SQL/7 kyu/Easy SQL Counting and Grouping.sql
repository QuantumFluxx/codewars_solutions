SELECT race, COUNT(name) AS count
FROM demographics
GROUP BY race
ORDER BY count DESC