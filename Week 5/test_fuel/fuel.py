
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:

        # Try to check if user input meets the conditions then returns it
        try:

            # Splits the input by division symbol and assigns it
            fraction = fraction.split("/")
            first = int(fraction[0])
            second = int(fraction[1])

            # Multiply the division of the inputs by 100
            gauge = (first / second) * 100

            # Rounded to nearest integer
            gauge = round(gauge)

            # first division if greater than second division prompt user
            if first > second:
                fraction
            return gauge

        # Do nothing with error
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage <= 98 and percentage >= 2:
        return f"{percentage}%"

    elif percentage >= 99:
        return "F"


if __name__ == "__main__":
    main()