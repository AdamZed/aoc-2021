import re
from itertools import pairwise
from collections import defaultdict

def run(initial, maps, rounds):
    pairs = defaultdict(lambda:0)
    last_char = initial[-1]
    for l,r in pairwise(initial):
        pairs[(l,r)] += 1
    for _ in range(rounds):
        next = defaultdict(lambda:0)
        for (l, r), cnt in pairs.items():
            m = maps[f'{l}{r}']
            next[(l,m)] += cnt
            next[(m,r)] += cnt
        pairs = next

    counts = defaultdict(lambda:0)
    counts[last_char] += 1
    for (l,r), cnt in pairs.items():
        counts[l] += cnt
    counts = sorted([v for _,v in counts.items()])
    return counts[-1] - counts[0]

def part1(initial, maps):
    return run(initial, maps, 10)

def part2(initial, maps):
    return run(initial, maps, 40)

def main(fname):
    with open(fname) as f:
        initial, mappings = f.read().strip().split("\n\n")

    mappings = {k:v for k,v in re.findall(r"([A-Z]{2}) -> (.)", mappings)}

    print(f'Part 1: {part1(initial, mappings)}')
    print(f'Part 2: {part2(initial, mappings)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)