import sys
from PIL import Image, ImageOps
import os

# Splits the arguments image name and extension name
arg1 = os.path.splitext(sys.argv[1])
arg2 = os.path.splitext(sys.argv[2])

# Checks if the command-line arguments are not exactly three and exit with error message
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Checks if not the second extension matches the list and exit with error message
elif arg2[1] not in [".jpg", ".png", ".jpeg"]:
    sys.exit("Invalid input")

# checks if the argument length is exactly three then proceed
elif len(sys.argv) == 3:

    # Checks if the arguments extension not match and exit with error message
    if arg1[1] != arg2[1]:
       sys.exit("Input and output have different extensions")

    else:
        # Open input image
        shirt = Image.open("shirt.png")
        muppet = Image.open(sys.argv[1])

        # resize the input image
        shirty = ImageOps.fit(muppet, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

        # Paste and save to second to third argument
        shirty.paste(shirt, shirt)
        shirty.save(sys.argv[2])
