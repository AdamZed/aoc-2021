def part1(data):
    pass

def part2(data):
    pass

def main(fname):
    with open(fname) as f:
        data = [x for x in f.read().strip().split()]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)