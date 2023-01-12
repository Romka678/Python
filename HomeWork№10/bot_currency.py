import telebot
from random import randint
import bot_valut
candy = 117
flag = 0
bot = telebot.TeleBot("5751185059:AAF3CZwPCESI8UTrowjzlMr5Sg3ac5QIEKg")

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,"Привет ✌️ Хочешь узнать курс валют?}")
	bot.send_message(message.chat.id, "Введи какую валюту хочешь посмотреть (Команда: /currency US Dollar, /currency Euro)")

@bot.message_handler(func=lambda message: True)

def echo_all(message):
    if message.text == "/currency US Dollar":
        price_datetime, exchange_rates = bot_valut.get_exchange_list_xrates('RUB', 1)
        bot.send_message(message.chat.id,str(price_datetime) + "\n" + "1 рубль = " + str(exchange_rates['US Dollar']))
    else:
        if "/currency Euro":
            price_datetime, exchange_rates = bot_valut.get_exchange_list_xrates('RUB', 1)
            bot.send_message(message.chat.id,"Last updated:" + str(price_datetime) + "\n" + "1 рубль = " + str(exchange_rates['Euro']))

bot.infinity_polling()