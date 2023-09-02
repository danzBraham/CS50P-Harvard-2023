def main():
    # Ask the user's input word
    vowels = input("Input: ")
    # Print the output without vowels
    print(f"Output: {shorten(vowels)}")


def shorten(word):
    # Iterate over each character in the word
    for c in word:
        # Check if the character (in lowercase) is a vowel
        if c.lower() in ["a", "e", "i", "o", "u"]:
            # If it's a vowel, replace it with an empty word
            word = word.replace(c, "")

    # Return the word without vowels
    return word


if __name__ == "__main__":
    main()
