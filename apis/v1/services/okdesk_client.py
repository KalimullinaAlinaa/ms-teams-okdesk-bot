import logging
from typing import Optional
import os
import httpx

from cards.adaptive_cards import build_issue_status_card

OKDESK_API_TOKEN = os.getenv("OKDESK_API_TOKEN")
OKDESK_BASE_URL = os.getenv("OKDESK_BASE_URL", "https://support.plus-aliance.ru")



async def create_okdesk_ticket(
    title: str,
    description: Optional[str] = None,
    ticket_type: Optional[str] = None,
    priority: Optional[str] = None,
    author_id: Optional[str] = None,
    author_type: Optional[str] = None,
    custom_parameters: Optional[dict] = None
) -> dict:
    issue = {
        "title": title,
        "description": description,
    }

    if ticket_type:
        issue["type"] = ticket_type
    if priority:
        issue["priority"] = priority
    if custom_parameters:
        issue["custom_parameters"] = custom_parameters
    if author_id and author_type:
        issue["author"] = {"id": author_id, "type": author_type}

    payload = {"issue": issue}

    logging.info(f"[CREATE TICKET PAYLOAD] {payload}")

    url = f"{OKDESK_BASE_URL}/api/v1/issues"
    params = {"api_token": OKDESK_API_TOKEN}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params, json=payload)
        response.raise_for_status()
        return response.json()
    # Удаление ключей со значением None
    payload["issue"] = {k: v for k, v in payload["issue"].items() if v is not None}

    url = f"{OKDESK_BASE_URL}/api/v1/issues"
    params = {"api_token": OKDESK_API_TOKEN}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params, json=payload)
        response.raise_for_status()
        return response.json()


async def get_issue_status(ticket_id: int) -> dict:
    url = f"{OKDESK_BASE_URL}/api/v1/issues/{ticket_id}"
    params = {"api_token": OKDESK_API_TOKEN}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()


async def format_issue_status(issue_id: int):
    url = f"{OKDESK_BASE_URL}/api/v1/issues/{issue_id}"
    params = {"api_token": OKDESK_API_TOKEN}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        issue = response.json()
        return build_issue_status_card(issue)
