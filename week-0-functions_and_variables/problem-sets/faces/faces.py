def main():
    faces(input("Phrase: "))


def faces(phrase):
    print(phrase.replace(":)", "🙂").replace(":(", "🙁"))


main()
