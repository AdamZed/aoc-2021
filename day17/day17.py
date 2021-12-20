REGION = { 'X': (20, 30), 'Y': (-10, -5)} if False else {'X': (195, 238), 'Y': (-93, -67)}

def inRange(e, pair):
    return 

def probe(dx, dy):
    x, y = 0, 0 
    h = 0
    while True:
        x, y = x+dx, y+dy
        dy -= 1
        if dx > 0: dx -= 1
        h = max(h, y)

        if (REGION['X'][0] <= x <= REGION['X'][1] and
            REGION['Y'][0] <= y <= REGION['Y'][1]):
            return h

        if x > REGION['X'][1]: return None
        if dx == 0 and not (REGION['X'][0] <= x <= REGION['X'][1]):
            return None
        if dy < 0 and y < REGION['Y'][0]:
            return None
    
def part1():
    for dx in range(238):
        for dy in range(100, 0, -1):
            if (high:=probe(dx, dy)):
                return high

def part2():
    t = 0
    for dx in range(500):
        for dy in range(-93, 100):
            if probe(dx, dy) is not None:
                t += 1
    return t

def main():
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')

if __name__ == "__main__":
    main()