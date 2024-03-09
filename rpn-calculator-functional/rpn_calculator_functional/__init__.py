def calculate(equation):
  symbols = parse_symbols(equation)
  stack = []

  while len(symbols) > 0:
    print("----")
    print(symbols)
    print(stack)
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
    return _add
  
def _add(a, b):
  return a + b