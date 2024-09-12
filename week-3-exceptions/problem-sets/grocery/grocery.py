def main():
    groceries = {}

    while True:
        try:
            item = input().upper()
            if groceries.get(item) == None:
                groceries[item] = 1
            else:
                groceries[item] += 1
        except EOFError:
            break

    print()
    for key in sorted(groceries):
        print(f"{groceries[key]} {key}")


main()
