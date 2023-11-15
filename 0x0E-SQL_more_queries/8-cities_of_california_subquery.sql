-- Listing cities
SELECT id, name
FROM cities
WHERE state_id = 1
GROUP BY id
ORDER BY id;
