import csv
from typing import Dict, List, Tuple

from tabulate import tabulate


def read_csv(file_path: str, verbose: bool = True) -> Tuple[List[Dict], List]:
    data = []
    header = []

    # Read CSV file
    with open(file_path, "r") as f:
        reader = csv.reader(f)

        for index, row in enumerate(reader):
            # Header is the first row
            if index == 0:
                header = row
                continue

            # Append data as dictionary
            data.append(dict(zip(header, row)))

    # Print sample data
    if verbose:
        print(f"Sample {file_path}")
        print(tabulate(data[:5], headers="keys", tablefmt="grid"))

    # Return statement
    return data, header


def drop_duplicates(data) -> List[Dict]:
    # * Add row to set if not seen before
    # * If the row is seen before, drop it
    seen = set()
    return [row for row in data if tuple(row.items()) not in seen and not seen.add(tuple(row.items()))]


def fill_missing_values(data: List[Dict]):
    for row in data:
        # * setdefault for row don't have the key
        # * else if the value is empty, fill it with default value

        # Timezone is UTC+0000 if not provided
        row.setdefault("{timezone}", "UTC+0000")
        row["{timezone}"] = row["{timezone}"] or "UTC+0000"

        # Created at is 0 if not provided
        row.setdefault("{created_at}", "0")
        row["{created_at}"] = row["{created_at}"] or "0"

        # Fill missing values with "Unknown"
        for h in ["{os_name}", "{device_type}", "{store}", "{platform}"]:
            row.setdefault(h, "Unknown")
            row[h] = row[h] or "Unknown"

    return data


def save_csv(data: List[Dict], header: List, file_path: str):
    with open(file_path, "w") as f:
        # Write header
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

        # Write data
        for row in data:
            writer.writerow(row)


def main():
    print("======== Part 1 ========")

    # Read CSV files
    data_1, header_1 = read_csv("./test_1.csv")
    data_2, header_2 = read_csv("./test_2.csv")

    # Merge header and data
    merged_data = [*data_1, *data_2]
    merged_header = set([*header_1, *header_2])

    # Drop duplicates
    dropped_data = drop_duplicates(merged_data)

    # Fill missing values
    filled_data = fill_missing_values(dropped_data)

    # Print sample filled data
    print("Sample filled")
    print(tabulate(filled_data[:5], headers="keys", tablefmt="grid"))

    # Save filled data to CSV
    save_csv(filled_data, merged_header, "./part_1.csv")

    print("======== Part 1 Done ========")


if __name__ == "__main__":
    main()
