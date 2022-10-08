
def main():
    Hello = input("Greeiting: ").lower().strip()
    amount = value(Hello)
    print(f"${amount}")


def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()