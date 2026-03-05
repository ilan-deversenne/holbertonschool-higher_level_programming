-- Create table unique_id where id is unique
CREATE TABLE IF NOT EXISTS unique_id (
    id int UNIQUE DEFAULT 1,
    name varchar(256)
)
