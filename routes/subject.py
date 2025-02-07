from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.subject
import config.db
import schemas.subject
import models.subject
from typing import List

subject = APIRouter()

models.subject.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@subject.get("/subjects/",response_model=List[schemas.subject.Subject], tags=["Materiales"])
async def read_subjects(skip: int = 0, limit: int = 10, db:Session = Depends(get_db)):
    db_subjects = crud.subject.get_subjects(db = db , skip = skip, limit = limit)
    return db_subjects

@subject.post("/subject/{id}",response_model=schemas.subject.Subject, tags=["Materiales"])
async def read_subject(id:int,db:Session=Depends(get_db)):
    db_subject = crud.subject.get_subject(db=db,id=id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return db_subject

@subject.post("/subjects/", response_model=schemas.subject.Subject, tags=["Materiales"])
async def create_subject(subject: schemas.subject.SubjectCreate, db: Session = Depends(get_db)):
    db_subject = crud.subject.create_subject(db=db, subject=subject)
    return db_subject

@subject.delete("/subject/{id}", response_model=schemas.subject.Subject, tags=["Materiales"])
async def delete_subject(id: int, db: Session = Depends(get_db)):
    db_subject = crud.subject.get_subject(db=db, id=id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Material no exite, no se puede eliminar")
    crud.subject.delete_subject(db=db, id=id)
    return db_subject

@subject.put("/subject/{id}", response_model=schemas.subject.Subject, tags=["Materiales"])
async def update_subject(id: int, subject: schemas.subject.SubjectUpdate, db: Session = Depends(get_db)):
    db_subject = crud.subject.get_subject(db=db, id=id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Material no existe, no actualizado")

    updated_subject = crud.subject.update_subject(db=db, id=id, subject=subject)
    return updated_subject
