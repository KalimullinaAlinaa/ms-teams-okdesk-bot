from botbuilder.schema import Activity, Attachment
from botbuilder.core import TurnContext
from cards.adaptive_cards import WELCOME_MENU_CARD

async def send_welcome_menu(turn_context: TurnContext):
    card = Attachment(
        content_type="application/vnd.microsoft.card.adaptive",
        content=WELCOME_MENU_CARD
    )
    activity = Activity(
        type="message",
        attachments=[card]
    )
    await turn_context.send_activity(activity)
