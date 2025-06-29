from botbuilder.schema import Activity, Attachment
from cards.adaptive_cards import MAIN_MENU_CARD, INPUT_ISSUE_ID, CREATE_ISSUE_CARD

async def handle_text_command(text: str) -> Activity:
    if text.startswith("status"):
        card = Attachment(
            content_type="application/vnd.microsoft.card.adaptive",
            content=INPUT_ISSUE_ID
        )
        return Activity(type="message", attachments=[card])

    elif text.startswith("создать") or text.startswith("create"):
        card = Attachment(
            content_type="application/vnd.microsoft.card.adaptive",
            content=CREATE_ISSUE_CARD
        )
        return Activity(type="message", attachments=[card])

    # Главное меню
    return Activity(type="message", text="Отлично, вот главное меню 👇", attachments=[
        Attachment(content_type="application/vnd.microsoft.card.adaptive", content=MAIN_MENU_CARD)
    ])
