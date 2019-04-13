import flask
from telebot import types
import telebot
import os

TOKEN = '824073635:AAFokg_1q7Wyj8VvkBgXm7SSfJ8kfXr7SJs'
APP_NAME = 'telegrambotfortest'
 
server = flask.Flask(__name__)
bot = telebot.TeleBot(TOKEN)
 
 
@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(
         flask.request.stream.read().decode("utf-8"))])
    return "!", 200
 
 
@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, TOKEN))
    return "Hello from Heroku!", 200
 
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 443)))
