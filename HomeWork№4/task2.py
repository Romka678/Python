# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Введите число: "))
k = 2 
s = []
while k <= n:
    if n % k == 0:
        if k not in s:
            s.append(k)
        n //= k
    else:
        k += 1
print(s)