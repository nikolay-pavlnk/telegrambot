import telebot
import os
from flask import Flask, request
import logging

bot = telebot.TeleBot('824073635:AAFokg_1q7Wyj8VvkBgXm7SSfJ8kfXr7SJs')

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

server = Flask(__name__)
@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
@server.route("/")
def webhook():
  	bot.remove_webhook()
    bot.set_webhook(url="https://min-gallows.herokuapp.com/bot") # этот url нужно заменить на url вашего Хероку приложения
    return "?", 200
server.run(host="0.0.0.0", port=os.environ.get('PORT', 80))