import re


def main():
    # Print the converted hours from 12-hour clock to 24-hour clock
    print(convert(input("Hours: ")))


def convert(s):
    # Define the pattern to match the input format of hours
    pattern = r"^(1[0-2]|[0-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[0-9])(?::([0-5][0-9]))? (AM|PM)$"

    # Check if the input string matches the pattern
    if matches := re.search(pattern, s):
        (
            first_hour,
            first_minute,
            first_period,
            second_hour,
            second_minute,
            second_period,
        ) = matches.groups()

        # Convert hours to integers
        first_hour = int(first_hour)
        second_hour = int(second_hour)

        # Adjust hour values based on AM/PM designation
        if first_hour == 12:
            first_hour = 0
        if first_period == "PM":
            first_hour += 12

        if second_hour == 12:
            second_hour = 0
        if second_period == "PM":
            second_hour += 12

        # Generate the formatted time string
        if first_minute and second_minute:
            return f"{first_hour:02}:{first_minute:02} to {second_hour:02}:{second_minute:02}"
        elif first_minute:
            return f"{first_hour:02}:{first_minute:02} to {second_hour:02}:00"
        elif second_minute:
            return f"{first_hour:02}:00 to {second_hour:02}:{second_minute:02}"

        return f"{first_hour:02}:00 to {second_hour:02}:00"

    # Raise a ValueError if the input format is invalid
    raise ValueError


if __name__ == "__main__":
    main()
