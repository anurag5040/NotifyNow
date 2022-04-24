import telegram

def send_msg(text):
    token = "5304578747:AAFIVPBgUPaooZAs8bMLID_GKTtoryrwBqI"
    chat_id = "1128822500"
    Bot = telegram.bot(token=token)
    for i in text:
        bot.sendMessage(chat_id=chat_id, text=i)

new_list = []
with open("output.txt", 'r', encoding="utf-8") as file:
     new_list = file.read()
for i in new_list:
     send_msg(i)