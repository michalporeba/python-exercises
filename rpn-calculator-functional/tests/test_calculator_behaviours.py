from rpn_calculator_functional import *


def test_simple_addition():
    assert 3 == calculate("1 2 +")
    assert 4 == calculate("2 2 +")
    assert 5 == calculate("4 1 +")

def test_simple_multiplication():
    assert 6 == calculate("2 3 *")