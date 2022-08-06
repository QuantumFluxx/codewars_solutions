SELECT id, name, quality1, quality2
FROM students
WHERE (quality1 = 'evil' AND quality2 = 'cunning') 
  OR (quality1 = 'brave' AND quality2 != 'evil')
  OR (quality1 = 'studious' OR quality2 = 'intelligent')
  OR (quality1 = 'hufflepuff' OR quality2 = 'hufflepuff')
ORDER BY id ASC;