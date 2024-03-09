def calculate(equation):
    symbols = parse_symbols(equation)
    stack = []

    while len(symbols) > 0:
        symbol = symbols.pop(0)
        if type(symbol) == type(""):
            operator = resolve_operator(symbol)
            return operator(stack.pop(), stack.pop())
        else:
            stack += [symbol]


def resolve_operator(symbol):
    if symbol == "+":
        return _add
    return _multiply


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