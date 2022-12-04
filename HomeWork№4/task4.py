#4'. Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.(записать в строку)

import random

s = []
polinom = ""
k = int(input("Введите степень многочлена: "))
for i in range(1,k + 2,1):
    s.append(random.randint(0,10))
for i in range(len(s)):
    if s[i] != 0 and k != 0:
        if s[i] == 1:
            polinom+=""
        else:
            polinom += str(s[i])
            polinom += "*"
        if k == 1:
            polinom += "x"
        else:
            polinom += "x^"
            polinom += str(k)
        if i == len(s) - 2 and s[i + 1] == 0:
            continue
        else:
            polinom += " + "
    else:
        if k == 0 and s[i] != 0:
            polinom += str(s[i])
    k-=1
with open(r'C:\Users\Роман\Documents\Python\HomeWork№4\out.txt','w') as f:
    f.write(polinom)