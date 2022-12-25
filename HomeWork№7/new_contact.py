def new_contact():
    name = input("Введите фамилию и инициалы, например(Петров И.И)\n")
    number = input("Введите номер\n")
    res = name + " // " + number
    with open(r'C:\Users\Роман\Documents\Python\HomeWork№7\dictionary.txt', 'a', encoding='utf-8') as f:
        f.write("\n" + name)
    with open(r'C:\Users\Роман\Documents\Python\HomeWork№7\dictionary2.txt', 'a', encoding='utf-8') as f:
        f.write("\n" + res)
    return res