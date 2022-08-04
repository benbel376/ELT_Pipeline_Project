# create databases
CREATE DATABASE IF NOT EXISTS `warehouse`;
CREATE DATABASE IF NOT EXISTS `test`;

# create root user and grant rights
CREATE USER 'mysql'@'localhost' IDENTIFIED BY 'mysql';
GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'%';

CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';