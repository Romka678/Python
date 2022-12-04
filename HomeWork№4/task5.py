# 5'. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import sympy
from sympy import sympify

x = sympy.Symbol('x')
with open(r'C:\Users\Роман\Documents\Python\HomeWork№4\polinom1.txt') as f:
    a = sympify(f.read())
with open(r'C:\Users\Роман\Documents\Python\HomeWork№4\polinom2.txt') as f:
    b = sympify(f.read())
with open(r'C:\Users\Роман\Documents\Python\HomeWork№4\result.txt','w') as f:
    f.write(str(sympy.simplify(a+b)))