# Initialize a variable
coke = 50

# Using while loop and asks user for an input of integer
while True:
    amount = int(input("Insert Coin: "))
    amounts = [25, 10, 5]

    # prints message when user inserts invalid coins and prompt's user for input again
    if  amount not in amounts:
        print("Amount due: 50")
        continue

    # Calculates the change and prints it
    coke -= amount
    if coke > 0:
        print(f"Change owed: {str(abs(coke))}")

    # prints change and break out
    else:
        print(f"Change owed: {str(abs(coke))}")
        break





