-- List cities where state is California with a sub query
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id;
