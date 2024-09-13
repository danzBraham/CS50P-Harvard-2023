def main():
    au = input("AU: ")
    while True:
        try:
            au = float(au)
            break
        except ValueError:
            pass

    print(f"{au} AU is {convert(au)} m")


def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")
    return au * 149597870700


if __name__ == "__main__":
    main()
