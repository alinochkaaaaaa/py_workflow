import pytest
from code import f


def test_normal_addition():
    """сложение с маленькими чисел"""
    assert f(2, 3) == 5
    assert f(-1, 1) == 0


def test_large_numbers():
    """сложение с большими числами"""
    assert f(1000000, 2000000) == 3000000
    assert f(-1000000000000, 10000) == 0


def test_type_error():
    """тест на TypeError"""
    with pytest.raises(TypeError):
        f("2", 3)

    with pytest.raises(TypeError):
        f(2, "3")

    with pytest.raises(TypeError):
        f("2", "3")