# MySahayak MySQL Table Creation Script
# Run this in your MySQL client to create the required table

CREATE DATABASE IF NOT EXISTS mysahayak;
USE mysahayak;

CREATE TABLE IF NOT EXISTS contact_messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    role VARCHAR(100),
    message TEXT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
