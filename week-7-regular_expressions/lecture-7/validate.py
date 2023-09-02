import re


def main():
    email = input("What's your email? ").strip()

    if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
9