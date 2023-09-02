import sys
import sayings


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    sayings.hello(sys.argv[1])
    sayings.goodbye(sys.argv[1])


if __name__ == "__main__":
    main()
