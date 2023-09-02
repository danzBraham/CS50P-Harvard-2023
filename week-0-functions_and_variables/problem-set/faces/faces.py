def main():
    # Ask user's prompt
    prompt = input("Prompt: ")

    # Print the prompt
    print(convert(prompt))


def convert(str):
    # Convert emoticons to emoji
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()