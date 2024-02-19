import math
import re

import sympy


def calculate(expression):
    expr = re.sub(r"([)\d])([a-zA-Z\d]+)", "\\1*\\2", expression)
    expr = re.sub(r"([\b]*)j([\b]*)", "\\1j\\2", expr)
    expr = re.sub(r"([\b]*)i([\b]*)", "\\1j\\2", expr)
    expr = re.sub(r"([\d]*)i([\b]*)", "\\1j\\2", expr)
    expr = re.sub(r"([\b\d]*)pi([\b\d]*)", fr"\g<1>{math.pi}\2", expr)
    expr = re.sub(r"([\b\d]*)e([\b\d]*)", fr"\g<1>{math.e}\2", expr)
    result = sympy.sympify(expr)
    return result
