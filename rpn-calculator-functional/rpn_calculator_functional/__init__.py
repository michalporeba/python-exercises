def calculate(equation):
    symbols = parse_symbols(equation)
    stack = []

    while len(symbols) > 0:
        if callable(symbols[0]):
            return symbols[0](stack.pop(), stack.pop())
        else:
            stack += [symbols.pop(0)]


def parse_symbols(equation):
    return [_parse_symbol(s) for s in equation.split()]


def _parse_symbol(symbol):
    try:
        return int(symbol)
    except:
        if symbol == "+":
          return _add
        return _multiply


def _add(a, b):
    return a + b


def _multiply(a, b):
    return a * b