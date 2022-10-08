import sys
import csv

students = []

try:
    # Checks if command-line arguments is not exactly 3 and exit with error message
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Checks if second and third command-line argument is not CSV file and exit with error
    elif not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Checks if command-line arguments is exactly three and CSV file and proceed
    elif len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):

        # Opens CSV file with csv with Dictionary reader
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)

            # Iterate through the csv file and split first column
            for row in reader:
                name = row["name"].split(",")

                # Add to the students list with columns of first name, last name, and house
                students.append({"first": name[1].lstrip(), "last": name[0].lstrip(), "house": row["house"]})

                # Column names for the csv file to write to
                fieldname = ["first", "last", "house"]

        # Opens new csv file with the third argument, write the list of students to the file
        with open(sys.argv[2], "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldname)
            writer.writeheader()
            for student in students:
                writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")