def f(a: int, b: int):
    if (type(a) or type(b)) is not int:
        raise TypeError
    else:
        return a+b