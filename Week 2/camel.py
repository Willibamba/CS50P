# Prompt's user for camel case input and print in snake case
def main():
    camelCase = input("camelCase: ")
    print(snake_case(camelCase))

# converts camel case words to snake case words
def snake_case(camel):
    for i in camel:
        if i.isupper():
            cam = "_" + i.lower()
            camel = camel.replace(i, cam)

    return camel

main()