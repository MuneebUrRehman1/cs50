from cs50 import get_int
height = 0
while (height <= 0 or height >=9):
    height = get_int("Height: ")

spaces = height-1
for i in range(height):
    for j in range(spaces):
        print(" ", end="")
    for k in range(i+1):
        print("#", end="")
    print(" ", end="")
    for l in range(i+1):
        print("#", end="")
    spaces -= 1
    print()
