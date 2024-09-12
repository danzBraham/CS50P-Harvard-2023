def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            if x > y:
                raise ZeroDivisionError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
                return
            if percentage >= 99:
                print("F")
                return

            print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            pass


main()
