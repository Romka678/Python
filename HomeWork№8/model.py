# Модуль для выполнения опреаций
import sympy

def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    try:
        ans = eval(expr)
    except:
        ans = 'Incorrect input'
    return str(ans)


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
                                                    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    x = sympy.Symbol('x')
    expr = expr.split("=", 1)[0]
    ans = []
    try:
        ans = sympy.solve(expr, x)
    except ValueError:
        ans = 'Incorrect input'
    return str(ans)


def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    x = sympy.Symbol('x')
    try:
        ans = sympy.simplify(expr)
    except:
        ans = 'Incorrect input'
    return str(ans)
