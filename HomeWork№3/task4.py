# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = 123
s = []
def LOL(num, line):
    if num != 0:
        LOL(int(num/2), line)
        s.append(num%2)
LOL(number, s)
print("".join(map(str,s)))