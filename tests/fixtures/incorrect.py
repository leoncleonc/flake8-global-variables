"""Module with incorrect content."""

global_hello = 'Hello'


def fun_a():
    return 2


def fun_b(var=5):
    result = fun_a() + var
    return result


global_var = 3
fun_b(global_var)
