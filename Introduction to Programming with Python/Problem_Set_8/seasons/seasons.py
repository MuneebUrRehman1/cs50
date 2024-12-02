from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
        birthday = input("Date of Birth: ")
        print (difference(birthday), "minutes")

def difference(birthday):
    try:
        year, month, day = birthday.split("-")
        birthday = date(int(year), int(month), int(day))
        difference =  (date.today() - birthday).days * 24 * 60
        result = p.number_to_words(difference, andword="").capitalize()
        return result

    except:
        return sys.exit("Invalid date")
 

if __name__ == "__main__":
    main()