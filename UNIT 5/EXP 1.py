def read_file():
    file_name = input("Enter the filename: ")

    try:
        with open(file_name, 'r') as f:
            data = f.read()
        print("File Content:")
        print(data)

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


def main():
    read_file()


if __name__ == "__main__":
    main()