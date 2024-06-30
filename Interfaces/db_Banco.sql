    CREATE TABLE mae_Persona (
      id_persona integer PRIMARY KEY,
      nombre varchar(20) NOT NULL,
      apellido varchar(20) NOT NULL,
      fechaNacimiento date NOT NULL,
      correo varchar(30) NOT NULL,
      telefono varchar(12) NOT NULL,
      direccion varchar(100) NOT NULL
    );

    CREATE TABLE mae_Cliente (
      id_cliente integer PRIMARY KEY,
      id_persona integer UNIQUE,
      contrasenia varchar(30) NOT NULL,
      tipo_cliente varchar(20) NOT NULL
    );

    CREATE TABLE mae_Cuenta (
      numero_cuenta varchar(30) UNIQUE PRIMARY KEY,
      id_cliente integer,
      tipo_cuenta varchar(50) NOT NULL,
      saldo_actual float NOT NULL,
      fecha_apertura date NOT NULL,
      fecha_cierre date,
      estado_cuenta varchar(20) NOT NULL,
      moneda varchar(10) NOT NULL
    );

    CREATE TABLE mae_tipo_transferencia (
      id_tipo_transferencia integer PRIMARY KEY,
      descripcion varchar(50)
    );

    CREATE TABLE trs_transferencia (
      id serial PRIMARY KEY,
      id_tipo_transferencia integer NOT NULL,
      numero_cuenta_origen varchar(50) NOT NULL,
      numero_cuenta_destino varchar(50) NOT NULL,
      monto numeric NOT NULL,
      fecha_transferencia date NOT NULL
    );

    ALTER TABLE mae_Cliente ADD FOREIGN KEY (id_persona) REFERENCES mae_Persona (id_persona);

    ALTER TABLE mae_Cuenta ADD FOREIGN KEY (id_cliente) REFERENCES mae_Cliente (id_cliente);

    ALTER TABLE trs_transferencia ADD FOREIGN KEY (id_tipo_transferencia) REFERENCES mae_tipo_transferencia (id_tipo_transferencia);

    ALTER TABLE trs_transferencia ADD FOREIGN KEY (numero_cuenta_origen) REFERENCES mae_Cuenta (numero_cuenta);

    ALTER TABLE trs_transferencia ADD FOREIGN KEY (numero_cuenta_destino) REFERENCES mae_Cuenta (numero_cuenta);
