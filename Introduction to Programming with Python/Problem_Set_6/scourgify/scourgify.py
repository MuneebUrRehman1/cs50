import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
students = []
try:
    with open(sys.argv[1]) as input:
        reader = csv.DictReader(input)
        for row in reader:
            last, first = row["name"].split(",")
            students.append({"first": first, "last": last, "house": row["house"]})

    with open(sys.argv[2], "w") as output:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
