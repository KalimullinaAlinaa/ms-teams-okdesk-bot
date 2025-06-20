
from fastapi import APIRouter
from apis.v1 import ticket

api_router = APIRouter()
api_router.include_router(ticket.router, prefix="/api/v1")
# app.include_router(status.router, prefix="/api/v1")
# app.include_router(ms_teams.router, prefix="/api/v1")