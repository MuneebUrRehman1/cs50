def main():
    fraction = input("Fraction: ")
    convert(fraction)

def convert(fraction):
    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError     
        if x > y:
            raise ValueError

        return round(x/y * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()



