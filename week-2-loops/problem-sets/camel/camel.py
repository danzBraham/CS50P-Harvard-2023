def main():
    camelCase = input("camelCase: ")
    print(f"snake_case: {snake_case(camelCase)}")


def snake_case(str):
    for i in range(len(str)):
        if str[i].isupper():
            str = str.replace(str[i], "_" + str[i].lower())
    return str


main()
