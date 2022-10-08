import sys
import csv
from tabulate import tabulate

try:
    # Checks if command-line arguments is not exactly two and exit with error message
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Checks if second command-line argument is not CSV file and exit with error
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Checks if command-line arguments is exactly two and CSV file and proceed
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):

        # Opens CSV file with csv reader it
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)

            # Iterate and print in grid table style from tabulate
            for row in reader:
                print(tabulate(reader, row, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")