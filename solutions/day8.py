# assignment: https://adventofcode.com/2022/day/8

from utils import read_input_file
import numpy as np

dev_mode = False
input = read_input_file("8", debug=dev_mode)


def part1(input):

    h = len(input)
    w = len(input[0])
    visible_cnt = 2*h + 2*(w-2)

    grid = np.array([list(line) for line in input])

    for i in range(1, h-1):
        for j in range(1, w-1):
            current_tree = grid[i][j]
            trees_in_hline = grid[i, :]
            trees_in_vline = grid[:, j]
            left = all([tree < current_tree for tree in trees_in_hline[:j]])
            right = all([tree < current_tree for tree in trees_in_hline[j+1:]])
            down = all([tree < current_tree for tree in trees_in_vline[i+1:]])
            up = all([tree < current_tree for tree in trees_in_vline[:i]])
            if any([left, right, up, down]):
                visible_cnt += 1
                #print(f"visible: {current_tree}")
            
            # print(f"{current_tree}:, left:{trees_in_hline[:j]}, right:{trees_in_hline[j+1:],} up:{trees_in_vline[:i]}, down: {trees_in_vline[i+1:]}")
            # print(f" {left=},{right=},{up=},{down=}")        
    return visible_cnt


def part2(input):
        
    h = len(input)
    w = len(input[0])

    max = 0
    l = []

    grid = np.array([list(line) for line in input])

    for i in range(1, h-1):
        for j in range(1, w-1):
            current_tree = grid[i][j]
            trees_in_hline = grid[i, :]
            trees_in_vline = grid[:, j]

            left = list(trees_in_hline[:j])
            right = list(trees_in_hline[j+1:])
            down = list(trees_in_vline[i+1:])
            up = list(trees_in_vline[:i])
            left_cnt, right_cnt, up_cnt, down_cnt = 0,0,0,0
            #print(current_tree, list(left), right, list(up), down)

            for tree in left[::-1]:
                #print(f"left: {tree=}, {current_tree=} ")
                if tree < current_tree:
                    left_cnt += 1
                elif tree >= current_tree:
                    left_cnt += 1
                    break
            
            for tree in right:
                #print(f"right: {tree=}, {current_tree=} ")
                if tree < current_tree:
                    right_cnt += 1
                elif tree >= current_tree:
                    right_cnt += 1
                    break

            for tree in up[::-1]:
                if tree < current_tree:
                    up_cnt += 1
                elif tree >= current_tree:
                    up_cnt += 1
                    break

            for tree in down:
                if tree < current_tree:
                    down_cnt += 1
                elif tree >= current_tree:
                    down_cnt += 1
                    break

            score = left_cnt * right_cnt * up_cnt * down_cnt
            l.append(score)
            #print(left_cnt, right_cnt, up_cnt, down_cnt, score)
            
            if score > max:
                max = score
            
    #print(l)
    return max

if __name__ == "__main__":

    print(f"Part 1 solution: {part1(input)}")
    print(f"Part 2 solution: {part2(input)}")

