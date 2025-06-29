from typing import Dict, Optional
from pydantic import BaseModel, Field

class TicketCreate(BaseModel):
    title: str
    description: Optional[str] = None
    type: Optional[str] = Field(default="service")
    priority: Optional[str] = Field(default="medium")
    author_id: Optional[str] = None
    author_type: Optional[str] = None  # 
    custom_parameters: Optional[Dict[str, str]] = None

class TicketResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True