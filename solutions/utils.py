def read_input_file(day, sep="\n", debug=False):
    """Reads daily input file and returns a list"""
    if debug:
        file_path = f'./input/day{day}_dev.txt'
    else:
        file_path = f'./input/day{day}.txt'
    with open(file_path) as f:
        l = f.read().rstrip().split(sep)

    return l