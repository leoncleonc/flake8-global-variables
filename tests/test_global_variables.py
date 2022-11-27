import ast
from typing import Set

from flake8_global_variables import GlobalVariablesChecker


def _results(code: str) -> Set[str]:
    tree = ast.parse(code)
    plugin = GlobalVariablesChecker(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}


def test_correct_code():
    result = _results(
        """
HELLO_CONSTANT = 'Hello'

def fun_a():
    return 2
        
def fun_b(var=5):
    result = fun_a() + var
    return result
        
fun_b(var=3)"""
    )
    assert len(result) == 0


def test_incorrect_code():
    result = _results(
        """
global_hello = 'Hello'

def fun_a():
    return 2
        
def fun_b(var=5):
    result = fun_a() + var
    return result
            
global_var = 3
fun_b(global_var)"""
    )
    assert result == {
        "11:0 GV400: Found global variable",
        "2:0 GV400: Found global variable",
    }
