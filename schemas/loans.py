from typing import List, Optional, Union
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class LoanBase(BaseModel):
    id_usuario: int
    id_material: int
    fecha_prestamo: datetime
    fecha_devolucion: datetime
    estado_prestamo: str
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime] = None


class LoanCreate(LoanBase):
    pass
class LoanUpdate(LoanBase):
    pass
class Loan(LoanBase):
    id: int
    model_config = ConfigDict(from_attributes=True)