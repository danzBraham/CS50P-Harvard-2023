def main():
    # Ask user for the time
    time = input("What time is it? ")
    # Convert the time to a numerical representation
    time = convert(time)

    # Check the time range and print the corresponding message
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    # Split the time into hour, minutes, and twelve-hour clock indicator
    hour, minutes = time.split(":")
    minutes = minutes.split(" ")[0]

    hour = float(hour)
    minutes = float(minutes)

    # Convert the time to a numerical representation
    if 0 < hour < 12 and "p.m." in time:
        # If it's PM, add 12 hours to the hour
        return (hour + minutes / 60.0) + 12.0
    else:
        # If it's AM, return the time as is
        return hour + minutes / 60.0


if __name__ == "__main__":
    main()
