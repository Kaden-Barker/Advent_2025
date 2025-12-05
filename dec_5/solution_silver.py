"""First part of the input is the ranges
Second part is the igredients
an ingredient is fresh if if is in a range otherwise it is spoiled
count the never of fresh ingredients"""

from pathlib import Path

def main():

    file_path = Path(__file__).parent / "input.txt"
    with open(file_path, "r") as f:
        lines = f.readlines()
        ranges = []
        num_fresh = 0
        isRanges = True 
        for line in lines:
            if "-" not in line:
                isRanges = False

            if isRanges:
                line = line.strip()
                parts = line.split("-")
                ranges.append((int(parts[0]), int(parts[1])))

            else:
                line = line.strip()
                if not line:
                    continue
                ingredient_value = int(line)
                is_fresh = False
                for r in ranges:
                    if ingredient_value >= r[0] and ingredient_value <= r[1]:
                        is_fresh = True
                        break
                if is_fresh:
                    num_fresh += 1


    print(f"Number of fresh ingredients: {num_fresh}")

main()