from typing import List, Union, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    nombre: str
    primerApellido: str
    segundoApellido: str
    tipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime

class UserCreate(UserBase):
    pass
class UserUpdate(UserBase):
    pass
class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
