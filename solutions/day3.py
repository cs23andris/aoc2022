# assignment: https://adventofcode.com/2022/day/3

from utils import read_input_file
import string

input = read_input_file("3")
alphabet = string.ascii_lowercase + string.ascii_uppercase


def part1(input):

    big_sum = 0
    for line in input:
        split_in = len(line)//2
        sack1 = set(line[:split_in])
        sack2 = set(line[split_in:])
        shared_items = sack1.intersection(sack2)
        sum_prio = [alphabet.index(item) + 1 for item in shared_items]
        big_sum += sum(sum_prio)
        #print(sum_prio)
    
    return big_sum

def part2(input):

    sum_badges = 0
    l = len(input)
    for line in range(0, l, 3):
        a,b,c = map(set, input[line:line+3])
        badge = list(a.intersection(b).intersection(c))[0]
        #print(badge)
        sum_badges += alphabet.index(badge) + 1

    return sum_badges

if __name__ == "__main__":

    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")

