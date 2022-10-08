import sys

try:
    # Checks if command-line arguments is not exactly two and exit with error message
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Checks if second command-line argument is not Python file and exit with error
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Pyton file")

    # Checks if command-line arguments is exactly two and Python file and proceed
    elif len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        code_lines = 0
        comments = 0
        whitespaces = 0

        # Open file strip the lines in read mode
        with open(sys.argv[1], "r") as file:

            # Iterate through the file and strip preceeding whitespces in lines
            for line in file:
                line = line.lstrip()

                # Checks for comments, whitespaces and code lines
                if line.startswith("# "):
                    comments += 1
                elif len(line) < 1:
                    whitespaces += 1
                else:
                    code_lines += 1

        print(code_lines)

except FileNotFoundError:
    sys.exit("File does not exit")