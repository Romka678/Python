# 4'. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
g = int(input('Введите номер четверти (1,2,3,4): '))
while(g < 1 or g > 4):
    print('Такой четверти не существует!')
    g = int(input('Введите номер четверти (1,2,3,4): '))
if(g == 1):
    print('x > 0 и y > 0')
if(g == 2):
    print('x < 0 и y > 0')
if(g == 3):
    print('x < 0 и y < 0')
if(g == 4):
    print('x > 0 и y < 0')