# 5'. Реализуйте алгоритм перемешивания списка.
import random

list1 = [1, 2, 3, 4, 5, 6, 7 ,8 ,9 ,10]
print("Original :", list1)
for i in range(len(list1)):
    index = random.randint(0, len(list1)-1)
    tmp = list1.pop(i)
    list1.append(tmp)
print("New :", list1)

#второй способ с встроенной функцией
# random.shuffle(list1)
# print ("New : ", str(list1))