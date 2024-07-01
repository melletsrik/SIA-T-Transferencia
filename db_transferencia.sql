CREATE TABLE mae_persona (
    id_persona VARCHAR(8) PRIMARY KEY NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    correo VARCHAR(255) NOT NULL,
    telefono VARCHAR(9) NOT NULL,
    direccion VARCHAR(255) NOT NULL
);

CREATE TABLE mae_cliente (
    id_cliente VARCHAR(8) PRIMARY KEY NOT NULL,
    contrasenia VARCHAR(20) NOT NULL,
    tipo_cliente VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES mae_persona (id_persona)
);

CREATE TABLE mae_tipo_cuenta (
    id_tipo_cuenta INT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE mae_tipo_transferencia (
    id_tipo_transferencia SERIAL PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE mae_tipo_moneda (
    id_moneda INT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE mae_cuenta (
    nro_cuenta VARCHAR(25) PRIMARY KEY NOT NULL,
    id_cliente VARCHAR(8) NOT NULL,
    id_tipo_cuenta INT NOT NULL,
    saldo_actual NUMERIC(15, 2) NOT NULL,
    fecha_apertura DATE NOT NULL,
    fecha_cierre DATE,
    estado_cuenta VARCHAR(255) NOT NULL,
    id_moneda INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES mae_cliente (id_cliente),
    FOREIGN KEY (id_tipo_cuenta) REFERENCES mae_tipo_cuenta (id_tipo_cuenta),
    FOREIGN KEY (id_moneda) REFERENCES mae_tipo_moneda (id_moneda)
);

CREATE TABLE trs_transferencia (
    id_transferencia SERIAL PRIMARY KEY,
    id_tipo_transferencia INT NOT NULL,
    nro_cta_origen VARCHAR(25) NOT NULL,
    nro_cta_destino VARCHAR(25) NOT NULL,
    monto NUMERIC(15, 2) NOT NULL,
    fecha_transferencia DATE NOT NULL,
    monto_itf NUMERIC(15, 2) NOT NULL,
    FOREIGN KEY (nro_cta_origen) REFERENCES mae_cuenta (nro_cuenta),
    FOREIGN KEY (id_tipo_transferencia) REFERENCES mae_tipo_transferencia (id_tipo_transferencia),
    FOREIGN KEY (nro_cta_destino) REFERENCES mae_cuenta (nro_cuenta)
);

-- Crear trigger para calcular el ITF automáticamente
CREATE OR REPLACE FUNCTION calculate_itf_before_insert() 
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.monto >= 1000 THEN
        NEW.monto_itf = NEW.monto * 0.00005; -- Ejemplo: ITF del 0.5%
    ELSE
        NEW.monto_itf = 0;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER calculate_itf_before_insert
BEFORE INSERT ON trs_transferencia
FOR EACH ROW
EXECUTE FUNCTION calculate_itf_before_insert();

INSERT INTO mae_persona (id_persona, nombre, apellido, fecha_nacimiento, correo, telefono, direccion) VALUES
('12345678', 'Napoleon', 'Perez', '1985-07-23', 'juan.perez@example.com', '987654321', 'Av. Siempre Viva 123, Lima'),
('98765432', 'Maria', 'Lopez', '1990-11-15', 'maria.lopez@example.com', '912345678', 'Calle Falsa 456, Arequipa');

INSERT INTO mae_cliente (id_cliente, contrasenia, tipo_cliente) VALUES
('98765432', 'pass1234', 'individual'),
('12345678', 'pass5678', 'empresarial');

INSERT INTO mae_tipo_cuenta (id_tipo_cuenta, descripcion) VALUES
(1, 'Cuenta de Ahorros'),
(2, 'Cuenta Corriente');

INSERT INTO mae_tipo_transferencia (descripcion) VALUES
('Transferencia a otra cuenta'),
('Transferencia a una cuenta propia');

INSERT INTO mae_tipo_moneda (id_moneda, descripcion) VALUES
(1, 'Soles'),
(2, 'Dólares');

INSERT INTO mae_cuenta (nro_cuenta, id_cliente, id_tipo_cuenta, saldo_actual, fecha_apertura, fecha_cierre, estado_cuenta, id_moneda) VALUES
('123456789012345', '12345678', 1, 1500.50, '2020-01-15', NULL, 'activa', 1),
('987654321098765', '98765432', 2, 25000.00, '2019-05-23', NULL, 'activa', 1),
('987654321098766', '98765432', 1, 5000.00, '2020-07-10', NULL, 'activa', 1);

INSERT INTO trs_transferencia (id_tipo_transferencia, nro_cta_origen, nro_cta_destino, monto, fecha_transferencia, monto_itf) VALUES
(1, '123456789012345', '987654321098765', 1200.00, '2024-06-15', 6.00), -- Transferencia a cuenta de tercero en el mismo banco
(2, '987654321098765', '123456789012345', 950.00, '2024-06-18', 0.00), -- Transferencia a otra cuenta propia en el mismo banco
(2, '987654321098766', '987654321098765', 1000.00, '2024-06-20', 5.00); -- Transferencia a otra cuenta propia en el mismo banco
