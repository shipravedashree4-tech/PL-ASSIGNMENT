import csv


def count_rows(file_path):
    try:
        with open(file_path, 'r', newline='') as f:
            csv_reader = csv.reader(f)
            total_rows = sum(1 for _ in csv_reader)
        print(f"Total number of rows: {total_rows}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    file_path = "C:/Users/Prannoy/OneDrive/sample-pl.csv"
    count_rows(file_path)


if __name__ == "__main__":
    main()