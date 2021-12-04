import re

def part1(data):
    x, y = 0, 0
    for d, delta in data:
        if d == 'forward': x += delta
        elif d == 'up': y -= delta
        elif d == 'down': y += delta
    return x*y

def part2(data):
    x, y, aim = 0, 0, 0
    for d, delta in data:
        if d == 'forward':
            x += delta
            y += delta*aim
        elif d == 'up': aim -= delta
        elif d == 'down': aim += delta
    return x*y

def main():
    with open('input.txt') as f:
        data = [(d, int(x)) for d, x in re.findall(r'(forward|up|down) (\d+)', f.read().strip())]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
