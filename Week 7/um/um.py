import re


def main():
    print(count(input("Text: ")))

# Finds and returns for the number of count of "um" word in a string
def count(s):
    return len(re.findall(r"\bum", s, re.IGNORECASE))





if __name__ == "__main__":
    main()