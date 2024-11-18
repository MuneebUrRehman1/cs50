list = {}
while True:
    try:
        item  = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1
    except EOFError:
        print("\n")
        for item in sorted(list):
            print(f"{list[item]} {item}")
        break
    