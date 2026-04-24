import json
import csv


def json_to_csv(json_file_path, csv_file_path):
    try:
        with open(json_file_path, 'r') as jf:
            data = json.load(jf)

        if not data:
            print("JSON file is empty.")
            return

        field_names = data[0].keys()

        with open(csv_file_path, 'w', newline='') as cf:
            writer = csv.DictWriter(cf, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)

        print(f"JSON data successfully converted to {csv_file_path}")

    except FileNotFoundError:
        print("JSON file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
    except Exception as err:
        print(f"An error occurred: {err}")


def main():
    json_file_path = "data.json"
    csv_file_path = "output.csv"
    json_to_csv(json_file_path, csv_file_path)


if __name__ == "__main__":
    main()