from fastapi import FastAPI
from routes.users import user
from routes.subject import subject
from routes.loans import loan

app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de préstamo de material educativo"
)

app.include_router(user)
app.include_router(subject)
app.include_router(loan)
