SELECT name, greeting, REPLACE(SUBSTRING(greeting, '#[\d]+'), '#', '') AS user_id
FROM greetings