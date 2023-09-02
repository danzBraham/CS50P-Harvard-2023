import inflect

# Create an instance of the Inflect engine
p = inflect.engine()


def main():
    # Create an empty list to store names
    names = []

    while True:
        try:
            # Prompt the user to enter a name
            name = input("Name: ")
            # Add the name to the list
            names.append(name)
        except EOFError:
            # If EOF (End of File) is encountered, break out of the loop
            break

    # Print the farewell message using the Inflect library to join the names
    print("\nAdieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
