from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship

from clases.tipo_transferencia import TipoTransferencia
from .conexion import Base

class Transferencia(Base):
    __tablename__ = 'trs_transferencia'

    id_transferencia = Column(Integer, primary_key=True)
    id_tipo_transferencia = Column(Integer, ForeignKey('mae_tipo_transferencia.id_tipo_transferencia'))
    nro_cta_origen = Column(String(25), ForeignKey('mae_cuenta.nro_cuenta'))
    nro_cta_destino = Column(String(25), ForeignKey('mae_cuenta.nro_cuenta'))
    monto = Column(Numeric(15, 2), nullable=False)
    fecha_transferencia = Column(Date, nullable=False)
    monto_itf = Column(Numeric(15, 2), nullable=False)

    tipo_transferencia = relationship('TipoTransferencia', back_populates='transferencias')
    cuenta_origen = relationship('Cuenta', foreign_keys=[nro_cta_origen])
    cuenta_destino = relationship('Cuenta', foreign_keys=[nro_cta_destino])

    def __repr__(self):
        return f"<Transferencia(id_transferencia={self.id_transferencia}, monto={self.monto})>"

TipoTransferencia.transferencias = relationship('Transferencia', back_populates='tipo_transferencia')
