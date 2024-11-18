months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        x = input("Date: ")
        if "/" in x:
            mm, dd, yyyy = x.split("/")
        elif "," in x:
            mmdd, yyyy = x.split(",")
            mm, dd = mmdd.split(" ")
            mm = months.index(mm) + 1
        if int(mm) > 12 or int(dd) > 31:
            pass
        else:
            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break
    except (ValueError, NameError):
        pass

