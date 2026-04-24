def write_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)
    print("Data written to file successfully.")


def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
            print("File Content:")
            print(data)
    except FileNotFoundError:
        print("File not found.")


def append_file(file_name, text):
    with open(file_name, 'a') as f:
        f.write(text)
    print("Data appended to file successfully.")


def main():
    file_name = "sample.txt"

    write_file(file_name, "Hello, this is the first line.\n")
    read_file(file_name)
    append_file(file_name, "This is an appended line.\n")
    read_file(file_name)


if __name__ == "__main__":
    main()