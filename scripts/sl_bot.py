from slack import WebClient


class Bot:
    # Заготовка сообщения для отправки
    TEXT_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Добрый день, коллеги, поступило новое сообщение: \n\n"
            ),
        },
    }

    def __init__(self, token="xoxb-2640569401490-2633839882710-qhHHjJgzebjI7j61KUBPJkHS"):
        self._slack_web_client = WebClient(token=token)

    def send_message(self, destination, message):
        # заготавливаем необходимео сообщение
        msg = self._get_message_payload(destination, message)
        # постим в указанный канал
        self._slack_web_client.chat_postMessage(**msg)

    # Метод для подготовки структуры сообщения
    def _get_message_payload(self, destination, text):
        return {
            "channel": destination,
            "blocks": [
                self.TEXT_BLOCK,
                {"type": "section", "text": {"type": "mrkdwn", "text": text}},
            ],
        }

