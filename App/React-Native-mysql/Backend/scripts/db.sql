CREATE DATABASE IF NOT EXISTS `users`;

USE `users`;

CREATE TABLE IF NOT EXISTS  usuarios(
    id INT NOT NULL AUTO_INCREMENT,
    tittle VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)

);

INSERT INTO usuarios(tittle, description) VALUES
('task 1','some description'),
('task 2','some description2');