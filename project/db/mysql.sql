create database pensamiento_computacional character set utf8;
use pensamiento_computacional;

CREATE TABLE cuatrimestre (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    description CHAR(50) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=INNODB;

CREATE TABLE alumno (
    cuit CHAR(11) NOT NULL,
    nombre CHAR(100) NOT NULL,
    cuatrimestre_id INT NOT NULL,
    registrado BOOLEAN DEFAULT false,
    estado INT NOT NULL,
    discord_id CHAR(30),
    PRIMARY KEY (cuit, cuatrimestre_id)
) ENGINE=INNODB;

