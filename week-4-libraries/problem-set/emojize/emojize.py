import emoji


def main():
    # Ask user's input
    prompt = input("Input: ")
    # Convert user's input and than print
    print(emoji.emojize(f"Output: {prompt}", language="alias"))


if __name__ == "__main__":
    main()
