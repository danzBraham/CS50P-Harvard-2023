def main():
    plate = input("Plate: ")
    if is_valid_plate(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid_plate(str):
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


main()
