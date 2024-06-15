CREATE TABLE `Persona` (
  `idPersona` integer PRIMARY KEY,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `correo` varchar(255) NOT NULL,
  `numeroTel` varchar(15) NOT NULL,
  `direccion` varchar(255) NOT NULL
);

CREATE TABLE `Cliente` (
  `idCliente` integer PRIMARY KEY,
  `idPersona` integer NOT NULL,
  `tipoCliente` varchar(20) NOT NULL,
  FOREIGN KEY (`idPersona`) REFERENCES `Persona` (`idPersona`),
  UNIQUE (`idPersona`) -- Un cliente no puede estar asociado a más de una persona
);

CREATE TABLE `Cuenta` (
  `idCuenta` integer PRIMARY KEY,
  `idCliente` integer NOT NULL,
  `numeroCta` varchar(255) NOT NULL UNIQUE,
  `tipoCta` varchar(255) NOT NULL,
  `balanceActual` decimal(10, 2) NOT NULL,
  `fechaCreacion` timestamp NULL,
  `fechaCierre` timestamp NULL,
  `estadoCta` varchar(255) NOT NULL, -- Puede estar activa, suspendida, cerrada o bloqueada
  FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`)
);

CREATE TABLE `TipoTransferencia` (
  `idTipoTransfer` integer PRIMARY KEY,
  `descripcion` varchar(255) NOT NULL
);

CREATE TABLE `TRS_Transferencia` (
  `idTransferencia` integer PRIMARY KEY,
  `idCuenta` integer NOT NULL,
  `idTipoTransfer` integer NOT NULL,
  `monto` decimal(10, 2) NOT NULL,
  `fechaTransfer` datetime NOT NULL,
  FOREIGN KEY (`idCuenta`) REFERENCES `Cuenta` (`idCuenta`),
  FOREIGN KEY (`idTipoTransfer`) REFERENCES `TipoTransferencia` (`idTipoTransfer`)
);

-- REGISTROS DE PRUEBA
INSERT INTO `Persona` (`idPersona`, `nombre`, `apellido`, `fechaNacimiento`, `correo`, `numeroTel`, `direccion`) VALUES
(11111111, 'Napoleón', 'Pérez', '1980-05-15', 'napoleon.perez@gmail.com', '555-1234', 'Calle Melgar 123'),
(22222222, 'Alexia', 'García', '1992-07-20', 'alexia.garcia@gmail.com', '555-5678', 'Avenida Siempre Viva 456'),
(33333333, 'Charles', 'Rosas', '1985-03-10', 'charles.rosasz@gmail.com', '555-8765', 'Calle Luna 789');

INSERT INTO `Cliente` (`idCliente`, `idPersona`, `tipoCliente`) VALUES
(1, 11111111, 'Individual'),
(2, 22222222, 'Individual'),
(3, 33333333, 'Corporativo');

INSERT INTO `Cuenta` (`idCuenta`, `idCliente`, `numeroCta`, `tipoCta`, `balanceActual`, `fechaCreacion`, `fechaCierre`, `estadoCta`) VALUES
(1, 1, '1001-2345-6789', 'Ahorros', 1500.50, '2020-01-01 10:00:00', NULL, 'Activa'),
(2, 2, '2002-3456-7890', 'Corriente', 2500.75, '2019-06-15 14:30:00', NULL, 'Activa'),
(3, 3, '3003-4567-8901', 'Ahorros', 5000.00, '2018-11-20 09:00:00', NULL, 'Activa');

INSERT INTO `TipoTransferencia` (`idTipoTransfer`, `descripcion`) VALUES
(1, 'Transferencia entre cuentas del mismo banco'),
(2, 'Transferencia interbancaria');

INSERT INTO `TRS_Transferencia` (`idTransferencia`, `idCuenta`, `idTipoTransfer`, `monto`, `fechaTransfer`) VALUES
(1, 1, 1, 100.50, '2024-01-10 10:15:00'),
(2, 2, 2, 200.75, '2024-02-20 12:30:00'),
(3, 3, 2, 300.00, '2024-03-15 14:45:00'),
(4, 1, 2, 150.25, '2024-04-10 16:00:00'),
(5, 2, 1, 250.50, '2024-05-05 11:00:00');
