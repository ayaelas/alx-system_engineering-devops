-- Create a dt
-- Create a table
CREATE DATABASE IF NOT EXISTS tyrell_corp;

CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6
(
        id INT UNIQUE AUTO_INCREMENT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id)
);

INSERT INTO tyrell_corp.nexus6 (name) VALUES ("ElHoussain");

GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

