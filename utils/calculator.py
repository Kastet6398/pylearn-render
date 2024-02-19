import math
import re

import sympy
import time


def calculate(expr: str):
    expr = expr.lower()
    while re.findall(r"\)([\d]+)", expr) or re.findall(r"(?<!\w)j(?!\w)", expr) \
            or re.findall(r"([\d)])i", expr) \
            or re.findall(r"(?<!\w)i(?!\w)", expr) or re.findall(r"(?<!\w)pi(?!\w)", expr) \
            or re.findall(r"(?<!\w)pi(?!\w)", expr) or re.findall(r"(?<!\w)e(?!\w)", expr) \
            or re.findall(r"([\d)])([a-ik-z]+)", expr):
        expr = re.sub(r"([\w)])\(", "\\1*(", expr)
        expr = re.sub(r"([\d)])i", "\\1*1j", expr)
        expr = re.sub(r"([\d)])\(", "\\1(", expr)
        print(expr)
        expr = re.sub(r"([\d)])([a-ik-z]+)", "\\1*\\2", expr)
        print(expr)
        expr = re.sub(r"\)([\d]+)", ")*\\1", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)j(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)i(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)pi(?!\w)", f"{math.pi}", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)e(?!\w)", f"{math.e}", expr)
        print(expr)
        print(2222222)
    result = sympy.sympify(expr)
    return str(result)
