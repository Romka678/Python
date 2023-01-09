import telebot
from random import randint
candy = 117
flag = 0
bot = telebot.TeleBot("5847172565:AAFC-6HsTs2ujdMW8_SWOWr7diuIxf3q7eU")

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,"Привет ✌️ Сыграем в игру с конфетами, есть 117 конфет")
	bot.send_message(message.chat.id, "Введите количество конфет, которое возьмете от 1 до 28: ")

@bot.message_handler(func=lambda message: True)

def echo_all(message):
	global flag
	win = False
	max_move = 28
	global candy
	count_for_check_win = candy // max_move
	if not win:
		move = int(message.text)
		if move > 0 and move <= max_move and move <= candy:
			bot.send_message(message.chat.id, f"Вы забрали {str(move)} конфет")
			candy -= move
			bot.send_message(message.chat.id, f'Осталось {str(candy)} конфет')
			flag += 1
		else:
			bot.send_message(message.chat.id, 'Количество взятых конфет должно быть в интервале от 1 до 28 или не больше оставшегося количества конфет')
			move = int(message.text)
		if flag >= count_for_check_win - 1:
			if candy == 0:
				if flag % 2 == 0:
					bot.send_message(message.chat.id, f'Вы выиграли.')
					candy = 117
					win = True
				else:
					bot.send_message(message.chat.id, f'Выиграл бот.')
					candy = 117
					win = True
	if not win:
		if flag % 2 == 1:
			move = randint(1, max_move) if candy >= max_move else randint(1, candy)
			bot.send_message(message.chat.id, f'Бот забрал {str(move)} конфет')
			candy -= move
			bot.send_message(message.chat.id, f'Осталось {str(candy)} конфет')
			flag += 1
			if flag >= count_for_check_win - 1:
				if candy == 0:
					if flag % 2 == 0:
						bot.send_message(message.chat.id, f'Вы выиграли.')
						candy = 117
						win = True
					else:
						bot.send_message(message.chat.id, f'Выиграл бот.')
						candy = 117
						win = True
		else:
			bot.send_message(message.chat.id, "Введите количество конфет, которое возьмете от 1 до 28: ")

bot.infinity_polling()