from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from config.db import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    ACTIVO = "Activo"
    DEVUELTO = "Devuelto"
    VENCIDO = "Vencido"

class Loan(Base):
    __tablename__ = "tbb_prestamos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, nullable=False)
    id_material = Column(Integer, nullable=False)
    fecha_prestamo = Column(DateTime, nullable=False)
    fecha_devolucion = Column(DateTime, nullable=False)
    estado_prestamo = Column(Enum(EstadoPrestamo), nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    fecha_actualizacion = Column(DateTime, nullable=True)
