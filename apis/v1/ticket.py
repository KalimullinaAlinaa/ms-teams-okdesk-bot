from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.db import  get_db
from models.ticket import Ticket
from schemas.ticket import TicketCreate, TicketResponse

router = APIRouter()

@router.post("/tickets", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = Ticket(user=ticket.user, message=ticket.message)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.get("/tickets", response_model=List[TicketResponse])
def read_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@router.get("/tickets/{ticket_id}", response_model=TicketResponse)
def read_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Тикет не найден")
    return ticket

@router.put("/tickets/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketCreate, db: Session = Depends(get_db)):
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Тикет не найден")
    db_ticket.user = ticket.user
    db_ticket.message = ticket.message
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@router.delete("/tickets/{ticket_id}", response_model=TicketResponse)
def delete_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Тикет не найден")
    db.delete(ticket)
    db.commit()
    return ticket
