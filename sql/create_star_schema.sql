-- FAct_Table
DROP TABLE IF EXISTS fact_listings;
CREATE TABLE fact_listings AS
SELECT
id, host_id, room_type, neighbourhood_cleansed, price, availability_365, number_of_reviews, review_scores_rating
FROM listings;


--  Host_Dimension
DROP TABLE IF EXISTS dim_host;
CREATE TABLE dim_host AS
SELECT DISTINCT host_id, host_name, host_since, host_is_superhost, host_response_rate
FROM listings;


--  Location_Dimension
DROP TABLE IF EXISTS dim_location;
CREATE TABLE dim_location AS
SELECT DISTINCT neighbourhood_cleansed, latitude, longitude
FROM listings;

--  Room_Type_Dimension
DROP TABLE IF EXISTS dim_room_type;
CREATE TABLE dim_room_type AS
SELECT DISTINCT room_type
FROM listings;