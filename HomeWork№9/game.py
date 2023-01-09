import bot
from random import randint


def input_dat(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(value):
    print(
        f"На столе осталось {value} конфет.")

def candy_game():
    player1 = "Игрок 1"
    player2 = "bot"
    value = 117
    flag = randint(0, 2)
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    while value != 0:
        if flag:
            k = input_dat(player1)
            value -= k
            flag = False
            p_print(value)
        else:
            k = randint(1, 28) if value >= 28 else randint(1, value)
            value -= k
            flag = True
            p_print(value)

    if flag:
        return f"Выиграл {player1}"
    else:
        return f"Выиграл {player2}"