
from fastapi import APIRouter

from apis.v1.routes import route_teams

api_router = APIRouter()
api_router.include_router(route_teams.router, prefix="/api", tags=["Teams"])

