import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_library.my_module import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(5, 6) == 11
    print(add(2, 3))

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(5, 6) == -1

def test_multiply():
    assert multiply(2, 7) == 6
    assert multiply(-1, 1) == -1
    assert multiply