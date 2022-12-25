def find_contact():
    contact = input("Введите контакт.\n")
    res = "Такого контакта нет в справочнике."
    with open(r'C:\Users\Роман\Documents\Python\HomeWork№7\dictionary2.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if contact in line:
                res = line
    return res