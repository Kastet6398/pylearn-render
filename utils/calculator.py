import re
import time

import sympy


def calculate(expr: str):
    expr = expr.lower()
    while re.findall(r"([a-zA-Z)]+(?<!sin)(?<!cos)(?<!tan)(?<!acos)(?<!asin)(?<!atan)(?<!cot)(?<!acot)(?<!sinc)("
                     r"?<!sinh)(?<!asinh)(?<!acosh)(?<!cosh)(?<!tanh)(?<!cotanh)(?<!atanh)(?<!acoth))\(",
                     expr) or re.findall(r"\)([\d]+)", expr) or re.findall(r"(?<!\w)j(?!\w)", expr) \
            or re.findall(r"([\d)])i", expr) \
            or re.findall(r"(?<!\w)i(?!\w)", expr) \
            or re.findall(r"([\d)])([a-ik-z]+)", expr):
        expr = re.sub(r"([a-zA-Z)]+(?<!sin)(?<!cos)(?<!tan)(?<!acos)(?<!asin)(?<!atan)(?<!cot)(?<!acot)(?<!sinc)("
                      r"?<!sinh)(?<!asinh)(?<!acosh)(?<!cosh)(?<!tanh)(?<!cotanh)(?<!atanh)(?<!acoth))\(", "\\1*(",
                      expr)
        print(expr)
        expr = re.sub(r"([\d)])i(?!\w)", "\\1*1j", expr)
        print(expr)
        expr = re.sub(r"([\d)])\(", "\\1(", expr)
        print(expr)
        expr = re.sub(r"([\d)])(?!(sin|cos|tan|acos|asin|atan|cot|acot|sinc|sinh|asinh|acosh|cosh|tanh|cotanh|atanh"
                      r"|acoth)\b)([a-ik-z]+)", "\\1*\\3", expr)
        print(expr)
        expr = re.sub(r"\)([\d]+)", ")*\\1", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)j(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)i(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"([\d)])([a-ik-z]+)", "\\1*\\2", expr)
        print(expr)
        print(2222222)
    result = sympy.simplify(expr).evalf()
    print(result)
    return str(result)
