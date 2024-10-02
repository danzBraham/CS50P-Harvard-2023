from datetime import date
from inflect import engine
import re
import sys

p = engine()


def main():
    # Prompt the user for the date of birth
    print(calculate_age_in_minutes(input("Date of Birth: ")))


def calculate_age_in_minutes(birth):
    pattern = r"^((?:19|20)[0-9]{2})-(1[0-2]|0[1-9])-(3[0-1]|[0-2][0-9])$"
    if matches := re.fullmatch(pattern, birth):
        # Split the birth date into year, month, and day components
        y, m, d = map(int, matches.groups())

        # Calculate the age in minutes by subtracting the birth date from the current date
        minutes = round((date.today() - date(y, m, d)).total_seconds() / 60)

        # Convert the number of minutes to words using the inflect engine
        return f"{p.number_to_words(minutes, andword='')} minutes".capitalize()

    sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
