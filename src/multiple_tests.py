import pytest

@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    assert x == y, "They are not equal!! Oh noooo!!!"

def test_method2():
    a = 15
    b = 20
    assert a+5 == b

    
