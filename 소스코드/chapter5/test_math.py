from math_operation import add

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def test_addition_fail():
    assert 1 + 3 == 2

def test_subtraction_fail():
    assert 3 - 1 == 1

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(0,0) == 0