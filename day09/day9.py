from functools import reduce
from operator import mul

def part1(data):
    score = 0
    for x, row in enumerate(data):
        for y, val in enumerate(row):
            if ((x > 0 and data[x-1][y] <= val) or
                (x+1 < len(data) and data[x+1][y] <= val) or
                (y > 0 and row[y-1] <= val) or
                (y+1 < len(row) and row[y+1] <= val)):
                continue
            score += 1 + val
    return score

def explore(data, i, j):
    if i < 0 or i >= len(data): return 0
    if j < 0 or j >= len(data[i]): return 0
    if not data[i][j]: return 0
    data[i][j] = False
    return (1 + explore(data, i-1, j) + explore(data, i+1, j) +
        explore(data, i, j-1) + explore(data, i, j+1))

def part2(data):
    data = [[v != 9 for v in row] for row in data]
    basins = []
    for x, row in enumerate(data):
        for y, val in enumerate(row):
            if val: basins.append(explore(data, x, y))
    return reduce(mul, sorted(basins)[-3:], 1)

def main(fname):
    with open(fname) as f:
        data = [[int(x) for x in row] for row in f.read().strip().split('\n')]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)