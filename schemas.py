from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class NoteResponse(NoteCreate):
    id: int

    class Config:
        from_attributes = True
