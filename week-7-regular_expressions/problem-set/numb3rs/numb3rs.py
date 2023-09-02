import re


def main():
    # Get user input and validate the IPv4 address
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression pattern for validating an IPv4 address:
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$"
    if re.fullmatch(pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()
