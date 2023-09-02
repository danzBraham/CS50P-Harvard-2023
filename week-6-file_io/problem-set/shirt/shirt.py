import os
from PIL import Image, ImageOps
import sys


def main():
    # Validate command-line arguments
    validate_command_line_arguments()

    # Get the input and output filename from command-line argument
    infile = sys.argv[1]
    outfile = sys.argv[2]

    # Validate file extension
    validate_file_extension(infile, outfile)

    # Edit the image
    edit_image(infile, outfile)


def validate_command_line_arguments():
    # Check the number of command-line arguments
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    elif arg_len > 3:
        sys.exit("Too many command-line arguments")


def validate_file_extension(infile, outfile):
    in_ext = os.path.splitext(infile)[-1].lower()
    out_ext = os.path.splitext(outfile)[-1].lower()

    # Check output file extension
    if out_ext not in [".jpeg", ".jpg", ".png"]:
        sys.exit("Invalid output")

    # Matching both file extensions
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")


def edit_image(infile, outfile):
    try:
        # Open input image
        photo = Image.open(infile)
        # Open shirt image
        shirt = Image.open("shirt.png")
        # Get the size of the shirt image
        size = shirt.size
        # Resize the input image to fit the shirt size
        photo = ImageOps.fit(photo, size)
        # Overlay the shirt image onto the input image
        photo.paste(shirt, shirt)
        # Save the resulting image to the output file
        photo.save(outfile)
    except FileNotFoundError:
        sys.exit("Input or shirt image file not found")


if __name__ == "__main__":
    main()
