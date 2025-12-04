"""Each row is a bank, each number represents a joltage of one battery
Each value is 1-9, two batteries must be active
Find the two batteries that together have the highest joltage
ex 1245 the highest joltage is battery 3 and 4 with a joltage of 45
batteries cannot be rearraged so the second battery must be after the first battery"""

from pathlib import Path

def find_highest_joltage(line):
    first_joltage = 0
    second_joltage = 0
    for i in range(len(line)):
        if int(line[i]) > int(first_joltage) and (i+1) < len(line):
            first_joltage = line[i]
            second_joltage = 0

            for j in range(i+1, len(line)):
                if int(line[j]) > int(second_joltage):
                    second_joltage = line[j]

    joltage = str(first_joltage) + str(second_joltage)
    return joltage

def main():

    file_path = Path(__file__).parent / "input.txt"
    with open(file_path, "r") as f:
        lines = f.readlines()
        joltage_per_line = []
        for line in lines:
            line = line.strip()
            joltage = find_highest_joltage(line)
            joltage_per_line.append(joltage)
        
        total_joltage = 0
        for joltage in joltage_per_line:
            total_joltage += int(joltage)
        print(f"Total joltage: {total_joltage}")

main()