import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if time := re.search(r"^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$",s):
        if int(time.group(1)) > 12 or int(time.group(4)) > 12:
            raise ValueError
        
        first_hours = to_24hour(int(time.group(1)), time.group(2), time.group(3))
        second_hours = to_24hour(int(time.group(4)), time.group(5), time.group(6))
        return f"{first_hours} to {second_hours}"
        

def to_24hour(hours, minutes, time):
    if time == 'PM':
        if hours == 12:
            hours = 12
        else:
            hours+= 12
    else:
        if hours == 12:
            hours = 0
    if minutes == None:
        minutes = "00"
    
    return f"{hours:02}:{minutes:02}"
        

if __name__ == "__main__":
    main()