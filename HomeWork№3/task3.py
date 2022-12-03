# 3'. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
ls = [1.02, 5, 2.01, 3.24, 8.05]
maximum = 0
minimum = 1
for i in ls:
    c , d = divmod(i, 1)
    if d == 0:
        continue
    else:
        d = round(d, 3)
        if maximum < d:
            maximum = d
        else:
            if minimum > d:
                minimum = d
print(round(maximum - minimum,3))