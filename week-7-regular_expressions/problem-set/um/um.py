import re


def main():
    # Print the number of ums that appear
    print(count(input("Text: ")))


def count(s):
    # Find the "um" word
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        # Returns the total number of "um"
        return len(matches)


if __name__ == "__main__":
    main()
