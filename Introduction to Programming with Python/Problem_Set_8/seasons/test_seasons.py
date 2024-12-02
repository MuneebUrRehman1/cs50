import pytest
from seasons import difference

def main():
    test()

def test():
    assert difference("2022-01-20") == "One million, five hundred seven thousand, six hundred eighty"
    assert difference("2021-01-20") == "Two million, thirty-three thousand, two hundred eighty"
    with pytest.raises(SystemExit):
        difference("Januar 1st, 2000")



if __name__ == "__main__":
    main()



