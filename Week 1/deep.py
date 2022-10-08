# Prompt user for input, removing white spaces and adjusting to case-sensitive
answer = input("What is the Answer to the Great Question of Life, The Universe, and everything? ").casefold().strip()

# Using a match method for matching strings
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
