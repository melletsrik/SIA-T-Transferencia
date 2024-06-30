from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .conexion import Base

class TipoTransferencia(Base):
    __tablename__ = 'mae_tipo_transferencia'

    id_tipo_transferencia = Column(Integer, primary_key=True)
    descripcion = Column(String(100), nullable=False)

    transferencias = relationship('Transferencia', back_populates='tipo_transferencia')

    def __repr__(self):
        return f"<TipoTransferencia(id_tipo_transferencia={self.id_tipo_transferencia}, descripcion='{self.descripcion}')>"


