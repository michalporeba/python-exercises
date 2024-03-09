def calculate(equation):
  symbols = parse_symbols(equation)

  return symbols[0] + symbols[1]

def parse_symbols(equation):
  return [_parse_symbol(s) for s in equation.split()]

def _parse_symbol(symbol):
  try:
    return int(symbol)
  except:
    return _add
  
def _add():
  pass