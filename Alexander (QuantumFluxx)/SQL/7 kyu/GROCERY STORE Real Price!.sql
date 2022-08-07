SELECT name, 
       weight,
       price,
       ROUND((price*1000/weight)::numeric, 2)::float AS price_per_kg 
FROM Products
ORDER BY price_per_kg ASC, 
         name ASC