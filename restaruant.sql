-- Create the database
CREATE DATABASE IF NOT EXISTS restaurant_menus;

-- Use the database
USE restaurant_menus;

-- Create the table to store menu items and their prices
CREATE TABLE IF NOT EXISTS menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(255),
    price VARCHAR(255)
);
