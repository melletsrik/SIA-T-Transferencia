from sqlalchemy import Column, String, Integer
from Clases import Conect
from Clases import *

conexion = Conect()

class TipoCuenta(conexion.Base):
    __tablename__ = 'mae_tipo_cuenta'

    id_tipo_cuenta = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<TipoCuenta(id_tipo_cuenta={self.id_tipo_cuenta}, descripcion='{self.descripcion}')>"