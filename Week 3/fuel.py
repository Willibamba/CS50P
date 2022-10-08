
# Gets user input
def main():
    gauge = get()

    # rounds number to nearest integer
    gauge = round(gauge)

    # Checks the conditions and prints output in percentage
    if gauge <= 24 and gauge >= 0:
        print("E")
    elif gauge <= 49 and gauge >= 25:
        print(f"{gauge}%")
    elif gauge <= 74 and gauge >= 50:
        print(f"{gauge}%")
    elif gauge == 75:
        print("75%")
    elif gauge <= 100 and gauge >= 76:
        print("F")



# Gets user input
def get():
    while True:

        # Try to check if user input meets the conditions then returns it
        try:
            print("Fraction: cat/dog")

            # Splits the input by division symbol and assigns it
            fraction = input("Fraction: ").split("/")
            first = int(fraction[0])
            second = int(fraction[1])

            # Multiply the division of the inputs by 100
            gauge = (first / second) * 100

            # first division if greater than second division prompt user
            if first > second:
                fraction = input("Fraction: ").split("/")
            return gauge

        # Do nothing with error
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()