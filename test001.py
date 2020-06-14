#hi roach nya nya
import telegram
from telegram.ext import Updater
import logging


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I\'m a bot, please talk to me!")


bot = telegram.Bot(token='1253179660:AAFp0ZOnzzXLjDNTlRYV5mHJZ4aZJWZJXdM')
# print(bot.get_me())
updater = Updater(token='1253179660:AAFp0ZOnzzXLjDNTlRYV5mHJZ4aZJWZJXdM',use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)




