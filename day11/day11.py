import re

def dump(data):
    print('====')
    for row in data:
        print(''.join(str(x) for x in row))

def pulse(data, i, j, initial=False):
    if i < 0 or j < 0 or i >= len(data) or j >= len(data[i]):
        return 0
    if data[i][j] == 0: return 0
    if not initial: data[i][j] += 1
    if data[i][j] < 10:
        return 0
    data[i][j] = 0
    props = 1 + pulse(data, i-1, j-1) + pulse(data, i-1, j) + pulse(data, i-1, j+1)
    props += pulse(data, i, j-1) + pulse(data, i, j+1)
    props += pulse(data, i+1, j-1) + pulse(data, i+1, j) + pulse(data, i+1, j+1)
    return props

def part1(data):
    pulses = 0
    for _ in range(100):
        for row in data:
            for j in range(len(row)):
                row[j] += 1
        for i in range(len(data)):
            for j in range(len(data[i])):
                pulses += pulse(data, i, j, initial=True)
    return pulses

def part2(data):
    step = 0
    while (step:=step+1):
        for row in data:
            for j in range(len(row)):
                row[j] += 1
        for i in range(len(data)):
            for j in range(len(data[i])):
                pulse(data, i, j, initial=True)
        if sum(sum(x for x in row) for row in data) == 0:
            return step

def main(fname):
    with open(fname) as f:
        data = [[int(x) for x in re.findall(r"\d{1}", line)] for line in f.readlines()]
    data_cpy = [[x for x in row] for row in data]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data_cpy)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)