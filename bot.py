import os
import telebot
from flask import Flask, request

bot = telebot.TeleBot('824073635:AAFokg_1q7Wyj8VvkBgXm7SSfJ8kfXr7SJs')


server = Flask(__name__)

#hadlers
#and in the end


@server.route("/", methods=['POST'])
def getMessage():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
        return "!", 200

@server.route("/")
def webhook():
	bot.remove_webhook()
    bot.set_webhook(url="https://telegrambotfortest.herokuapp.com/")
    return "!", 200

server.run(host="0.0.0.0", port=5000)
server = Flask(__name__)
