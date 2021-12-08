import re
from collections import defaultdict
from math import copysign as sign

def buildVents(data, blockDiag=True):
    vents = defaultdict(lambda:0)

    for (a, b, x, y) in data:
        if blockDiag and a != x and b != y: continue
        i, j = a, b
        xDir = int(sign(1, x-a)) if x != a else 0
        yDir = int(sign(1, y-b)) if y != b else 0
        while i != x or j != y:
            vents[(i,j)] += 1
            i, j = i+xDir, j+yDir
        vents[(i,j)] += 1
    return len([v for v,a in vents.items() if a > 1])

def part1(data):
    return buildVents(data)

def part2(data):
    return buildVents(data, False)
    
def main():
    with open('input.txt') as f:
        data = [[int(x) for x in ent] for ent in re.findall(r'(\d+),(\d+) -> (\d+),(\d+)', f.read().strip())]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
