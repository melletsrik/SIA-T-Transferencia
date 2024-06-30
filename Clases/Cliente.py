from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from Clases import Conect
from Clases import *
import Persona

conexion = Conect()


class Cliente(conexion.Base):
    __tablename__ = 'mae_cliente'

    id_cliente = Column(String(8), primary_key=True)
    contrasenia = Column(String(20), nullable=False)
    tipo_cliente = Column(String(255), nullable=False)
    id_persona = Column(String(8), ForeignKey('mae_persona.id_persona'))

    persona = relationship('Persona', back_populates='cliente')

    def __repr__(self):
        return f"<Cliente(id_cliente='{self.id_cliente}', tipo_cliente='{self.tipo_cliente}')>"

Persona.cliente = relationship('Cliente', uselist=False, back_populates='persona')