# prompt user for an input
math = input("Expression: ")

# Splits the string input to values
x, y, z = math.split(" ")

# change to float
x = float(x)
z = float(z)

# calculates and print
if y == "*":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "+":
    print(x + z)
else:
    print(x / z)