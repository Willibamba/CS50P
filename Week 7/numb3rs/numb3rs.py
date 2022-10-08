import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    # Regular Expression (Regex) for valid IPv4 address (0.0.0.0 - 255.255.255.255)
    if re.search(r"^(([01]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([01]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){1}$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()