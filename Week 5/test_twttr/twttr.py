
def main():
    get = input("Input: ")

    print(shorten(get))


def shorten(word):
    # assign a variable to list for holding values of vowels
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    # assign an empty
    output = ""

    # Iterate through user input and vowels then add non-vowels to output
    for i in range(len(word)):
        if word[i] not in vowels:
            output += word[i]
    return output


if __name__ == "__main__":
    main()