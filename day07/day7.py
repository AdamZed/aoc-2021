def part1(data):
    return min([sum([abs(y-x) for y in data]) for x in range(min(data), max(data)+1)])

def part2(data):
    return min([sum([(z := abs(y-x))*(z+1)//2 for y in data]) for x in range(min(data), max(data)+1)])

def main():
    with open('input.txt') as f:
        data = [int(x) for x in f.read().strip().split(',')]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
