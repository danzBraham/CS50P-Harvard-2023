import emoji


def main():
    s = input("Input : ")
    print(f"Output: {emoji.emojize(s, language="alias")}")


if __name__ == "__main__":
    main()
