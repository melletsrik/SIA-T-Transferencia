from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .conexion import Base

class TipoCuenta(Base):
    __tablename__ = 'mae_tipo_cuenta'

    id_tipo_cuenta = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False)

    cuentas = relationship('Cuenta', back_populates='tipo_cuenta')

    def __repr__(self):
        return f"<TipoCuenta(id_tipo_cuenta={self.id_tipo_cuenta}, descripcion='{self.descripcion}')>"
