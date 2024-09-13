def main():
    word = input("Input : ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    for c in word:
        if c.lower() in ["a", "i", "u", "e", "o"]:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()
