# assignment: https://adventofcode.com/2022/day/9

from utils import read_input_file
from dataclasses import dataclass



dev_mode = False
input = read_input_file("9", debug=dev_mode)

@dataclass(eq=True, frozen=True)
class Cor:
    x: int
    y: int


def is_adjacent(a: Cor, b: Cor):
    a_x_adj = [a.x-1, a.x, a.x+1]
    a_y_adj = [a.y-1, a.y, a.y+1]

    if b.x in a_x_adj and b.y in a_y_adj:
        return True
    else:
        return False

def catchup(head_pos, tail_pos) -> Cor:
    if is_adjacent(head_pos, tail_pos):
        #print("tail adjacent")
        new_x = tail_pos.x
        new_y = tail_pos.y

    elif head_pos.x == tail_pos.x:
        #print("x equals, move on y")
        new_y = int(sum([head_pos.y, tail_pos.y]) / 2)
        new_x = tail_pos.x
    elif head_pos.y == tail_pos.y:
        #print("y equals, move on x")
        new_x = int(sum([head_pos.x, tail_pos.x]) / 2)
        new_y = tail_pos.y
    elif head_pos.y != tail_pos.y and  head_pos.x != tail_pos.x:
        #print("move diagonally")
        if abs(head_pos.x - tail_pos.x) == 1:
            new_x = head_pos.x
            if head_pos.y > tail_pos.y:
                new_y = head_pos.y - 1
            if head_pos.y < tail_pos.y:
                new_y = head_pos.y + 1 
        elif abs(head_pos.y - tail_pos.y) == 1:
            new_y = head_pos.y
            if head_pos.x > tail_pos.x:
                new_x = head_pos.x - 1
            if head_pos.x < tail_pos.x:
                new_x = head_pos.x + 1 
        elif abs(head_pos.x - tail_pos.x) == 2:
            new_x = sum([head_pos.x, tail_pos.x]) / 2
            new_y = sum([head_pos.y, tail_pos.y]) / 2  

    #print(f"{Cor(new_x, new_y)}")
    return Cor(new_x, new_y)

def move_head(direction, head_pos: Cor):
    if direction == "R":
        new_head_pos = Cor(head_pos.x+1, head_pos.y)

    if direction == "L":
        new_head_pos = Cor(head_pos.x-1, head_pos.y)

    if direction == "U":
        new_head_pos = Cor(head_pos.x, head_pos.y+1)

    if direction == "D":
        new_head_pos = Cor(head_pos.x, head_pos.y-1)

    return new_head_pos

def part1(input):

    head_current, tail_current = Cor(0,0), Cor(0,0)
    head_all = []
    head_all.append(head_current)
    tail_all = []
    tail_all.append(tail_current)

    for line in input:
        dir, t = line.split()
        #print(dir, t)
        for i in range(int(t)):
            #print(f"{head_current=}, {tail_current=}")
            head_temp = move_head(dir, head_current)
            tail_temp = catchup(head_current, tail_current)
            head_all.append(head_temp)
            tail_all.append(tail_temp)
            head_current = head_temp
            tail_current = tail_temp

    return len(set(tail_all))


def part2(input):
    
    a = [Cor(0,0) for i in range(10)]
    head_all = []
    head_current = a[0]
    head_all.append(a[0])
    tail_all = []
    tail_all.append(a[9])
    

    for line in input:
        dir, t = line.split()
        print(dir, t)
        for j in range(int(t)):
            #print(f"{head_current=}, {tail_current=}")
            print(f"Step {j}")
            head_temp = move_head(dir, head_current)
            head_all.append(head_temp)
            head_current = head_temp
            print(f"H:{head_current}")
            for i in range(9):
                print(f"{head_temp=}, {i=}:{a[i]}")
                a[i] = catchup(head_temp, a[i])
                head_temp = a[i]

            tail_all.append(a[8])

    return len(set(tail_all))

if __name__ == "__main__":

    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")