first, operator, second = input("Expression: ").split(" ")
first = float(first)
second  = float(second)
match operator:
    case "+":
        print(f"{first + second:.1f}")
    case "-":
        print(f"{first - second:.1f}")
    case "*":
        print(f"{first * second:.1f}")  
    case _:
        print(f"{first / second:.1f}")

