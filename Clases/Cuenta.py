from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from .conexion import Base

class Cuenta(Base):
    __tablename__ = 'mae_cuenta'

    nro_cuenta = Column(String(25), primary_key=True)
    id_cliente = Column(String(8), ForeignKey('mae_cliente.id_cliente'))
    id_tipo_cuenta = Column(Integer, ForeignKey('mae_tipo_cuenta.id_tipo_cuenta'))
    saldo_actual = Column(Numeric(15, 2), nullable=False)
    fecha_apertura = Column(Date, nullable=False)
    fecha_cierre = Column(Date)
    estado_cuenta = Column(String(255), nullable=False)
    moneda = Column(Integer, nullable=False)

    cliente = relationship('Cliente', back_populates='cuentas')
    tipo_cuenta = relationship('TipoCuenta', back_populates='cuentas')

    def __repr__(self):
        return f"<Cuenta(nro_cuenta='{self.nro_cuenta}', saldo_actual={self.saldo_actual})>"

Cliente.cuentas = relationship('Cuenta', back_populates='cliente')

