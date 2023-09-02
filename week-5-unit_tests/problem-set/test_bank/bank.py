def main():
    # Ask user's greeting
    greeting = input("Greeting: ")
    # Print the value of greeting
    print(f"${value(greeting)}")


def value(greeting):
    # Strip greeting and change it to lowercase
    greeting = greeting.lower().strip()

    # Check the greeting
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
