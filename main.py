import os

from flask import Flask, request
from telebot import types

import telebot

TOKEN = '5062379047:AAHR_qfGMypD4PxnFzKdq6gs6Ppr0KcWXRI'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


#КОД ТЕЛЕБОТА
!pip install pyTelegramBotAPI
import telebot
from telebot import types

bot = telebot.TeleBot("5062379047:AAHR_qfGMypD4PxnFzKdq6gs6Ppr0KcWXRI")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, напиши что-нибудь! )')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ага, значит ' + message.text)


bot.polling(none_stop = True)
#КОД ТЕЛЕБОТА


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://blrite.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
