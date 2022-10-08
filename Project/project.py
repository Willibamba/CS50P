import random

# Prompt's user for an input of level 1, 2 or 3 and outputs the total score out of 10
def main():
    num = int(input("Level 1, 2, or 3: "))
    if num not in [1, 2, 3]:
        num
    else:
        total = add(num) + subtract(num) + multiply(num) + divide(num)
        print(f"Total Score: {total}")


# Generates integer numbers based on user's level
def random_integer(level):
    try:
        if level == 1:
            return  random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
    except:
        raise ValueError

# Prompt's user for to answer 3 random generated equation of addition based on level
def add(level):
    wrong = 1
    correct = 0

    for x in range(3):
        x = random_integer(level)
        for y in range(1):
            y = random_integer(level)
            answer = x + y
            user = input(f"{x} + {y} = ")
            if int(user) == answer:
                correct += 1
            elif int(user) != answer:
                wrong += 1
                print(f"Sorry answer is {answer}")
                user
    return correct

# Prompt's user for to answer 2 random generated equation of subtraction based on level
def subtract(level):
    wrong = 1
    correct = 0

    for x in range(2):
        x = random_integer(level)
        for y in range(1):
            y = random_integer(level)
            answer = x - y
            user = input(f"{x} - {y} = ")
            if int(user) == answer:
                correct += 1
            elif int(user) != answer:
                wrong += 1
                print(f"Sorry answer is {answer}")
                user
    return correct

# Prompt's user for to answer 3 random generated equation of multiplication based on level
def multiply(level):
    wrong = 1
    correct = 0

    for x in range(3):
        x = random_integer(level)
        for y in range(1):
            y = random_integer(level)
            answer = x * y
            user = input(f"{x} * {y} = ")
            if int(user) == answer:
                correct += 1
            elif int(user) != answer:
                wrong += 1
                print(f"Sorry answer is {answer}")
                user
    return correct

# Prompt's user for to answer 2 random generated equation of division based on level
def divide(level):
    wrong = 1
    correct = 0

    for x in range(2):
        x = random_integer(level)
        for y in range(1):
            y = random_integer(level)
            answer = x / y
            user = input(f"{x} / {y} = ")
            if int(user) == round(answer):
                correct += 1
            elif int(user) != answer:
                wrong += 1
                print(f"Sorry answer is {round(answer)}")
                user
    return correct

if __name__ == "__main__":
    main()