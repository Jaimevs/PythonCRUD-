from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum

# Definición de enumeraciones para tipo de usuario y estatus
class TipoUsuario(str, enum.Enum):
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Directivo = "Directivo"
    Administrativo = "Administrativo"

class Estatus(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

# Definición del modelo de usuario
class User(Base):
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    primerApellido = Column(String(60), nullable=False)
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario), nullable=False)
    nombreUsuario = Column(String(60), unique=True, nullable=False)
    correoElectronico = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(60), nullable=False)
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus), nullable=False)
    fechaRegistro = Column(DateTime, nullable=False)
    fechaActualizacion = Column(DateTime, nullable=True)
