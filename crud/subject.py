import models.subject
import schemas.subject
from sqlalchemy.orm import Session

def get_subject(db: Session, id: int):
    return db.query(models.subject.Subject).filter(models.subject.Subject.id == id).first()

def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.subject.Subject).offset(skip).limit(limit).all()

def create_subject(db: Session, subject: schemas.subject.SubjectCreate):
    db_subject = models.subject.Subject(
        tipoMaterial=subject.tipoMaterial,
        marca=subject.marca,
        modelo=subject.modelo,
        numeroSerie=subject.numeroSerie,
        estatus=subject.estatus,
        fechaRegistro=subject.fechaRegistro,
        fechaActualizacion=subject.fechaActualizacion
    )

    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def update_subject(db: Session, id: int, subject: schemas.subject.SubjectUpdate):
    db_subject = db.query(models.subject.Subject).filter(models.subject.Subject.id == id).first()
    
    if not db_subject:
        return None
    update_data = subject.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_subject, key, value)

    db.commit()
    db.refresh(db_subject)
    return db_subject


def delete_subject(db: Session, id: int):
    db_subject = db.query(models.subject.Subject).filter(models.subject.Subject.id == id).first()
    if db_subject:
        db.delete(db_subject)
        db.commit()
    return db_subject
