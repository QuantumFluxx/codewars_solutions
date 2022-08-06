SELECT 
  s.id,
  COALESCE(NULLIF(s.name, ''), '[product name not found]') AS name,
  s.price,
  COALESCE(NULLIF(s.card_name, ''), '[card name not found]') AS card_name,
  s.card_number,
  s.transaction_date
FROM eusales AS s
WHERE s.price > 50