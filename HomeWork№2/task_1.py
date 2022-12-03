# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
import math

num = input('Введите число :')
str = num.replace('.', '')
str = abs(float(str))
sum = 0
sum2 = 0
while (str != 0):
    sum = sum + str%10
    str = str // 10
print(sum)