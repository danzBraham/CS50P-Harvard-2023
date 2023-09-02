def main():
    # Print the formatted new date
    print(newdate())


def newdate():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:
            # Prompt the user for a date
            date = input("Date: ")
            date = date.split("/")

            if len(date) == 3:
                # If the date has three components separated by "/", assume format: "MM/DD/YYYY"
                m, d, y = map(int, date)
            else:
                # If the date has a different format, assume format: "Month DD, YYYY"
                md, y = date[0].split(", ")
                m, d = md.split(" ")
                # Convert the month to its corresponding numeric representation
                m = int(months.index(m.capitalize()) + 1)
                d = int(d)
                y = int(y)

            # Check if the date components are valid
            if m < 1 or m > 12 or d < 1 or d > 31:
                continue

            # Format the date as "YYYY-MM-DD"
            return f"{y}-{m:02}-{d:02}"
        except ValueError:
            pass


if __name__ == "__main__":
    main()
