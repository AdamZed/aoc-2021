from collections import Counter

def reproduce(data, days):
    spawns = [(k,v) for k,v in Counter(data).items()]
    for _ in range(days):
        newfish = 0
        for i, (age, cnt) in enumerate(spawns):
            if age == 0: newfish += cnt
            spawns[i] = (age-1 if age > 0 else 6, cnt)
        spawns.append((8, newfish))

    return sum(cnt for _,cnt in spawns)

def part1(data):
    return reproduce(data, 80)

def part2(data):
    return reproduce(data, 256)

def main():
    with open('input.txt') as f:
        data = [int(x) for x in f.read().strip().split(',')]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
