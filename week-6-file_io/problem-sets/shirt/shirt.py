import sys
from PIL import Image, ImageOps


def main():
    arg_len = len(sys.argv)
    if arg_len < 3:
        sys.exit("Too few command-line arguments")
    if arg_len > 3:
        sys.exit("Too many command-line arguments")

    file_in = sys.argv[1]
    file_out = sys.argv[2]

    if not file_in.lower().endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid input")
    if not file_out.lower().endswith((".png", ".jpeg", ".jpg")):
        sys.exit("Invalid output")

    if file_in.lower().split(".")[-1] != file_out.lower().split(".")[-1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(file_in) as img, Image.open("./shirt.png") as shirt:
            img = ImageOps.fit(img, shirt.size)
            img.paste(shirt, shirt)
            img.save(file_out)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")


if __name__ == "__main__":
    main()
