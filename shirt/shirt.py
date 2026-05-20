import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = {".jpg", ".jpeg", ".png"}
    in_ext = os.path.splitext(input_file)[1].lower()
    out_ext = os.path.splitext(output_file)[1].lower()

    if in_ext not in valid_extensions or out_ext not in valid_extensions:
        sys.exit("Invalid input")
    if in_ext != out_ext and not (in_ext in {".jpg", ".jpeg"} and out_ext in {".jpg", ".jpeg"}):
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, shirt)
    photo.save(output_file)

main()