import math
def divide(a, b):
    if b > 0:
        return a / b
    return 0


def calculate_logarithm(x, base):
    result = math.log(x, base)
    return result


def reverse_string(new_string: str) -> str:
    """"Реверсируем строку"""
    return new_string[::-1]