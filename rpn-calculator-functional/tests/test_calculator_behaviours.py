from rpn_calculator_functional import calculate


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


def test_simple_power_of():
    assert 1 == calculate("2 0 ^")
    assert 2 == calculate("2 1 ^")
    assert 4 == calculate("2 2 ^")
    assert 8 == calculate("2 3 ^")
    assert 16 == calculate("2 4 ^")


def test_square_root_as_reverse_of_square():
    assert 2 != calculate("2 2 ^")
    assert 2 == calculate("2 2 ^ sqrt")


def test_complex_operations():
    assert 5 == calculate("2 3 + 8 3 - * sqrt")


def test_custom_operators():
    def modulo(a, b):
        return a % b
    assert 1 == calculate("6 5 %", {"%": modulo})
