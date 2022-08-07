SELECT id,
       NETWORK(ip_address) as first_address, 
       BROADCAST(ip_address) as last_address 
FROM connections