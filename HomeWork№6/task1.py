# 3'. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
ls = [1.02, 5, 2.01, 3.24, 8.05]
max_and_min= [0,1]
def Max_Min(ls, maxmin):
    for i in ls:
        c , d = divmod(i, 1)
        if d == 0:
            continue
        else:
            d = round(d, 3)
            if maxmin[0] < d:
                maxmin[0] = d
            else:
                if maxmin[1] > d:
                    maxmin[1] = d
filter(Max_Min(ls,max_and_min),ls)
difference = lambda x,y: x - y
print(round(difference(max_and_min[0],max_and_min[1]),3))