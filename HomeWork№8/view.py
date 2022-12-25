# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    return input("Выберите режим:\n1 - выражения типа((5+3)*10)\n2 - выражения типа(x**3 - 8 = 0)\n3 - упрощение многочлена\n4 - вывести истроию оперций\n")


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    return input("Введите выражение:\n")


def show_res(res: str):
    """Выводит результат"""
    print("Результат вычислений: " + res)


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print("Вы уверены, что выбрали режим, попробуйте еще раз.")


def show_history(history: str):
    """Выводит истроию оперций"""
    for i in history:
        print(i)
