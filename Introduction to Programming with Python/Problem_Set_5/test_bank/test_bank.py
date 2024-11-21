from bank import value

def test_with_hello():
    assert value("hello, world") == 0

def test_with_h():
    assert value("hi, how are you?") == 20

def test_without_h():
    assert value("This is cs50") == 100

def test_with_uppercase():
    assert value("HELLO, World") == 0