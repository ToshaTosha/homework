import pytest
from main import to_infix

def test_case1():
    prefix = '+ - 13 4 55'
    expected = '((13 - 4) + 55)'
    assert to_infix(prefix) == expected

def test_case2():
    prefix = '+ 2 * 2 - 2 1'
    expected = '(2 + (2 * (2 - 1)))'
    assert to_infix(prefix) == expected

def test_case3():
    prefix = '+ + 10 20 30'
    expected = '((10 + 20) + 30)'
    assert to_infix(prefix) == expected


def test_case5():
    prefix = '/ + 3 10 * + 2 3 - 3 5'
    expected = '((3 + 10) / ((2 + 3) * (3 - 5)))'
    assert to_infix(prefix) == expected


def test_to_infix_errors():
    with pytest.raises(ValueError):
        to_infix("")
    with pytest.raises(ValueError):
        to_infix("- - 1 2")
