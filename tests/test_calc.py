import pytest

from calc.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9


def test_add_three_numbers():
    c = Calc()

    res = c.add(4, 5, 6)

    assert res == 15


def test_add_many_numbers():
    s = range(100)

    assert Calc().add(*s) == 4950


def test_subtract_two_numbers():
    c = Calc()

    res = c.sub(10, 3)

    assert res == 7


def test_mul_two_numbers():
    c = Calc()

    res = c.mul(6, 4)

    assert res == 24


def test_mul_many_numbers():
    s = range(1, 10)

    assert Calc().mul(*s) == 362880


def test_div_two_numbers_float():
    c = Calc()

    res = c.div(13, 2)

    assert res == 6.5


def test_div_by_zero_returns_inf():
    c = Calc()

    res = c.div(5, 0)

    assert res == "inf"


def test_mul_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mul(3, 0)


def test_avg_correct_average():
    c = Calc()

    res = c.avg([2, 5, 12, 98])

    assert res == 29.25


def test_avg_removes_upper_outliers():
    c = Calc()

    res = c.avg([2, 5, 12, 98], ut=90)

    assert res == pytest.approx(6.333333)
