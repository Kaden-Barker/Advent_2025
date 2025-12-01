'''starts at 50
Dial is a circle and goes from 0 to 99
The first letter of each line is the direction, L is minus, R is plus'''

from pathlib import Path

class Dial:
    def __init__(self):
        self.dial_num = 50



    def right(self, num):
        num_clicks = 0
        for _ in range(num):
            self.dial_num = (self.dial_num + 1) % 100
            if self.dial_num == 0:
                num_clicks += 1
        return num_clicks


        
    def left(self, num):
        num_clicks = 0
        for _ in range(num):
            self.dial_num = (self.dial_num - 1) % 100
            if self.dial_num == 0:
                num_clicks += 1
        return num_clicks





def main():

    file_path = Path(__file__).parent / "input.txt"
    dial = Dial()
    passcode = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:

                line = line.strip()
                if not line:
                    continue
                direction = line[0]
                num = int(line[1:])

                if direction == "R":
                    clicks = dial.right(num)
                else:
                    clicks = dial.left(num)

                passcode += clicks

        print(f"The final passcode is: {passcode}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


main()