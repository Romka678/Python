# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
ls1 = [1, 2, 3, 4, 5]
ls2 = [1, 2, 3, 4]
def Summa_par(ls):
    res = []
    if len(ls)%2==0:
        for i in range(int(len(ls)/2)):
            res.append(ls[i]*ls[len(ls) - i - 1])
        print("Новый список из произведений пар: ", res)
    else:
        k = int(len(ls)/2)
        for i in range(int(len(ls)/2)):
            res.append(ls[i]*ls[len(ls) - i - 1])
        res.append(ls[k]**2)
        print("Новый список из произведений пар: ", res)

Summa_par(ls1)
Summa_par(ls2)