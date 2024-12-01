import pytest
from um import count

def main():
    test1()



def test1():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um, hello, um, world") == 2
    assert count("yummy") == None