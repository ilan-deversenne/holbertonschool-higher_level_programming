-- List values of second_table ordered by score desc (only 10 and high)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
