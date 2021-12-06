def check_bingo(board):
    checks = board + [[board[y][x] for y in range(len(board))] for x in range(len(board))]
    return any(sum(checks[i]) == -5 for i in range(len(checks)))

def score(board, call):
    return sum(map(sum, [filter(lambda x: x > 0, row) for row in board])) * call

def mark(board, call):
    for row in board:
        for i, n in enumerate(row):
            if n == call: row[i] = -1

def part1(calls, boards):
    for call in calls:
        for i in range(len(boards)):
            mark(boards[i], call)
            if check_bingo(boards[i]):
                return score(boards[i], call)

def part2(calls, boards):
    for call in calls:
        for i in range(len(boards)):
            mark(boards[i], call)
        if len(boards) > 1:
            boards = [board for board in boards if not check_bingo(board)]
        elif check_bingo(boards[0]): return score(boards[0], call)
    
def main():
    with open('input.txt') as f:
        data = [n for n in f.readlines() if len(n.strip()) > 0]

    calls = [int(c) for c in data[0].split(',')]
    data = data[1:]
    boards = list()
    while len(data) > 0:
        board = data[:5]
        board = [[int(col) for col in row.strip().split()] for row in board]
        boards.append(board)
        data = data[5:]

    print(f'Part 1: {part1(calls, boards)}')
    print(f'Part 2: {part2(calls, boards)}')

if __name__ == "__main__":
    main()
