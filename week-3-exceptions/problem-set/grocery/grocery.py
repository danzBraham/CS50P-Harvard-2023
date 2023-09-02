def main():
    # Obtain the sorted grocery list
    grocery_list = grocery()

    # Print the counts and items in uppercase
    for item, count in grocery_list.items():
        print(count, item.upper())


def grocery():
    lists = {}

    # Continuously prompt for grocery items
    while True:
        try:
            item = input("").lower()
            # Increment the count of the item in the dictionary
            lists[item] = lists.get(item, 0) + 1
        except EOFError:
            # Handle the EOFError exception
            print()
            break

    # Sort the dictionary by keys and return the sorted dictionary
    return dict(sorted(lists.items()))


if __name__ == "__main__":
    main()
