-- List score values in second_table score ordered desc and grouped  
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
