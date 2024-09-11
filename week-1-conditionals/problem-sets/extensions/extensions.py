def main():
    print_extension(input("File: "))


def print_extension(file):
    file_extension = file.split(".")[-1].strip().lower()

    if file_extension == "jpg":
        file_extension = "jpeg"

    match file_extension:
        case "gif" | "jpeg" | "png":
            print(f"image/{file_extension}")
        case "pdf" | "zip":
            print(f"application/{file_extension}")
        case "txt":
            print(f"text/plain")
        case _:
            print(f"application/octet-stream")


main()
