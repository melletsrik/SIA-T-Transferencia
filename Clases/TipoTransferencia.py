from sqlalchemy import Column, String, Integer
from Clases import Conect
from Clases import *

conexion = Conect()

class TipoTransferencia(conexion.Base):
    __tablename__ = 'mae_tipo_transferencia'

    id_tipo_transferencia = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<TipoTransferencia(id_tipo_transferencia={self.id_tipo_transferencia}, descripcion='{self.descripcion}')>"