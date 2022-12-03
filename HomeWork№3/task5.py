# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

l = [1 , 0 , 1]

def Fibb(n, s):
    a = 0
    b = 1
    c = 0
    k = -1
    if n == 1:
        print(s[1])
    else:
        if n == 2: print(s)
    if n == 0: print("Ничего не вывел")
    else:
        for i in range(1,n,1):
            c = int(a + b)
            s.append(c)
            s.insert(0,c*k)
            k*=(-1)
            a = b
            b = c
Fibb(8, l)
print(l)
