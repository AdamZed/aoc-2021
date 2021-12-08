from math import floor, ceil

def part1(data):
    med = sorted(data)[len(data)//2]
    return sum(abs(y-med) for y in data)

def part2(data):
    avg = sum(data)/len(data)
    return min(
        sum((dx := abs(y-floor(avg)))*(dx+1)//2 for y in data),
        sum((dx := abs(y-ceil(avg)))*(dx+1)//2 for y in data),
    )

def main():
    with open('input.txt') as f:
        data = [int(x) for x in f.read().strip().split(',')]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
