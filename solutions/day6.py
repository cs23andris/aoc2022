# assignment: https://adventofcode.com/2022/day/6

from utils import read_input_file

dev_mode = False
input = read_input_file("6", debug=dev_mode)

def detector(input, distinct_chars=4):

    i_str = "".join(input)
    for i in range(len(i_str)):
        #print(f"{i=}, {i_str[i:i+4]}")
        if len(set(i_str[i:i+distinct_chars])) == distinct_chars:
            return i+distinct_chars

if __name__ == "__main__":

    print(f"Part 1 solution: {detector(input, distinct_chars=4)}")
    print(f"Part 2 solution: {detector(input, distinct_chars=14)}")

