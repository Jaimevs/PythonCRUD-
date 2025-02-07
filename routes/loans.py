from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.loans
import config.db
import schemas.loans
import models.loans
from typing import List

loan = APIRouter()

models.loans.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@loan.get("/loans/", response_model=List[schemas.loans.Loan], tags=["Prestamos"])
async def read_loans(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.loans.get_loans(db=db, skip=skip, limit=limit)

@loan.get("/loan/{id}", response_model=schemas.loans.Loan, tags=["Prestamos"])
async def read_loan(id: int, db: Session = Depends(get_db)):
    db_loan = crud.loans.get_loan(db=db, id=id)
    if not db_loan:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return db_loan

@loan.post("/loans/", response_model=schemas.loans.Loan, tags=["Prestamos"])
async def create_loan(loan: schemas.loans.LoanCreate, db: Session = Depends(get_db)):
    return crud.loans.create_loan(db=db, loan=loan)

@loan.delete("/loan/{id}", tags=["Prestamos"])
async def delete_loan(id: int, db: Session = Depends(get_db)):
    db_loan = crud.loans.get_loan(db=db, id=id)
    if not db_loan:
        raise HTTPException(status_code=404, detail="Préstamo no existe, no se puede eliminar")
    crud.loans.delete_loan(db=db, id=id)
    return {"message": "Préstamo eliminado correctamente"}

@loan.put("/loan/{id}", response_model=schemas.loans.Loan, tags=["Prestamos"])
async def update_loan(id: int, loan: schemas.loans.LoanUpdate, db: Session = Depends(get_db)):
    db_loan = crud.loans.get_loan(db=db, id=id)
    if not db_loan:
        raise HTTPException(status_code=404, detail="Préstamo no existe, no actualizado")
    return crud.loans.update_loan(db=db, id=id, loan=loan)
