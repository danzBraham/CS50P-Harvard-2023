def main():
    yell("I", "am", "the", "most", "overpower", "Batman")


def yell(*words):
    # Using map
    # uppercased = map(str.upper, words)
    # print(*uppercased)

    # Using list comprehensions a.k.a pythonic way
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
