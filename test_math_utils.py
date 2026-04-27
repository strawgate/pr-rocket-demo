from math_utils import safe_divide
import pytest


def test_basic_division():
    assert safe_divide(10, 2) == 5
    assert safe_divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)
