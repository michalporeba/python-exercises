from rpn_calculator_functional import *


def test_symbol_parser():
    assert [1] == parse_symbols("1")
    assert [2] == parse_symbols("2")
    assert [2, 1] == parse_symbols("2 1")
    assert callable(parse_symbols("2 1 +")[2])
