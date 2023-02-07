import json
import requests
class Telegram:
    baseUrl = f"https://api.telegram.org/bot"
    def __init__(self, token, chatID) -> None:
        self.token, self.chatID = token, chatID

    def get(self, url, params):
        r = requests.get(url, params=params)
        return r

    def sendMessage(self, message):
        self.get(f"{self.baseUrl}{self.token}/sendMessage", {'chat_id': self.chatID, 'text': message})

    def getMessage(self):
        res = self.get(f"{self.baseUrl}{self.token}/getUpdates", {})
        results = json.loads(res.content.decode("utf8"))["result"]
        if results:
            return results[-1]
        else:
            return []