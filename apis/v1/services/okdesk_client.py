import httpx
import os
from dotenv import load_dotenv

load_dotenv()

OKDESK_API_KEY = os.getenv("OKDESK_API_KEY")
OKDESK_URL = os.getenv("OKDESK_URL", "https://yourcompany.okdesk.ru/api/v1")

headers = {
    "X-Token": OKDESK_API_KEY,
    "Content-Type": "application/json"
}

class OkDeskClient:
    def __init__(self):
        self.base_url = OKDESK_URL

    async def create_ticket(self, subject: str, description: str):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/tickets",
                headers=headers,
                json={
                    "subject": subject,
                    "description": description,
                    "requester": {"email": "user@example.com"}  
                }
            )
            response.raise_for_status()
            return response.json()

    async def get_ticket_status(self, ticket_id: int):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/tickets/{ticket_id}",
                headers=headers
            )
            response.raise_for_status()
            return response.json()
