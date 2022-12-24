# 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)

def draw_board(pole):
   print("-" * 13)
   for i in range(3):
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
      print("-" * 13)

def step(pole,xo):
    stak = False
    while(stak == False):
        step = input("Куда поставить {}?\n".format(xo))
        try:
            step = int(step)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if step >= 1 and step <= 9:
            if(str(pole[step-1]) not in "XO"):
                pole[step-1] = xo
                stak = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Введите число от 1 до 9.")

def win(pole):
    win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win:
        if pole[each[0]]==pole[each[1]]==pole[each[2]]:
            return pole[each[0]]
    return False

else_game = "1"
while(else_game == "1"):
    k = 0
    pole = list(range(1,10))
    draw_board(pole)
    game = False
    while(game == False):
        while(k < 9):
            if k % 2 == 0:
                step(pole,"X")
            else:
                step(pole,"O")
            draw_board(pole)
            k+=1
            if k > 4:
                player = win(pole)
                if player:
                    print(player,"Выиграл")
                    game = True
                    break
            if k == 9:
                print("Ничья!")
                break
    print("Хотите сыграть еще раз?\nВведите:")
    else_game = input("1 - да, 2 - нет\n")
        