# (1)
SELECT
neighbourhood_cleansed,
ROUND(AVG(price),2) AS average_price
FROM listings
GROUP BY neighbourhood_cleansed
ORDER BY average_price DESC
LIMIT 10;

# (2)
SELECT
room_type,
COUNT(*) AS listings
FROM listings
GROUP BY room_type
ORDER BY listings DESC;

# (3)
SELECT
host_is_superhost,
ROUND(AVG(price),2) AS average_price
FROM listings
GROUP BY host_is_superhost;

# (4)
SELECT
property_type,
COUNT(*) AS total
FROM listings
GROUP BY property_type
ORDER BY total DESC
LIMIT 15;