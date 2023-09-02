def main():
    # Ask the user's input string
    vowels = input("Input: ")
    # Print the output without vowels
    print(f"Output: {no_vowels(vowels)}")


def no_vowels(string):
    # Iterate over each character in the string
    for c in string:
        # Check if the character (in lowercase) is a vowel
        if c.lower() in ["a", "e", "i", "o", "u"]:
            # If it's a vowel, replace it with an empty string
            string = string.replace(c, "")

    # Return the string without vowels
    return string


if __name__ == "__main__":
    main()
