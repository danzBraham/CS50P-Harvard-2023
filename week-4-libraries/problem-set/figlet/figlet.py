from pyfiglet import Figlet
import random
import sys


def main():
    # Get the number of command-line arguments
    num_args = len(sys.argv)
    # Create an instance of Figlet
    figlet = Figlet()
    # Get the available fonts
    fonts = figlet.getFonts()

    # If no command-line arguments provided, choose a random font
    if num_args == 1:
        figlet.setFont(font=random.choice(fonts))
    # If two command-line arguments provided for font selection
    elif num_args == 3:
        # Validate the command-line arguments
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        figlet.setFont(font=sys.argv[2])
    # If an invalid number of command-line arguments provided
    else:
        sys.exit("Invalid usage")

    # Get user input for the prompt
    prompt = input("Input: ")
    # Render and print the Figlet text
    print("Output:", figlet.renderText(prompt), sep="\n")


if __name__ == "__main__":
    main()
