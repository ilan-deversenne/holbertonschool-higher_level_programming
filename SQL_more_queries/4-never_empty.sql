-- Create table id_not_null if doesn't exist where id can't be null
CREATE TABLE IF NOT EXISTS id_not_null (
    id int DEFAULT 1,
    name varchar(256)
)
