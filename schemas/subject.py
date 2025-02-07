from typing import List, Union, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class SubjectBase(BaseModel):
    tipoMaterial: str
    marca: str
    modelo: str
    numeroSerie: str 
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime

class SubjectCreate(SubjectBase):
    pass

class SubjectUpdate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
