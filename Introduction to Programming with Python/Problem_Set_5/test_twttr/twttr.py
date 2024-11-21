def main():
    str = input("Input: ")
    print("Output:", shorten(str))

def shorten(str):
    vowels = "aeiou"
    for s in str:
        if(s.lower() in vowels):
            str = str.replace(s,"")
    return str

if __name__ == "__main__":
    main()