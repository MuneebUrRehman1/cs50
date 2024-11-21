def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return condition_one(s) and condition_two(s) and condition_three(s) and  condition_four(s)

def condition_one(s):
    return 2 <= len(s) <= 6

def condition_two(s):
    return not s[0].isdigit() and not s[1].isdigit()

def condition_three(s):
    seen_digit = False
    for char in s:
        if char.isdigit():
            if not seen_digit and char == '0':  
                return False
            seen_digit = True 
        elif seen_digit:
           
            return False
    return True

def condition_four(s):
    return s.isalnum()
if __name__ == "__main__":
    main()