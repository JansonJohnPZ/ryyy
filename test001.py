#hi roach nya nya
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)
import logging
import re

######################################################################
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 2334)
socket.socket = socks.socksocket
######################################################################


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='I\'m a bot, please talk to me!')


def error_callback(update, context):
    try:
        raise context.error
    except Unauthorized:
        pass
        # remove update.message.chat_id from conversation list
    except BadRequest:
        pass
        # handle malformed requests - read more below!
    except TimedOut:
        pass
        # handle slow connection problems
    except NetworkError:
        pass
        # handle other connection problems
    except ChatMigrated as e:
        pass
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        pass
        # handle all other telegram related errors

#######################################################################


def echo(update, context):
    print('New message:', update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def mesg(update, context):
    temp_m = update.message.text

    pattern = re.compile('(.*)偏指(.*)')
    search_pianzhi = re.search(pattern, temp_m)

    print('New message:', temp_m)
    if temp_m == 'nmsl':
        context.bot.send_message(chat_id=update.effective_chat.id, text='cnm')
    elif search_pianzhi:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Roach is watching you!')
    # elif temp_m == 'godie':
    #     context.bot.send_message(chat_id=update.effective_chat.id, text='oh, fuck, I will die!')
    #     updater.stop()
    else:
        pass


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I didn\'t understand that command.')


#######################################################################


bot = telegram.Bot(token='1253179660:AAFp0ZOnzzXLjDNTlRYV5mHJZ4aZJWZJXdM')
# print(bot.get_me())
updater = Updater(token='1253179660:AAFp0ZOnzzXLjDNTlRYV5mHJZ4aZJWZJXdM', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


########################################################################


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

mesg_handler = MessageHandler(Filters.text & (~Filters.command), mesg)
dispatcher.add_handler(mesg_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

dispatcher.add_error_handler(error_callback)

updater.start_polling()

