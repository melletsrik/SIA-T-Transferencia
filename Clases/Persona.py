from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
import Conect

conexion = Conect()

class Persona(conexion.Base):
    __tablename__ = 'mae_persona'

    id_persona = Column(String(8), primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    correo = Column(String(255), nullable=False)
    telefono = Column(String(9), nullable=False)
    direccion = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<Persona(id_persona='{self.id_persona}', nombre='{self.nombre}', apellido='{self.apellido}')>"
