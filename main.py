from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="TODO Notes API")


@app.get("/")
def read_root():
    return {"Message": "Welcome to the Todo Notes API!"}


# Create a New Note
@app.post("/notes", response_model=schemas.NoteResponse)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    try:
        new_note = models.Note(
            title=note.title,
            description=note.description,
            is_completed=note.is_completed,
        )

        db.add(new_note)
        db.commit()
        db.refresh(new_note)

        return new_note

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Get All Notes
@app.get("/notes", response_model=list[schemas.NoteResponse])
def get_notes(db: Session = Depends(database.get_db)):
    try:
        return db.query(models.Note).all()

    except Exception:
        raise HTTPException(status_code=500, detail="Couldn't fetch notes")


# Update a Existing Note
@app.put("/notes/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int,
    updated_note: schemas.NoteCreate,
    db: Session = Depends(database.get_db),
):
    try:
        db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

        if db_note is None:
            raise HTTPException(status_code=404, detail="Note not Found")

        for key, value in updated_note.model_dump().items():
            setattr(db_note, key, value)

        db.commit()
        db.refresh(db_note)
        return db_note

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Update Failed")


# Delete a Note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    try:
        db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

        if db_note is None:
            raise HTTPException(status_code=404, detail="Note not found")

        db.delete(db_note)
        db.commit()
        return {"message": "Note deleted successfully"}

    except HTTPException:
        raise

    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Delete Failed")
