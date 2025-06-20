from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True