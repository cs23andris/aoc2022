# assignment: https://adventofcode.com/2022/day/10

from utils import read_input_file

dev_mode = True
input = read_input_file("10", debug=dev_mode)

def part1(input):
    cycle = 0
    x = 1
    cycles = [20, 60, 100, 140, 180, 220]
    signal_str_sum = 0

    for line in input:
        
        if cycle in cycles:
            print(f"sum! {cycle=} {(cycle*x)}")
            signal_str_sum += (cycle*x)
            cycles.remove(cycle)
        if line.startswith("addx"):
            inc = int(line.split()[1])
            for i in range(2):
                cycle += 1
                print(f"{line=} {cycle=}, {x=} ")
                if cycle in cycles:
                    print(f"sum! {cycle=} {(cycle*x)}")
                    signal_str_sum += (cycle*x)
                    cycles.remove(cycle)
            x += inc
        else:
            cycle += 1
            print(f"{line=} {cycle=}, {x=} ")

    return signal_str_sum
    

def part2(input):
    cycle = 0
    crt_cycle = 0
    crt_w, crt_h = 40, 6
    x = 1
    sprite = [x-1, x, x+1]
    crt = []
    crt_str = ""

    for line in input:
        crt_str += f"{'#' if crt_cycle in sprite else '.'}"
        if crt_cycle == 39:
            crt.append(crt_str)
            crt_cycle = 0
            
        if line.startswith("addx"):
            inc = int(line.split()[1])
            for i in range(2):
                crt_str += f"{'#' if crt_cycle in sprite else '.'}"
                if crt_cycle == 39:
                    crt.append(crt_str)
                    crt_cycle = 0
                cycle += 1
                print(f"{line=} {cycle=}, {x=} ")
            x += inc
            sprite = [x-1, x, x+1]
        else:
            cycle += 1
            print(f"{line=} {cycle=}, {x=} ")
        
        crt_cycle +=1

    for i in crt:
        print(i)

    return "Over"

if __name__ == "__main__":

    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")
