def main():
    # Ask user's plate
    plate = input("Plate: ")
    # Check if the plate is valid and print the result
    print("Valid") if is_valid(plate) else print("Invalid")


def is_valid(str):
    str_len = len(str)

    if str_len < 2 or str_len > 6:
        return False

    if str[:2].isalpha():
        digit = ""
        digit_in_middle = False

        for c in str[2:]:
            if c.isdigit():
                digit += c
                digit_in_middle = True
            elif c.isalpha():
                if digit_in_middle:
                    return False
            else:
                return False

        if len(digit) != 0 and digit[0] == "0":
            return False

        return True

    return False


if __name__ == "__main__":
    main()
