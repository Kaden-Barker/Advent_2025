"""Ranges are separated with dashes
New ranges are separated with commas
eg. 2-4,6-8
ids will never start with 0"""


from pathlib import Path

def find_invalid_ids(start, end):
    invalid_ids = []
    for i in range(int(start), int(end) + 1):
        length = len(str(i))
        if length % 2 != 0:
            continue
        mid = length // 2
        first_half = str(i)[:mid]
        second_half = str(i)[mid:]

        if first_half == second_half:
            invalid_ids.append(i)
    return invalid_ids


def main():

    file_path = Path(__file__).parent / "input.txt"
    with open(file_path, "r") as f:
        lines = f.readlines()
        invalid_ids = []
        for line in lines:
            line = line.strip()
            ranges = line.split(",")

            for r in ranges:
                start, end = r.split("-")
                start, end = start, end

                invalid = find_invalid_ids(start, end)
                invalid_ids.extend(invalid)


        invalid_total = 0
        for invalid in invalid_ids:
            invalid_total += int(invalid)
        print(f"Total invalid IDs: {invalid_total}")
main()