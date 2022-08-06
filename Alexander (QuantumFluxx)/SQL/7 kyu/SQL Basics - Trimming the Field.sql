SELECT id, name, SPLIT_PART(characteristics, ',', 1) AS characteristic
FROM monsters
ORDER BY id