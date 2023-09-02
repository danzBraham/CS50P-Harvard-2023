# THIS PROGRAM IS TO EXTRACT USER'S USERNAME FROM TWITTER
import re
import sys


def main():
    url = input("URL: ")
    username = extract_username(url)
    print(f"Username: {username}")

    # Using replace
    # username = url.replace("https://twitter.com/", "")

    # Using removeprefix
    # username = url.removeprefix("https://twitter.com/")

    # Using split
    # username = url.split("/")[-1]


def extract_username(url):
    # THE BEST METHOD is using regex (regular expression)
    if username := re.search(
        r"^(?:https?://)?(?:www\.)?twitter\.com/((?!home\b)[a-z0-9]+)",
        url,
        re.IGNORECASE,
    ):
        return username.group(1)
    sys.exit("The username was not found")


if __name__ == "__main__":
    main()
