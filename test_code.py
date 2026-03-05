import pytest
from mycode import f


def test_normal_addition():
    """сложение с маленькими чисел"""
    assert f(2, 3) == 5
    assert f(-1, 1) == 0


def test_large_numbers():
    """сложение с большими числами"""
    assert f(1_000_000, 2_000_000) == 3_000_000
    assert f(-1_000_000_000_000, 10_000) == -999_999_990_000


def test_type_error():
    """тест на TypeError"""
    with pytest.raises(TypeError):
        f("2", 3)

    with pytest.raises(TypeError):
        f(2, "3")

    with pytest.raises(TypeError):
        f("2", "3")