import view
import model
import logger

# Реализовать калькулятор с системой логирования:
# 1) решение вводимых примеров (2+3) -> 5 ; 2**3 + (3+6)/(1+2) ->  11
# 2) решение уравнений (x+3 = 0) -> -3
# 3) упрощение многочленов (x*2 + 3*x2 + 4) -> 4*x*2 + 4

# Записать в файл "задачу" от пользователя и ответ.


def run_calc():
    tmp = "1"
    while(tmp == "1"):
        mode = view.choose()
        if mode == '1':
            expr = view.get_expr()
            result = model.execute_expr(expr)
            view.show_res(result)
            logger.log_exec(expr, result, "выражения типа((5+3)*10)")
            tmp = input("1 - продолжить работу\n2 - закончить")
        elif mode == '2':
            expr = view.get_expr()
            result = model.solve_eq(expr)
            view.show_res(result)
            logger.log_exec(expr, result, "выражения типа(x**3 - 8 = 0)")
            tmp = input("1 - продолжить работу\n2 - закончить")
        elif mode == '3':
            expr = view.get_expr()
            result = model.simpify_pol(expr)
            view.show_res(result)
            logger.log_exec(expr, result, "упрощение многочлена")
            tmp = input("1 - продолжить работу\n2 - закончить")
        elif mode == '4':
            history = logger.get_history()
            view.show_history(history)
            tmp = input("1 - продолжить работу\n2 - закончить")
        else:
            view.erorr_mode()
            tmp = input("1 - продолжить работу\n2 - закончить")
