import sys
import sayings


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: ./python say.py your_name")

    sayings.hello(sys.argv[1])
    sayings.goodbye(sys.argv[1])


main()
