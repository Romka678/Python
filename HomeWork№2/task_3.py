# 3'. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input('Введите число : '))
ls = list()
res = {}
for i in range(1,num + 1):
    res[i] = (1+1/i)**i
print(res)