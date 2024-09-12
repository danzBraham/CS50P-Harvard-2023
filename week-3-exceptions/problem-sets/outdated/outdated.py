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


def main():
    while True:
        try:
            date = input("Date: ").split("/")
            if len(date) == 3:
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])
            else:
                month, day, year = date[0].split(" ")
                for i in range(len(months)):
                    if months[i] == month:
                        month = i + 1
                if day.endswith(","):
                    day = int(day.removesuffix(","))
                else:
                    raise ValueError
                year = int(year)

            if month > 12 or day > 31:
                raise ValueError

            print(f"{year}-{month:02}-{day:02}")
            break
        except Exception:
            pass


main()
