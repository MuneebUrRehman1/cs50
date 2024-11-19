import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries_remaining = 3
        while True:
            try:
                answer = int(input(f"{x} + {y} =  "))
                if answer != x + y:
                    tries_remaining -= 1
                    if tries_remaining == 0:
                        print("EEE")
                        print(f"{x} + {y} =", x + y)
                        break
                    else:
                        print("EEE")
                else:
                    score += 1
                    break
            except ValueError:
                tries_remaining -= 1
                if tries_remaining == 0:
                    print("EEE")
                    print(f"{x} + {y} =", x + y)
                    break
                else:
                    print("EEE")
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            number = random.randint(0, 9)
        case 2:
            number = random.randint(10, 99)
        case 3:
            number = random.randint(100, 990)
        case _:
            raise ValueError
    return number


if __name__ == "__main__":
    main()
