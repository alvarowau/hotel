CREATE DATABASE IF NOT EXISTS hotel CHARACTER SET utf8mb4 COLLATE utf8mb4_spanish_ci;

USE hotel;

CREATE TABLE IF NOT EXISTS tipos_reservas (
    tipo_reserva_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    requiere_jornadas TINYINT(1) NOT NULL DEFAULT 0,
    requiere_habitaciones TINYINT(1) NOT NULL DEFAULT 0,
    PRIMARY KEY (tipo_reserva_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


CREATE TABLE IF NOT EXISTS tipos_cocina (
    tipo_cocina_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (tipo_cocina_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;



CREATE TABLE IF NOT EXISTS salones (
    salon_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    PRIMARY KEY (salon_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS clientes (
    Id INT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(255) NOT NULL,
    Apellidos VARCHAR(255) NOT NULL,
    Num_Identificacion VARCHAR(50) NOT NULL UNIQUE,
    Fec_Nac DATE,
    Pais VARCHAR(100),
    Telefono VARCHAR(20),
    email VARCHAR(255),
    Sexo VARCHAR(10),
    Menores INT,
    activo TINYINT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (Id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE IF NOT EXISTS reservas (
    reserva_id INT NOT NULL AUTO_INCREMENT,
    tipo_reserva_id INT NOT NULL,
    salon_id INT NOT NULL,
    tipo_cocina_id INT NOT NULL,
    id_cliente INT NOT NULL,
    fecha DATE NOT NULL,
    ocupacion INT NOT NULL,
    jornadas INT NOT NULL,
    habitaciones INT NOT NULL DEFAULT 0,
    PRIMARY KEY (reserva_id),
    FOREIGN KEY (id_Cliente) REFERENCES clientes(id),
    FOREIGN KEY (salon_id) REFERENCES salones(salon_id),
    FOREIGN KEY (tipo_cocina_id) REFERENCES tipos_cocina(tipo_cocina_id),
    FOREIGN KEY (tipo_reserva_id) REFERENCES tipos_reservas(tipo_reserva_id),
    UNIQUE (salon_id, fecha)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

SET foreign_key_checks = 0;

/*datos*/
INSERT INTO tipos_reservas (nombre, requiere_jornadas, requiere_habitaciones)
VALUES
    ('Banquete', 0, 0),
    ('Jornada', 0, 0),
    ('Congreso', 1, 1);

INSERT INTO tipos_cocina (nombre)
VALUES
    ('Bufé'),
    ('Carta'),
    ('Pedir cita con el chef'),
    ('No precisa');

INSERT INTO salones (nombre)
VALUES
    ('Salón Habana'),
    ('Otro Salón');

INSERT INTO clientes (Id, Nombre, Apellidos, Num_Identificacion, Fec_Nac, Pais, Telefono, email, Sexo, Menores)
VALUES
    (1, 'Iván', 'Cuartango Del Río', '2W', '2003-02-08', 'España', '416568265', 'icuartan@gmail.com', 'H', 1),
    (2, 'María Azucena', 'García Mayor', '3A', '2003-06-13', 'España', '602724480', 'mgarcía@gmail.com', 'M', 1),
    (3, 'Álvaro', 'Gómez Tejada', '4G', '2006-09-11', 'Reino Unido', '721376842', 'ágómez t@gmail.com', 'H', 0),
    (4, 'Adrián', 'Gregorio Ortiz', '5M', '2005-02-07', 'Nigeria', '659641230', 'agregori@gmail.com', 'H', 0),
    (5, 'Alonso', 'Guerrero García', '6Y', '1983-09-06', 'Somalia', '1697052230', 'aguerrer@gmail.com', 'H', 0),
    (6, 'Bilal', 'Hamdach El Amri', '7F', '2002-10-16', 'Tailandia', '393331228', 'bhamdach@gmail.com', 'M', 1),
    (7, 'Sergio', 'Lapeña Martínez', '8P', '2006-07-17', 'Irán', '726568228', 'slapeña@gmail.com', 'H', 0),
    (8, 'Pablo', 'Menéndez Mendoza', '9D', '1991-04-08', 'España', '222837147', 'pmenénde@gmail.com', 'H', 0),
    (9, 'DanielA', 'Monje Malvar', '10X', '2004-05-31', 'Colombia', '1357985817', 'dmonje m@gmail.com', 'M', 0),
    (10, 'Javier', 'Muela Mazarío', '11B', '2006-04-21', 'USA', '726775466', 'jmuela m@gmail.com', 'N', 0),
    (11, 'Raimundo Jesús Atuba', 'Nguema Ayetebe', '12N', '2003-07-08', 'España', '474131221', 'rnguema@gmail.com', 'N', 1),
    (12, 'César', 'Nicolás Carrascosa', '13J', '2000-02-26', 'España', '497856212', 'cnicolás@gmail.com', 'H', 1),
    (13, 'Borislav', 'Nikolaev Mladenov', '14Z', '2005-04-25', 'Países Bajos', '630812215', 'bnikolae@gmail.com', 'M', 1),
    (14, 'Sergio', 'Romero Tejedor', '15S', '2004-01-03', 'México', '1629071747', 'sromero@gmail.com', 'H', 1),
    (15, 'David', 'Vargas Del Santo', '16Q', '2006-11-16', 'Reino Unido', '703998180', 'dvargas@gmail.com', 'H', 0),
    (16, 'Diego', 'Barroso Torres', '1R', '2006-07-28', 'España', '711133226', 'dbarroso@gmail.com', 'H', 0);

INSERT INTO reservas (reserva_id, tipo_reserva_id, salon_id, tipo_cocina_id, id_cliente, fecha, ocupacion, jornadas, habitaciones)
VALUES
    (1, 1, 1, 1, 1, '2024-12-20', 35, 0, 0),
    (2, 2, 2, 2, 2, '2025-01-14', 2, 0, 0),
    (3, 1, 2, 1, 3, '2025-01-17', 1, 0, 0),
    (4, 2, 2, 1, 4, '2025-01-20', 3, 0, 0),
    (5, 1, 1, 2, 5, '2024-11-20', 35, 0, 0),
    (6, 1, 1, 1, 6, '2024-11-21', 3, 0, 0),
    (7, 3, 2, 3, 7, '2025-01-10', 2, 0, 0),
    (8, 1, 1, 1, 8, '2024-10-21', 1, 0, 0),
    (9, 1, 2, 1, 9, '2025-01-13', 1, 0, 0),
    (10, 3, 1, 2, 10, '2024-12-01', 3, 1, 1),
    (11, 2, 1, 2, 11, '2024-10-01', 5, 0, 0),
    (12, 2, 1, 2, 12, '2024-10-02', 5, 0, 0),
    (13, 1, 1, 2, 13, '2024-12-25', 3, 0, 0),
    (14, 2, 2, 1, 14, '2025-01-23', 3, 0, 0),
    (15, 2, 2, 1, 10, '2024-12-27', 4, 0, 0),
    (16, 2, 2, 3, 16, '2025-01-22', 4, 0, 0);

SET foreign_key_checks = 1;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES ('alvarowau', 'alvarowau');
INSERT INTO users (username, password) VALUES ('hotel', '$BRIANDA');

SELECT * FROM users
