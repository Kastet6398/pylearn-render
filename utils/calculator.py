import math
import re
import time
import traceback

import sympy


def lg(x):
    return math.log10(x)


def calculate(expr: str):
    expr = expr.lower()
    while re.findall(r"\)([\d]+)", expr) or re.findall(r"(?<!\w)j(?!\w)", expr) \
            or re.findall(r"([\d)])i(?!\w)", expr) \
            or re.findall(r"(?<!\w)i(?!\w)", expr) or re.findall(r"(?<!\w)e(?!\w)", expr) \
            or re.findall(r"([\d)])([a-ik-z]+)", expr):

        expr = re.sub(r"([\d)])i(?!\w)", "\\1*1j", expr)
        print(expr)
        expr = re.sub(r"([\d)])\(", "\\1(", expr)
        print(expr)
        expr = re.sub(r"([\d)])([a-ik-z]+)", "\\1*\\2", expr)
        print(expr)
        expr = re.sub(r"\)([\d]+)", ")*\\1", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)j(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"(?<!\w)e(?!\w)", str(math.e), expr)
        print(expr)
        expr = re.sub(r"(?<!\w)i(?!\w)", "1j", expr)
        print(expr)
        expr = re.sub(r"([\d)])([a-ik-z]+)", "\\1*\\2", expr)
        print(expr)
        print(2222222)
    try:
        smpf = sympy.sympify(expr, {"lg": lg})
        try:
            result = smpf.evalf()
            print(result)
            return str(result)
        except AttributeError:
            result = smpf
            print(result)
            return str(result)
    except:
        traceback.print_exc()
        return "Error"
