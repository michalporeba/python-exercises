from inspect import signature
from math import sqrt 

def calculate(equation):
    symbols = parse_symbols(equation)
    stack = []

    while len(symbols) > 0:
        symbol = symbols.pop(0)
        if type(symbol) == type(""):
            operator = _resolve_operator(symbol)
            (result, stack) = _process_operator(operator, stack)
            if len(symbols) == 0:
                return result
            else:
                stack += [result]
        else:
            stack += [symbol]


def _process_operator(operator, stack):
    parameters = []
    for _ in signature(operator).parameters:
        parameters = [stack.pop()] + parameters

    return (operator(*parameters), stack)


def _resolve_operator(symbol):
    return {
        "+": _add,
        "-": _subtract,
        "*": _multiply,
        "^": _power,
        "sqrt": _square_root
    }[symbol]


def parse_symbols(equation):
    return [_parse_symbol(s) for s in equation.split()]


def _parse_symbol(symbol):
    try:
        return int(symbol)
    except:
        return symbol


def _add(a, b):
    return a + b


def _multiply(a, b):
    return a * b


def _subtract(a, b):
    return a - b

def _power(a, n):
    return a ** n

def _square_root(a):
    return sqrt(a)
