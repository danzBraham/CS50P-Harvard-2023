def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${convert_to_dollars(greeting)}")


def convert_to_dollars(greeting):
    if greeting.startswith("hello"):
        return 0
    if greeting.startswith("h"):
        return 20
    return 100


main()
