from datetime import date, datetime
import re
import inflect
import sys

p = inflect.engine()



def main():
    print(convert(input("Date of Birth: ")))

def convert(s):

    # Conditions for DoB format "YYYY-MM-DD", convert from days to minutes and return in words
    if match := re.search("(^[0-9]{4})-(0[0-9]|1[0-2])-(0[0-9]|1[0-9]|2[0-9]|3[0-1]$)", s):
        age = date.today() - date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        return f"{p.number_to_words(age.days * 24 * 60, andword='').capitalize()} minutes"
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()