from my_code import factorial_calc


def test_factorial_calc():
    assert 120 == factorial_calc(5)
    assert 6 == factorial_calc(3)
    assert 1 == factorial_calc(0)
    assert 40320 == factorial_calc(8)
