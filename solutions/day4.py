# assignment: https://adventofcode.com/2022/day/4

from utils import read_input_file

input = read_input_file("4")

def part1(input):

    cnt = 0
    for line in input:
        a, b = line.split(",")
        a_min, a_max = map(int, str(a).split("-"))
        b_min, b_max = map(int, str(b).split("-"))

        set_a = set(range(a_min,a_max + 1))
        set_b = set(range(b_min,b_max + 1))
        if set_a.issuperset(set_b) or set_b.issuperset(set_a):
            cnt += 1
    
    return cnt

def part2(input):

    cnt = 0
    for line in input:
        a, b = line.split(",")
        a_min, a_max = map(int, str(a).split("-"))
        b_min, b_max = map(int, str(b).split("-"))

        set_a = set(range(a_min,a_max + 1))
        set_b = set(range(b_min,b_max + 1))
        
        if len(set_a.intersection(set_b)) > 0:
            cnt += 1
    
    return cnt

if __name__ == "__main__":

    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")

