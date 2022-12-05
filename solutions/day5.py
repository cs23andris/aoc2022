# assignment: https://adventofcode.com/2022/day/5

from utils import read_input_file
from collections import deque
import string, re

ab = string.ascii_uppercase

dev_mode = False
input = read_input_file("5", debug=dev_mode)

def parse_stack(input):

    cs = {}
    for line in input:
        if line[1] == "1":
            break
        crates_in_line = {i: j for i, j in enumerate(line) if j in ab}
        for stack_no, crate in crates_in_line.items():
            stack_no = int((stack_no - 1) / 4 + 1)
            if cs.get(stack_no) is not None:
                cs.get(stack_no).append(crate)
            else:
                cs[stack_no] = deque([crate])

    return cs

def parse_moves(input):
    moves = []
    
    for line in input:
        if line.startswith("move"):
            moves.append(re.findall(r'\d+', line))

    return moves

def move_crate(move_details, stack, crane_version):
    quantity = int(move_details[0])
    from_ = int(move_details[1])
    to_= int(move_details[2])
    print(f"move {quantity} {from_=} {to_=}")

    if crane_version == "9000":
        for i in range(quantity):
            crate = stack[from_].popleft()
            stack[to_].appendleft(crate)
    
    if crane_version == "9001":
        stack[from_], stack[to_] = list(stack[from_]), list(stack[to_])
        crates_to_move = stack[from_][:quantity]
        stack[to_] = crates_to_move + stack[to_]
        stack[from_] = stack[from_][quantity:]
    

def rearrange(input, crane_version="9000"):
    stack = parse_stack(input)
    moves = parse_moves(input)

    for move in moves:
        move_crate(move, stack, crane_version)
    
    r = [v[0] for k,v in dict(sorted(stack.items())).items()]

    result = "".join([v[0] for k,v in dict(sorted(stack.items())).items()])
    return result

if __name__ == "__main__":

    print(f"Part 1 solution: {rearrange(input, crane_version='9000')}")
    print(f"Part 2 solution: {rearrange(input, crane_version='9001')}")