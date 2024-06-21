-- Script to create table id_not_null if it doesn't exist

-- Check if the table id_not_null exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- This line ensures that the table will have the two columns and their requirements
