def main():
    people = [
        {"name": "Zidan", "city": "Manchester"},
        {"name": "Abraham", "city": "London"},
        {"name": "Thomas", "city": "Birmingham"},
        {"name": "John", "city": "London"},
        {"name": "Jack", "city": "London"},
    ]

    cities = set()
    for person in people:
        cities.add(person["city"])

    for city in cities:
        print(city)


if __name__ == "__main__":
    main()
