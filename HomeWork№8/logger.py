# Модуль для записи резуьтатов вычислений
import view
def log_exec(expr: str, result: str, k: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open(r'C:\Users\Роман\Documents\Python\HomeWork№8\log.txt', 'a', encoding='utf-8') as f:
        f.write("\nРежим калькулятора:" + k + "\nПользователь ввел : " + expr + "; Результат вычислений : " + result + "\n")


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    res = []
    with open(r"C:\Users\Роман\Documents\Python\HomeWork№8\log.txt",'r',encoding='utf-8') as f:
        for line in f:
            res.append(line)
    #print(res)
    return res
