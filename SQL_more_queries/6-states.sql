-- Create database hbtn_0d_usa if not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create table states if not exists
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(256) NOT NULL
)
