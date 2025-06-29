INPUT_ISSUE_ID = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "text": "Введите ID заявки",
            "weight": "Bolder",
            "size": "Medium",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "id": "issue_id",
            "placeholder": "Пример: 12345"
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Проверить статус",
            "data": {"id": "GET_ISSUE_STATUS"}
        }
    ]
}

CREATE_ISSUE_CARD = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "text": "📝 Заполните поля для создания заявки",
            "wrap": True,
            "weight": "Bolder",
            "size": "Medium"
        },
        {
            "type": "TextBlock",
            "text": "Тема заявки *",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "id": "issue_title",
            "placeholder": "Например: Не работает принтер"
        },
        {
            "type": "TextBlock",
            "text": "Описание заявки *",
            "wrap": True
        },
        {
            "type": "Input.Text",
            "id": "issue_description",
            "placeholder": "Подробно опишите проблему",
            "isMultiline": True
        },
        {
            "type": "TextBlock",
            "text": "Приоритет *",
            "wrap": True
        },
        {
            "type": "Input.ChoiceSet",
            "id": "issue_priority",
            "style": "compact",
            "choices": [
                { "title": "Нормальный", "value": "low" },
                { "title": "Средний", "value": "medium" },
                { "title": "Высокий", "value": "high" },
                { "title": "Критический", "value": "critical" }
            ],
            "value": "medium"
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Создать заявку",
            "data": { "id": "CREATE_ISSUE" }
        }
    ]
}

def build_issue_status_card(issue: dict) -> dict:
    deadline = issue.get("deadline_at") or "Не указана"
    completed = issue.get("completed_at") or "Не завершена"
    status = issue.get("status", {}).get("name", "Неизвестен")
    title = issue.get("title", "Без темы")
    issue_id = issue.get("id", "—")

    return {
        "type": "AdaptiveCard",
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.3",
        "body": [
            {
                "type": "TextBlock",
                "text": f"📝 Заявка №{issue_id}",
                "weight": "Bolder",
                "size": "Large",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": f"📌 Статус: {status}",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": f"📅 Дедлайн: {deadline}",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": f"✅ Завершена: {completed}",
                "wrap": True
            },
            {
                "type": "TextBlock",
                "text": f"📄 Описание: {title}",
                "wrap": True
            }
        ]
    }

MAIN_MENU_CARD = {
    "type": "AdaptiveCard",
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.3",
    "body": [
        {
            "type": "TextBlock",
            "text": "Главное меню",
            "weight": "Bolder",
            "size": "Large",
            "wrap": True
        }
    ],
    "actions": [
        {
            "type": "Action.Submit",
            "title": "Проверить статус заявки",
            "data": {"id": "SHOW_STATUS_INPUT"}
        },
        {
            "type": "Action.Submit",
            "title": "Создать заявку",
            "data": {"id": "SHOW_CREATE_ISSUE"}
        }
    ]
}
