from sqlalchemy import Column, Integer, String, DateTime, Enum, Text
from config.db import Base
import enum
from datetime import datetime

class TipoMaterial(str, enum.Enum):
    Canon = "Cañon"
    Computadora = "Computadora"
    Extension = "Extensión"
    Proyector = "Proyector"
    Impresora = "Impresora"
    Router = "Router"
    Monitor = "Monitor"

class Estatus(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    Mantenimiento = "Mantenimiento"
    Dañado = "Dañado"

class Subject(Base):
    __tablename__ = "tbb_materiales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipoMaterial = Column(Enum(TipoMaterial), nullable=False)
    marca = Column(String(60), nullable=False)
    modelo = Column(String(60), nullable=True)
    numeroSerie = Column(String(100), unique=True, nullable=True)
    estatus = Column(Enum(Estatus), nullable=False, default=Estatus.Disponible)
    fechaRegistro = Column(DateTime, default=datetime, nullable=False)
    fechaActualizacion = Column(DateTime, onupdate=datetime, nullable=True)
