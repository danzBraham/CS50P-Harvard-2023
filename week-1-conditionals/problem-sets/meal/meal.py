def main():
    time = input("What time is it? ")
    print_meal_time(convert(time))


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60.0


def print_meal_time(time):
    if 7 <= time <= 8:
        print("breakfast time")
        return
    if 12 <= time <= 13:
        print("lunch time")
        return
    if 18 <= time <= 19:
        print("dinner time")
        return


if __name__ == "__main__":
    main()
