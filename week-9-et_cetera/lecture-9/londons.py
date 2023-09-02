def main():
    people = [
        {"name": "Zidan", "city": "Manchester"},
        {"name": "Abraham", "city": "London"},
        {"name": "Thomas", "city": "Birmingham"},
        {"name": "John", "city": "London"},
        {"name": "Jack", "city": "London"},
    ]

    # Using list comprehensions a.k.a pythonic way
    # londons = [person["name"] for person in people if person["city"] == "London"]
    # print(sorted(londons))

    # Using filter
    # people = filter(is_london, people)
    people = filter(lambda s: s["city"] == "London", people)
    for person in sorted(people, key=lambda s: s["name"]):
        print(person["name"])


def is_london(p):
    return p["city"] == "London"


if __name__ == "__main__":
    main()
