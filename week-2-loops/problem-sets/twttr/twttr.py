def main():
    str_input = input("Input : ")
    print(f"Output: {omit_vowel(str_input)}")


def omit_vowel(str):
    for c in str:
        if c.lower() in ["a", "i", "u", "e", "o"]:
            str = str.replace(c, "")
    return str


main()
