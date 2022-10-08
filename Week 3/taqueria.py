# Dictionaries of keys with associated values
menus = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Variable assign with value of 0
total = 0


while True:
    try:
        # prompts user for an input and coverts to title case words
        items = input("Item: ").title()

        # Add the price to total, prints the total and reprompt user
        for item in menus:
            price = menus[item]

            if items == item:
                total += price
                print(f"Total: ${total:.2f}")
            else:
                continue

    # Ignore when item is not in the menu dictionaries
    except KeyError:
        pass

    # print new line and break out when user ends (Ctrl + D) the program
    except EOFError:
        print("\n")
        break

