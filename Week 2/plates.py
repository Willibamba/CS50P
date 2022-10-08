
def main():

    # Prompts user for input of number plates
    s = input("Plates: ")

    # Prints "Valid" if input is valid number plate else "invalid"
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")

#
def is_valid(s):
    plates = len(s)
    # Checks for min 2 chars and max 6 chars
    if plates >= 2 and plates <= 6:
        for letters in s:

            # break out if not alphanumeric and first two chars not letters
            if not s.isalnum() or not s[0:2].isalpha():
                break

            # Checks if all the characters in the string are letters
            if s.isalpha():
                return True

            # Checks if first two chars are letters
            if s[0:2].isalpha():


                # Checks if second to last chars is exactly 0
                if s[-2] == "0":
                    return False

                # Checks if last three chars are alphanumeric
                if s[1:-2].isalnum():

                        # Checks if all last three is either letters or digits
                        if s[1:-2].isalpha() or s[1:-2].isdigit():
                            return True

                        # Checks if the last char is letter or the last three char starts with 0
                        elif s[-1].isalpha() or s[-3].startswith("0"):
                            return False
                            
    else:
        False

main()