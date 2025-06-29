import logging
from botbuilder.schema import Activity, Attachment
from apis.v1.services.okdesk_client import format_issue_status, create_okdesk_ticket
from cards.adaptive_cards import (
    build_issue_status_card,
    INPUT_ISSUE_ID,
    CREATE_ISSUE_CARD,
    MAIN_MENU_CARD
)

async def handle_card_submit(data: dict) -> Activity:
    action_id = data.get("id")

    if action_id == "SHOW_STATUS_INPUT":
        return Activity(
            type="message",
            attachments=[Attachment(content_type="application/vnd.microsoft.card.adaptive", content=INPUT_ISSUE_ID)]
        )

    elif action_id == "SHOW_CREATE_ISSUE":
        return Activity(
            type="message",
            attachments=[Attachment(content_type="application/vnd.microsoft.card.adaptive", content=CREATE_ISSUE_CARD)]
        )

    elif action_id == "GET_ISSUE_STATUS":
        issue_id = data.get("issue_id")
        if not issue_id or not str(issue_id).isdigit():
            return Activity(type="message", text="⚠️ Укажите корректный ID заявки.")
        try:
            card = await format_issue_status(int(issue_id))
            return Activity(type="message", attachments=[
                Attachment(content_type="application/vnd.microsoft.card.adaptive", content=card)
            ])
        except Exception as e:
            logging.exception("Ошибка при получении статуса")
            return Activity(type="message", text=f"❌ Ошибка: {str(e)}")

    elif action_id == "CREATE_ISSUE":
        title = data.get("issue_title")
        description = data.get("issue_description")
        priority = data.get("issue_priority", "medium")

        if not title or not description:
            return Activity(type="message", text="⚠️ Укажите тему и описание заявки.")

        try:
            issue = await create_okdesk_ticket(
                title=title,
                description=description,
                priority=priority,
                author_id=None,
                author_type=None
            )
            return Activity(type="message", text=f"✅ Заявка создана: ID {issue.get('id')}")
        except Exception as e:
            logging.exception("Ошибка при создании заявки")
            return Activity(type="message", text=f"❌ Не удалось создать заявку: {str(e)}")

    return Activity(type="message", text="⚠️ Неизвестное действие.")
