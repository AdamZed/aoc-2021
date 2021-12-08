BASE_MAP = {2: 1,  3: 7,  4: 4,  7: 8}
# 1 => 2
# 7 => 3
# 4 => 4
# 2 => 5, 3 => 5, 5 => 5
# 0 => 6, 6 => 6, 9 => 6
# 8 => 7

def part1(data):
    return sum(sum(1 for ent in out if len(ent) in BASE_MAP.keys()) for _,out in data)

def strsrt(s):
    return ''.join(sorted(s))

def isct(s1, s2):
    return ''.join(c for c in s1 if c in s2)

def getBaseFour(data):
    return {ent:BASE_MAP[len(ent)] for ent in data if len(ent) in BASE_MAP.keys()}

def decode(inp):
    nums = getBaseFour(strsrt(e) for e in inp)
    lets = {v:k for k,v in nums.items()}
    for ent in inp:
        ent = strsrt(ent)
        if len(ent) == 5:
            if len(isct(lets[1], ent)) == 2: nums[ent] = 3
            elif len(isct(lets[4], ent)) == 3: nums[ent] = 5
            else: nums[ent] = 2
        elif len(ent) == 6:
            if len(isct(lets[1], ent)) != 2: nums[ent] = 6
            elif len(isct(lets[4], ent)) == 4: nums[ent] = 9
            else: nums[ent] = 0
    return nums

def numerize(out, decoded):
    return sum(10**(3-i) * decoded[strsrt(n)] for i,n in enumerate(out))

def part2(data):
    return sum(numerize(out, decode(inp)) for inp,out in data)

def main(fname):
    with open(fname) as f:
        data = [x.split(' | ') for x in f.read().strip().split('\n')]
    data = [(a.split(' '), b.split(' ')) for (a,b) in data]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)