from datetime import datetime

import telebot
from GenerateMatrix import GenerateMatrix
from MessageGenerator import MessageGenerator
from AutobusNumber import *

bot = telebot.TeleBot("7179596607:AAEBE8Zo5rgqSTUZw_1c2uNK95vlr7BRZ3U")
last_seen = ""
isFirst = True


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Я бот для генерации автобусного бинго для генерации карты введите комманду /generate")


@bot.message_handler(commands=['generate'])
def generate(message):
    global last_seen
    if last_seen == datetime.now().strftime('%Y-%m-%d'):
        bot.send_message(message.chat.id, "Раз в день, падлюка")
    else:
        last_seen = datetime.now().strftime('%Y-%m-%d')
        message_to_send = MessageGenerator.GenerateMatrixMessage(GenerateMatrix.Generate(transports))
        bot.send_message(message.chat.id, message_to_send)


if __name__ == '__main__':
    print("Запустил автобусного мастера")
    bot.infinity_polling(none_stop=True)
