from clases import Conexion, Persona, Cliente, TipoCuenta, TipoTransferencia, Cuenta, Transferencia

# Crear todas las tablas en la base de datos, si no existen
conexion = Conexion()
conexion.Base.metadata.create_all(conexion.engine)

# Crear una sesión para interactuar con la base de datos
db = next(conexion.get_db())

# Ejemplo de uso: insertar datos en las tablas
# Insertar clientes
cliente1 = Cliente(id_cliente='12345678', contrasenia='pass5678', tipo_cliente='empresarial')
cliente2 = Cliente(id_cliente='98765432', contrasenia='pass1234', tipo_cliente='individual')

db.add_all([cliente1, cliente2])
db.commit()

# Insertar tipos de cuenta
tipo_cuenta1 = TipoCuenta(id_tipo_cuenta=1, descripcion='Cuenta de Ahorros')
tipo_cuenta2 = TipoCuenta(id_tipo_cuenta=2, descripcion='Cuenta Corriente')

db.add_all([tipo_cuenta1, tipo_cuenta2])
db.commit()

# Insertar tipos de transferencia
tipo_transferencia1 = TipoTransferencia(descripcion='Transferencia a otra cuenta')
tipo_transferencia2 = TipoTransferencia(descripcion='Transferencia a una cuenta propia')

db.add_all([tipo_transferencia1, tipo_transferencia2])
db.commit()

# Insertar cuentas
cuenta1 = Cuenta(nro_cuenta='123456789012345', id_cliente='12345678', id_tipo_cuenta=1,
                saldo_actual=1500.50, fecha_apertura='2020-01-15', estado_cuenta='activa', moneda=1)
cuenta2 = Cuenta(nro_cuenta='987654321098765', id_cliente='98765432', id_tipo_cuenta=2,
                saldo_actual=25000.00, fecha_apertura='2019-05-23', estado_cuenta='activa', moneda=1)

db.add_all([cuenta1, cuenta2])
db.commit()

# Insertar transferencias
transferencia1 = Transferencia(id_tipo_transferencia=1, nro_cta_origen='123456789012345',
                               nro_cta_destino='987654321098765', monto=1200.00,
                               fecha_transferencia='2024-06-15', monto_itf=6.00)
transferencia2 = Transferencia(id_tipo_transferencia=2, nro_cta_origen='987654321098765',
                               nro_cta_destino='123456789012345', monto=950.00,
                               fecha_transferencia='2024-06-18', monto_itf=0.00)

db.add_all([transferencia1, transferencia2])
db.commit()

# Cerrar la sesión al finalizar
db.close()
