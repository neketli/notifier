import vk_api


class Bot:
    def __init__(self, token="3cfe3c1c18a92f28de92e3154f183ba9390e965f8377efbc5e26bc833478182f8eba90fc2ef1a73f1395b"):
        self._session = vk_api.VkApi(token=token)

    def send_message(self, destination, message):
        self._session.method("messages.send", {
            "user_id": destination,
            "message": message,
            "random_id": 0
    })



