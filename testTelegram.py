import json
from utelegram import Telegram
from uconfig import telegramGroupChatID, telegramTestBotToken
telegram = Telegram(telegramTestBotToken, telegramGroupChatID)
lastMes = None
lastMesTime = None
sender = None

while True:
    try:
        incoming = telegram.getMessage()
        # print(json.dumps(incoming, indent=4))
        # checking if incoming message_id is same as of last, then skip
        if lastMes == incoming["message"]["message_id"]:
            continue
        else:
            lastMes = incoming["message"]["message_id"]

        # adding more validation to prevent messaging the last message whenever the polling starts
        if not lastMesTime:
            lastMesTime = incoming["message"]["date"]
            continue
        elif lastMesTime < incoming["message"]["date"]:
            lastMesTime = incoming["message"]["date"]
        else:
            continue

        text: str = incoming['message']['text']
        if not sender:
            sender = f'{incoming["message"]["from"]["first_name"]} {incoming["message"]["from"]["last_name"]}'
        print("Incoming Message!!")
        print(f'This is from: {sender}')
        # print(f'Also: @{incoming["message"]["from"]["username"]}')
        print(text)
        if any(word in text.lower() for word in ['hi', 'hello', '/greet' , 'how are you']):
            telegram.chatID = incoming["message"]["from"]["id"]
            reply = f"Hi, {sender}"
            print(f"Sending: {reply}")
            telegram.sendMessage(reply)
        if any(word in text.lower() for word in ['name is', 'my name is']):
            telegram.chatID = incoming["message"]["from"]["id"]
            sender = text.split('is')[-1]
            reply = f"Hi, {sender}"
            print(f"Sending: {reply}")
            telegram.sendMessage(reply)

        # telegram.chatID = incoming["message"]["from"]["id"]
        # reply = f"Sorry master, i cant understand!"
        # print(f"Sending: {reply}")
        # telegram.sendMessage(reply)
    except KeyboardInterrupt:
        print("Quitting...")
        exit()