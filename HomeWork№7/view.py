def choose_mode():
    with open(r"C:\Users\Роман\Documents\Python\HomeWork№7\dictionary.txt",'r',encoding='utf-8') as f:
        for line in f:
            print(line)
    return input('1 - получить данные из справлчника.\n2 - добавить контакт в справочник\n')


def show_results(x):
    print(x)