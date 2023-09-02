import re


def main():
    name = input("What's your name? ").strip().title()
    if matches := re.search(r"^(.+), *(.+)$", name):
        # You can use this:
        # last = matches.group(1)
        # first = matches.group(2)
        # Or this:
        # last, first = matches.groups()
        # name = f"{first} {last}"
        # Or this:
        name = f"{matches.group(2)} {matches.group(1)}"
    print(f"Hello {name}")


if __name__ == "__main__":
    main()
