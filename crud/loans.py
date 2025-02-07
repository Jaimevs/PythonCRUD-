import models.loans
import schemas.loans
from sqlalchemy.orm import Session

def get_loan(db: Session, id: int):
    return db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()

def get_loans(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.loans.Loan).offset(skip).limit(limit).all()

def create_loan(db: Session, loan: schemas.loans.LoanCreate):
    db_loan = models.loans.Loan(
        id_usuario=loan.id_usuario,
        id_material=loan.id_material,
        fecha_prestamo=loan.fecha_prestamo,
        fecha_devolucion=loan.fecha_devolucion,
        estado_prestamo=loan.estado_prestamo,
        fecha_registro=loan.fecha_registro,
        fecha_actualizacion=loan.fecha_actualizacion
    )

    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

def update_loan(db: Session, id: int, loan: schemas.loans.LoanUpdate):
    db_loan = db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()
    if db_loan:
        for var, value in vars(loan).items():
            if value is not None:
                setattr(db_loan, var, value)
        db.commit()
        db.refresh(db_loan)
    return db_loan


def delete_loan(db: Session, id: int):
    db_loan = db.query(models.loans.Loan).filter(models.loans.Loan.id == id).first()
    if db_loan:
        db.delete(db_loan)
        db.commit()
    return db_loan
