def main():
    # Ask the user for a camelCase string
    camelCase = input("camelCase: ")
    # Convert the camelCase string to snake_case
    print(f"snake_case: {snake_case(camelCase)}")


def snake_case(str):
    # Iterate over each character in the string
    for i in range(len(str)):
        # Check if the character is uppercase
        if str[i].isupper():
            # Replace the uppercase character with "_lowercase"
            str = str.replace(str[i], "_" + str[i].lower())
    return str


if __name__ == "__main__":
    main()
