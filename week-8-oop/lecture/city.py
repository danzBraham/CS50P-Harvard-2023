import random


class City:
    # Class variable
    cities = ["Denpasar", "Gianyar", "Badung", "Jimbaran"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.cities)}")


def main():
    City.sort("zidan")


if __name__ == "__main__":
    main()
