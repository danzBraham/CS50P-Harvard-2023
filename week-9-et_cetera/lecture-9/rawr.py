import argparse


def main():
    parser = argparse.ArgumentParser(description="Rawr like a cat")
    parser.add_argument("-n", default=1, help="number of times to rawr", type=int)
    args = parser.parse_args()

    for _ in range(args.n):
        print("rawr")


if __name__ == "__main__":
    main()
