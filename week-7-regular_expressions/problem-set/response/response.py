import validators


def main():
    # Prompt the user to enter an email address
    email = input("What's your email address? ")

    # Validate the email address
    if validate_email_address(email):
        print("Valid")
    else:
        print("Invalid")


def validate_email_address(email):
    # Use the validators.email function to validate the email address
    return validators.email(email)


if __name__ == "__main__":
    main()
