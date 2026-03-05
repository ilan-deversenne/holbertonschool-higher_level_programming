-- Create database hbtn_0d_usa if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table cities if not exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id int PRIMARY KEY AUTO_INCREMENT,
    state_id int,
    name varchar(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
)
