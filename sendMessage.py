from uconfig import telegramSivayogeithBotToken, telegramGroupChatID
from utelegram import Telegram
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("-cd", "--chatID", nargs=1, type=str)
args = parser.parse_args()
print(args)
if args.chatID:
    chatID = args.chatID[0]
else:
    chatID = telegramGroupChatID
lastMes = None
lastMesTime = None
sender = None

t = Telegram(telegramSivayogeithBotToken, chatID)
while True:
    try:
        message = input("wHaT yOU wAnT tO sEnD? ")
        t.sendMessage(message)
        print()

        # incoming = t.getMessage()
        # # checking if incoming message_id is same as of last, then skip
        # if lastMes == incoming["message"]["message_id"]:
        #     continue
        # else:
        #     lastMes = incoming["message"]["message_id"]

        # # adding more validation to prevent messaging the last message whenever the polling starts
        # if not lastMesTime:
        #     lastMesTime = incoming["message"]["date"]
        #     continue
        # elif lastMesTime < incoming["message"]["date"]:
        #     lastMesTime = incoming["message"]["date"]
        # else:
        #     continue

        # # print(json.dumps(incoming, indent=4))
        # text: str = incoming['message']['text']
        # if not sender:
        #     sender = f'{incoming["message"]["from"]["first_name"]} {incoming["message"]["from"]["last_name"]}'
        # print(f"Reply from {sender}: {text}")

    except KeyboardInterrupt:
        print("Quitting...")
        exit()