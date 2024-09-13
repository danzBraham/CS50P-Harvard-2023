import random
import sys
from pyfiglet import Figlet


def main():
    num_args = len(sys.argv)

    f = Figlet()
    fonts = f.getFonts()

    if num_args == 1:
        f.setFont(font=random.choice(fonts))
    elif num_args == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Usage: python figlet.py -f font_name")

        font_name = sys.argv[2]
        if font_name not in fonts:
            sys.exit("Font name does not exist")
        f.setFont(font=font_name)
    else:
        sys.exit("Invalid usage")

    s = input("Input: ")
    print(f"Output:\n{f.renderText(s)}")


if __name__ == "__main__":
    main()
