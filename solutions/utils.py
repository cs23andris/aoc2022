def read_input_file(day, sep="\n", debug=False):
    """Reads daily input file and returns a list"""
    with open(f'./input/day{day}.txt') as f:
        l = f.read().rstrip().split(sep)

    return l