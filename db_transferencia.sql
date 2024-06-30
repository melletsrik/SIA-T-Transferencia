CREATE TABLE mae_persona (
  id_persona integer PRIMARY KEY,
  nombre varchar(100) NOT NULL,
  apellido varchar(100) NOT NULL,
  fecha_nacimiento date NOT NULL,
  correo varchar(255) NOT NULL,
  numero_tel varchar(15) NOT NULL,
  direccion varchar(255) NOT NULL
);

CREATE TABLE mae_cliente (
  id_cliente integer PRIMARY KEY,
  id_persona integer NOT NULL,
  tipo_cliente varchar(20) NOT NULL,
  FOREIGN KEY (id_persona) REFERENCES mae_persona (id_persona),
  UNIQUE (id_persona) -- Un cliente no puede estar asociado a más de una persona
);

CREATE TABLE mae_cuenta (
  id_cuenta integer PRIMARY KEY,
  id_cliente integer NOT NULL,
  numero_cuenta varchar(255) NOT NULL UNIQUE,
  tipo_cuenta varchar(255) NOT NULL,
  balance_actual decimal(10, 2) NOT NULL,
  fecha_creacion timestamp NULL,
  fecha_cierre timestamp NULL,
  estado_cuenta varchar(255) NOT NULL, -- Puede estar activa, suspendida, cerrada o bloqueada
  FOREIGN KEY (id_cliente) REFERENCES mae_cliente (id_cliente)
);

CREATE TABLE mae_tipo_transferencia (
  id_tipo_transfer integer PRIMARY KEY,
  descripcion varchar(255) NOT NULL
);

CREATE TABLE trs_transferencia (
  id_transferencia integer PRIMARY KEY,
  id_cuenta integer NOT NULL,
  id_tipo_transfer integer NOT NULL,
  monto decimal(10, 2) NOT NULL,
  fecha_transfer datetime NOT NULL,
  FOREIGN KEY (id_cuenta) REFERENCES mae_cuenta (id_cuenta),
  FOREIGN KEY (id_tipo_transfer) REFERENCES mae_tipo_transferencia (id_tipo_transfer)
);

-- REGISTROS DE PRUEBA PARA TABLAS RENOMBRADAS
INSERT INTO mae_persona (id_persona, nombre, apellido, fecha_nacimiento, correo, numero_tel, direccion) VALUES
(11111111, 'Napoleón', 'Pérez', '1980-05-15', 'napoleon.perez@gmail.com', '555-1234', 'Calle Melgar 123'),
(22222222, 'Alexia', 'García', '1992-07-20', 'alexia.garcia@gmail.com', '555-5678', 'Avenida Siempre Viva 456'),
(33333333, 'Charles', 'Rosas', '1985-03-10', 'charles.rosasz@gmail.com', '555-8765', 'Calle Luna 789');

INSERT INTO mae_cliente (id_cliente, id_persona, tipo_cliente) VALUES
(1, 11111111, 'Individual'),
(2, 22222222, 'Individual'),
(3, 33333333, 'Corporativo');

INSERT INTO mae_cuenta (id_cuenta, id_cliente, numero_cuenta, tipo_cuenta, balance_actual, fecha_creacion, fecha_cierre, estado_cuenta) VALUES
(1, 1, '1001-2345-6789', 'Ahorros', 1500.50, '2020-01-01 10:00:00', NULL, 'Activa'),
(2, 2, '2002-3456-7890', 'Corriente', 2500.75, '2019-06-15 14:30:00', NULL, 'Activa'),
(3, 3, '3003-4567-8901', 'Ahorros', 5000.00, '2018-11-20 09:00:00', NULL, 'Activa');

INSERT INTO mae_tipo_transferencia (id_tipo_transfer, descripcion) VALUES
(1, 'Transferencia entre cuentas del mismo banco'),
(2, 'Transferencia interbancaria');

INSERT INTO trs_transferencia (id_transferencia, id_cuenta, id_tipo_transfer, monto, fecha_transfer) VALUES
(1, 1, 1, 100.50, '2024-01-10 10:15:00'),
(2, 2, 2, 200.75, '2024-02-20 12:30:00'),
(3, 3, 2, 300.00, '2024-03-15 14:45:00'),
(4, 1, 2, 150.25, '2024-04-10 16:00:00'),
(5, 2, 1, 250.50, '2024-05-05 11:00:00');


