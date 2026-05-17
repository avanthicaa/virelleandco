CREATE DATABASE virelle;

USE virelle;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255)
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    price DECIMAL(10,2),
    image VARCHAR(255)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    address TEXT,
    payment_method VARCHAR(100),
    total DECIMAL(10,2)
);

INSERT INTO products(name, description, price, image)
VALUES
(
'Virelle Signature Ritual Kit',
'Luxury mehendi ritual kit including 4 premium cones, essential oil, aftercare balm, sealant spray, mehendi dip and designer stencils.',
249,
'signature-kit.jpg'
);