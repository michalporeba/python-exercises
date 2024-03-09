def calculate(equation):
    symbols = parse_symbols(equation)
    stack = []

    while len(symbols) > 0:
        symbol = symbols.pop(0)
        if type(symbol) == type(""):
            operator = resolve_operator(symbol)
            b = stack.pop()
            a = stack.pop()
            return operator(a, b)
        else:
            stack += [symbol]


def resolve_operator(symbol):
    return {
        "+": _add,
        "-": _subtract,
        "*": _multiply,
        "^": __power
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

def __power(a, n):
    return a ** n