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
