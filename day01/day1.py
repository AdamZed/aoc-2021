def part1(nums):
    return sum(1 for l, r in zip(nums, nums[1:]) if l < r)

def part2(nums):
    return part1([nums[i]+nums[i+1]+nums[i+2] for i in range(len(nums)-2)])

def main():
    with open('input.txt') as f:
        nums = [int(n) for n in f.readlines() if len(n.strip()) > 0]

    print(f'Part 1: {part1(nums)}')
    print(f'Part 2: {part2(nums)}')

if __name__ == "__main__":
    main()
