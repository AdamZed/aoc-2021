from collections import deque

SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
MATCH = {")": "(", "]": "[", "}": "{", ">": "<"}
SCOR2 = {"(": 1, "[": 2, "{": 3, "<": 4}
MATHC = {v: k for k, v in MATCH.items()}

def brackify(ent):
    stack = deque()
    for ch in ent:
        if ch in MATCH.keys():
            if MATCH[ch] != stack.pop():
                return SCORE[ch], True
        else: stack.append(ch)
    score = 0
    while len(stack) > 0:
        score = score * 5 + SCOR2[stack.pop()]
    return score, False

def part1(data):
    return sum(score[0] for ent in data if (score:=brackify(ent))[1])

def part2(data):
    scores = sorted(score[0] for ent in data if not (score:=brackify(ent))[1])
    return scores[len(scores)//2]

def main(fname):
    with open(fname) as f:
        data = f.read().strip().split("\n")

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1]
    main(filename)
