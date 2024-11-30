import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r"https?://(www\.)?youtube\.com/embed/([A-za-z0-9]+)", s):
        return "https://youtu.be/"+ url.group(2)



if __name__ == "__main__":
    main()