
# list for months
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

# main function for printing output
def main():
    date = validate()
    print(date)

# A function to check for date validation and convert to date format (YYYY-MM-DD)
def validate():
    while True:


        try:
            date = input("Date: ")

            # Validate date format of 1/1/2002
            if "/" in date:
                date = date.split("/")
                month = date[0].strip().zfill(2)
                day = date[1].strip().zfill(2)
                year = date[2].strip()

                if int(month) <= 12 and int(day) <= 31:
                    return f"{year}-{month}-{day}"

            # Validate date format of September 8, 2202
            elif ", " in date:
                date = date.split(", ")
                year = date[1]
                month_day = date[0].split(" ")
                day = month_day[1].zfill(2)
                month = months.index(month_day[0]) + 1


                if int(day) <= 31:
                    return f"{year}-{month:02}-{day}"


        except ValueError:
                pass




main()
