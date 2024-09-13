import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")

    for arg in sys.argv[1:]:
        print(f"Hello {arg.title()}!")


if __name__ == "__main__":
    main()
