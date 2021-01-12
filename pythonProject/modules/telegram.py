import telegram
import time

def send_message(text):

    bot = telegram.Bot(token = TELEGRAM_TOKEN)
    updates = bot.getUpdates()

    bot.sendMessage(chat_id=CHAT_ID, text=text)
    time.sleep(2)

# text = 'hello2222_lll aa'
# send_message(chat_id, text)
