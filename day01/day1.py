import math

with open('input.txt') as f:
    nums = [int(n) for n in f.readlines() if len(n.strip())>0]

def part1(nums):
    return sum(1 for e in zip(nums, [math.inf] + nums[:-1]) if e[0] > e[1])

def part2(nums):
    windows = []
    for i in range(2, len(nums)):
        windows.append(nums[i]+nums[i-1]+nums[i-2])
    return part1(windows)


print(f'Part 1: {part1(nums)}')
print(f'Part 2: {part2(nums)}')