# 3'. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

ls = list(range(1,int(input('Введите число : ')) + 1))
res = [(1+1/n)**n for n in ls]
print(res)