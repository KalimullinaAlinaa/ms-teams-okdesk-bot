from fastapi import APIRouter, Request
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings, TurnContext
from botbuilder.schema import Activity, ActivityTypes
import logging

from apis.v1.handlers.text_commands import handle_text_command
from apis.v1.handlers.card_handlers import handle_card_submit
from cards.adaptive_cards import MAIN_MENU_CARD
from botbuilder.schema import Attachment

router = APIRouter()
adapter_settings = BotFrameworkAdapterSettings(app_id="", app_password="")
adapter = BotFrameworkAdapter(adapter_settings)

@router.post("/messages")
async def messages(request: Request):
    body = await request.json()
    activity = Activity().deserialize(body)

    async def aux_func(turn_context: TurnContext):
        try:
            logging.info(f"[ACTIVITY TYPE] {activity.type}")
            logging.info(f"[RAW ACTIVITY] {activity.__dict__}")

            if activity.type == ActivityTypes.conversation_update:
                if activity.members_added:
                    for member in activity.members_added:
                        if member.id != activity.recipient.id:
                            await turn_context.send_activity("👋 Добро пожаловать! Отправьте любое сообщение, чтобы открыть главное меню.")

            elif activity.type == "message":
                # Если пришёл ответ из карточки (value)
                if activity.value:
                    card_response = await handle_card_submit(activity.value)
                    await turn_context.send_activity(card_response)
                    return

                text = (turn_context.activity.text or "").strip().lower()
                if not text:
                    await turn_context.send_activity("❗ Сообщение без текста. Попробуйте снова.")
                    return

                message_response = await handle_text_command(text)
                await turn_context.send_activity(message_response)

        except Exception as e:
            logging.exception("[MAIN BOT HANDLER ERROR]")
            await turn_context.send_activity(f"⚠️ Непредвиденная ошибка: {str(e)}")

    auth_header = request.headers.get("Authorization", "")
    await adapter.process_activity(activity, auth_header, aux_func)
    return {}
