# https://adventofcode.com/2022/day/1

from utils import read_input_file

input = read_input_file("1")

def calculate_calories_sums(input):
    sums = []
    elf_index = 0
    sums.insert(elf_index, 0)
    for i in input:
        if i == "":
            elf_index += 1
            sums.insert(elf_index, 0)
            continue
        else:
            sums[elf_index] += int(i)

    return sums

def part1(sums):
    return max(sums)

def part2(sums):
    sums_sorted = sorted(sums)
    return sum(sums_sorted[-3:])

if __name__ == "__main__":
    sums = calculate_calories_sums(input)
    print(f"Part 1 solution: {part1(sums)}")
    print(f"Part 2 solution: {part2(sums)}")