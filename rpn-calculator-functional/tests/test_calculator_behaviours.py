from rpn_calculator_functional import *


def test_simple_addition():
    assert 3 == calculate("1 2 +")
    assert 4 == calculate("2 2 +")
    assert 5 == calculate("4 1 +")
    assert 3 == calculate("-3 6 +")

def test_simple_multiplication():
    assert 6 == calculate("2 3 *")
    assert 12 == calculate("3 4 *")
    assert 21 == calculate("3 7 *")
    assert -10 == calculate("2 -5 *")

def test_simple_subtraction():
    assert 1 == calculate("4 3 -")
    assert -1 == calculate("3 4 -")