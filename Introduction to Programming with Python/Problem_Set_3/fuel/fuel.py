while True:
    try:
        x , y = input("Fraction: ").split("/")
        fuel = round(int(x)/int(y) * 100)
        if fuel <= 1:
            print("E")
        elif fuel >= 100:
            print("F")
        else:
            print(f"{fuel}%")
        break
    except (ValueError, ZeroDivisionError):
        pass





