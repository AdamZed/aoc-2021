import re

def fold(dots, is_x_fold, line):
    new_dots = set()
    if is_x_fold:
        for x,y in dots:
            if x > line: new_dots.add((line-(x-line), y))
            else: new_dots.add((x,y))
    else:
        for x,y in dots:
            if y > line: new_dots.add((x, line-(y-line)))
            else: new_dots.add((x,y))
    return new_dots

def part1(data, folds):
    data = fold(data, folds[0][0], folds[0][1])
    return len(data)

def part2(data, folds):
    for f in folds:
        data = fold(data, f[0], f[1])
    X = max(data, key=lambda x: x[0])[0] + 1
    Y = max(data, key=lambda x: x[1])[1] + 1

    for y in range(Y):
        ans = ''
        for x in range(X):
            ans += 'XX' if (x,y) in data else "  "
        print(ans)

def main(fname):
    with open(fname) as f:
        points, folds = f.read().strip().split("\n\n")

    points = set((int(p[0]), int(p[1])) for p in re.findall("(\d+),(\d+)", points.strip()))
    folds = [(x=="x",int(d)) for x,d in re.findall("fold along (x|y)=(\d+)", folds)]

    print(f'Part 1: {part1(points, folds)}')
    print(f'Part 2: ')
    part2(points, folds)

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)