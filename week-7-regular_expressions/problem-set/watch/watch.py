import re


def main():
    # Get user input and parse the YouTube video URL
    print(parse(input("HTML: ")))


def parse(s):
    # Regular expression pattern to match the YouTube video URL in the HTML
    if matches := re.search(r'"https?://(?:www\.)?youtube\.com/embed/(.+?)"', s):
        # Return the final YouTube video URL using the captured video ID
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
