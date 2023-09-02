import random


class City:
    cities = ["London", "Manchester", "Birmingham", "Denpasar"]

    @classmethod
    def sort(cls, name):
        return f"{name} lives in {random.choice(cls.cities)}"


def main():
    print(City.sort("Zidan"))


if __name__ == "__main__":
    main()
