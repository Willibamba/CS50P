# Asking user for input from and printing
def main():
    x = input()
    convert(x)

# Converting strings to emoticons
def convert(faces):
    s = faces.replace(":)","\U0001F642").replace(":(", "\U0001F641")

    return print(f"{s}")

main()