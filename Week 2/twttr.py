# Prompt's user for input
get = input("Input: ")

# assign a variable to list for holding values of vowels
vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

# assign an empty
output = ""

# Iterate through user input and vowels then add non-vowels to output
for i in range(len(get)):
  if get[i] not in vowels:
    output += get[i]
print(f"Output: {output}")