from adaptivecards.card import AdaptiveCard
from adaptivecards.elements import TextBlock, InputText, ActionSubmit
from adaptivecards.containers import ColumnSet, Column
from adaptivecards.enums import Size, Weight

def create_input_issue_id_card():
    card = AdaptiveCard(version="1.3")

    # Заголовок
    card.add(TextBlock(
        text="Введите ID заявки",
        size=Size.MEDIUM,
        weight=Weight.BOLDER,
        wrap=True
    ))

    # Поле ввода ID
    card.add(InputText(
        id="issue_id",
        placeholder="Пример: 12345",
        is_required=True,
        error_message="Введите корректный ID"
    ))

    # Кнопка "Проверить статус"
    card.add(ActionSubmit(
        title="Проверить статус",
        data={"id": "GET_ISSUE_STATUS"}
    ))

    return card.to_dict()
