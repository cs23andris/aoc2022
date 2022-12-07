# assignment: https://adventofcode.com/2022/day/7

from utils import read_input_file
from dataclasses import dataclass


dev_mode = False
input = read_input_file("7", debug=dev_mode)

@dataclass
class Dir:
    name: str
    parent: int
    size: int = 0


def count_dir_sizes(input):

    root = Dir("/", -1, 0)
    id = 0
    dir_sums = []
    dir_sums.insert(0, root)
    active_id = id
    current_dirs = []
    current_dirs.append(active_id)

    
    for line in input:
        # print(line)
        # print(f"current dirs: {current_dirs}")
        if line.startswith("$ cd"):
            dir = line[-2:].lstrip()
            #print(f"{dir}")
            if dir != ".." and dir != "/":
                id += 1
                d = Dir(dir, active_id, 0)
                dir_sums.insert(id, d)
                active_id = id
                current_dirs.append(active_id)
            elif dir == "..":
                current_dirs.remove(active_id)
                active_id = dir_sums[active_id].parent

        elif line.startswith("$ ls"):
            continue
        else:
            if line.startswith("dir"):
                continue
            else:
                f_size = int(line.split()[0])
                for id in current_dirs:
                    dir_sums[id].size += f_size 

    return dir_sums


def part1(dirs):
    size_of_max_100000s = [d.size for d in dirs if d.size <= 100000]

    return sum(size_of_max_100000s)

def part2(dirs):
    disk_space = 70000000
    update_space = 30000000
    available_space = disk_space - dirs[0].size
    req_space = update_space - available_space

    potentials = [d.size for d in dirs if d.size >= req_space]

    return min(potentials)


if __name__ == "__main__":

    dirs = count_dir_sizes(input)
    print(f"Part 1 solution: {part1(dirs)}")
    print(f"Part 2 solution: {part2(dirs)}")

