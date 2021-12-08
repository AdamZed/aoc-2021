def part1(data):
    gamma = [str(int(sum(y) > len(data)/2))
            for y in zip(*[[int(x) for x in d] for d in data])]
    epsilon = [str(int(x) ^ 1) for x in gamma]
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

def part2(data):
    def sonar(data, opp=False):
        a, b = ('0', '1') if opp else ('1', '0')
        bits = [0] * len(data[0])
        for i in range(len(bits)):
            for bit in data:
                bits[i] += int(bit[i])
            bits[i] = a if bits[i] >= len(data)/2 else b
            data = [x for x in data if x[i] == bits[i]]
            if len(data) == 1: break
        return int(data[0], 2)
    return sonar(data) * sonar(data, True)

def main():
    with open('input.txt') as f:
        data = [n.strip() for n in f.readlines() if len(n.strip()) > 0]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    main()
