from twttr import shorten


def test_lowercase():
    assert shorten("hello, world") == "hll, wrld"

def test_uppercase():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_no_vowels():
    assert shorten("dry, cysts") == "dry, cysts"

def test_only_vowels():
    assert shorten("aeiou") == ""