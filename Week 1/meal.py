# Prompt's user for an input and calls convert function
def main():
    meal = input("What time is it? ")
    meal = convert(meal)

    if 7.0 <= meal <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        print("dinner time")


# Converts time string to floating point number
def convert(time):
    h, m = time.split(":")
    h = float(h)
    m = float(m) / 60
    return h + m



if __name__ == "__main__":
    main()