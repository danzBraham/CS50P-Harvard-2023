def main():
    # Ask user's plate
    plate = input("Plate: ")
    # Check if the plate is valid and print the result
    print("Valid") if is_valid(plate) else print("Invalid")


def is_valid(string):
    # Get the length of the string
    string_len = len(string)

    # Check the length of the string
    if string_len < 2 or string_len > 6:
        return False

    # Check if all characters are alphanumeric
    if not string.isalnum():
        return False

    # Check the first character
    if not string[0].isalpha():
        return False

    # Check if the string consists of only alphabetic characters
    if string.isalpha():
        return True

    # Check for numbers in the middle or invalid first number
    for i in range(1, string_len):
        if string[i] == "0":
            return False
        if string[i].isdigit():
            if not string[i + 1 :].isdigit():
                return False
            return True

    return False


if __name__ == "__main__":
    main()
