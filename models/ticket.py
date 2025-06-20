from sqlalchemy import Column, Integer, String
from db.db import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, nullable=False)
    message = Column(String, nullable=False)
