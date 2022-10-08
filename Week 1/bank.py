# Prompt user for an input
Hello = input("Greeiting: ").lower().strip()

# Checking for conditions and prints

if "hello" in Hello:
    print("$0")
elif Hello[0] == "h":
    print("$20")
else:
    print("$100")