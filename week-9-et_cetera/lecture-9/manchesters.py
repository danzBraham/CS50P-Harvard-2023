def main():
    people = ["Zidan", "Abraham", "John"]

    # enumerate
    for i, person in enumerate(people):
        print(f"{i + 1}. {person}")

    print()

    # Using dict comprehensions
    manchesters = {person: "Manchester" for person in people}
    print(manchesters)


if __name__ == "__main__":
    main()
