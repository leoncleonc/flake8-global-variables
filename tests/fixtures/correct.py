"""Module with correct content."""

HELLO_CONSTANT = 'Hello'


def fun_a():
    return 2


def fun_b(var=5):
    result = fun_a() + var
    return result


fun_b(var=3)
