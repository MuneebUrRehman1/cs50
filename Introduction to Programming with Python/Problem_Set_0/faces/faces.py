def main():
    text = input()
    convert(text)

def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙂"))

main()