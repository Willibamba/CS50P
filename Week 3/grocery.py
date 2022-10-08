
# Empty list and dictionaries to hold the user inputs
list = []
items = {}

while True:
    # prompts user for input then covert to upper case letters
    try:
        item = input(" ").upper()

        # add user input to the list and sort the list in alphabetical order
        list.append(item)
        list.sort()

    # when user ends (Ctrl + D), print the item(s) with the number of items inputted the item
    # and break out of the program
    except EOFError:
        for item in list:
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        for item in items:
            print(items[item], item)
        break